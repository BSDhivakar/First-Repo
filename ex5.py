flat_leaf_nodes = [
    3, 5, 6, 9,
    1, 2, 0, -1,
    7, 4, 5, 8,
    9, 6, 2, 1,
    4, 8, 6, 7,
    3, 2, 9, 5,
    1, 6, 4, 8,
    7, 5, 2, 3
]

TREE_DEPTH = 4          # A -> D -> C -> B -> Terminal
TOTAL_NODES = 47        # 1 + 2 + 4 + 8 + 32

nodes_evaluated = 0
best_path = []


def alpha_beta(depth, index, is_max, alpha, beta, path):
    global nodes_evaluated, best_path

    # ---------------- B NODE ----------------
    # B nodes have 4 terminal children
    if depth == 1:

        print(f"\n{'MAX' if is_max else 'MIN'} Node")
        print(f"Alpha = {alpha if alpha != float('-inf') else '-INF'}")
        print(f"Beta  = {beta if beta != float('inf') else '+INF'}")

        best = float("-inf") if is_max else float("inf")

        for i in range(4):

            leaf_index = index * 4 + i
            value = flat_leaf_nodes[leaf_index]

            nodes_evaluated += 1
            print(f"Terminal Node [{leaf_index}] = {value}")

            if is_max:
                best = max(best, value)
                alpha = max(alpha, best)
                print(f"Updated Alpha = {alpha}")
            else:
                best = min(best, value)
                beta = min(beta, best)
                print(f"Updated Beta = {beta}")

            if beta <= alpha:
                print("Pruning Remaining Branches")
                break

        return best

    # ---------------- INTERNAL NODE ----------------

    print(f"\n{'MAX' if is_max else 'MIN'} Node")
    print(f"Alpha = {alpha if alpha != float('-inf') else '-INF'}")
    print(f"Beta  = {beta if beta != float('inf') else '+INF'}")

    best = float("-inf") if is_max else float("inf")

    for i, direction in enumerate(("Left Subtree", "Right Subtree")):

        value = alpha_beta(
            depth - 1,
            index * 2 + i,
            not is_max,
            alpha,
            beta,
            path + [direction]
        )

        if is_max:
            if value > best:
                best = value
                if depth == TREE_DEPTH:
                    best_path = path + [direction]

            alpha = max(alpha, best)
            print(f"Updated Alpha = {alpha}")

        else:
            best = min(best, value)
            beta = min(beta, best)
            print(f"Updated Beta = {beta}")

        if beta <= alpha:
            print("Pruning Remaining Branches")
            break

    return best


def main():

    print("================ ALPHA-BETA PRUNING ================")
    print("Game Tree Loaded Successfully.")
    print("Root Player : MAX")
    print("Starting Alpha-Beta Search...\n")
    print("----------------------------------------------------")

    optimal_value = alpha_beta(
        TREE_DEPTH,
        0,
        True,
        float("-inf"),
        float("inf"),
        ["MAX"]
    )

    print("\n----------------------------------------------------")
    print("Search Completed Successfully.")

    print(f"\nOptimal Utility Value : {optimal_value}")

    print("\nOptimal Decision Path")
    print("MAX")
    for step in best_path:
        print("↓")
        print(step)
    print("↓")
    print("Terminal Node")

    print("\n----------------------------------------------------")
    print("Performance Statistics")
    print("----------------------------------------------------")
    print(f"Total Nodes      : {TOTAL_NODES}")
    print(f"Nodes Evaluated  : {nodes_evaluated}")
    print(f"Nodes Pruned     : {TOTAL_NODES - nodes_evaluated}")
    print(f"Optimal Utility  : {optimal_value}")

    print("\nPerformance Comparison")
    print(f"{'Algorithm':<15}{'Evaluated':<15}{'Pruned'}")
    print(f"{'Minimax':<15}{32:<15}{0}")
    print(f"{'Alpha-Beta':<15}{nodes_evaluated:<15}{TOTAL_NODES - nodes_evaluated}")

    print("\nConclusion")
    print("Alpha-Beta gives the same result as Minimax")
    print("while evaluating fewer nodes by pruning unnecessary branches.")


if __name__ == "__main__":
    main()