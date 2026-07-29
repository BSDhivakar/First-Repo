class Node:
    def __init__(self, name, level, player=None, value=None):
        self.name, self.level = name, level
        self.player, self.value = player, value
        self.children, self.chosen_child = [], None


def build_tree():
    terminal_rows = [
        [3,5,6,9],[1,2,0,-1],[7,4,5,8],[9,6,2,1],
        [4,8,6,7],[3,2,9,5],[1,6,4,8],[7,5,2,3]
    ]

    level3, leaf = [], 1
    for i, row in enumerate(terminal_rows, 1):
        node = Node(f"B{i}", 3, "MIN")
        for val in row:
            node.children.append(Node(f"T{leaf}", 4, value=val))
            leaf += 1
        level3.append(node)

    level2 = []
    for i in range(4):
        node = Node(f"C{i+1}", 2, "MAX")
        node.children = level3[2*i:2*i+2]
        level2.append(node)

    level1 = []
    for i in range(2):
        node = Node(f"D{i+1}", 1, "MIN")
        node.children = level2[2*i:2*i+2]
        level1.append(node)

    root = Node("A", 0, "MAX")
    root.children = level1
    return root


nodes_evaluated = 0

def alphabeta(node, alpha, beta):
    global nodes_evaluated
    nodes_evaluated += 1

    if not node.children:
        return node.value

    if node.player == "MAX":
        best = float("-inf")
        for child in node.children:
            val = alphabeta(child, alpha, beta)
            if val > best:
                best, node.chosen_child = val, child
            alpha = max(alpha, best)
            print(f"  Node {node.name} (MAX): alpha={alpha}, beta={beta}")
            if beta <= alpha:
                print(f"  --> Pruning remaining children of {node.name} (beta <= alpha)")
                break
    else:
        best = float("inf")
        for child in node.children:
            val = alphabeta(child, alpha, beta)
            if val < best:
                best, node.chosen_child = val, child
            beta = min(beta, best)
            print(f"  Node {node.name} (MIN): alpha={alpha}, beta={beta}")
            if beta <= alpha:
                print(f"  --> Pruning remaining children of {node.name} (beta <= alpha)")
                break

    node.value = best
    return best


def trace_path(node):
    path = []
    while node:
        path.append(node)
        node = node.chosen_child
    return path


def count_nodes(node):
    if not node.children:
        return 1, 0, 1
    total = internal = 1
    terminal = 0
    for child in node.children:
        t, i, l = count_nodes(child)
        total += t
        internal += i
        terminal += l
    return total, internal, terminal


def main():
    root = build_tree()

    optimal = alphabeta(root, float("-inf"), float("inf"))

    print("\nSearch Completed Successfully.")
    print("Optimal Utility Value :", optimal)

    print("\nOptimal Decision Path:")
    print(" -> ".join(n.name for n in trace_path(root)))

    total, _, _ = count_nodes(root)

    print("Performance Statistics")
    print(f"Total Nodes in Game Tree      : {total}")
    print(f"Nodes Evaluated               : {nodes_evaluated}")
    print(f"Nodes Pruned                  : {total - nodes_evaluated}")
    print(f"Optimal Utility               : {optimal}")


if __name__ == "__main__":
    main()