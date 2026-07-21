flat_leaf_nodes = [
    3, 5, 6, 9, 1, 2, 0, -1,
    7, 4, 5, 8, 9, 6, 2, 1,
    4, 8, 6, 7, 3, 2, 9, 5,
    1, 6, 4, 8, 7, 5, 2, 3
]

TREE_DEPTH = 5
TOTAL_NODES = 63

nodes_evaluated = 0
best_path = []


def alpha_beta(depth, index, is_max, alpha, beta, path):
    global nodes_evaluated, best_path

    if depth == 0:
        nodes_evaluated += 1
        print(f"Terminal Node [{index}] = {flat_leaf_nodes[index]}")
        return flat_leaf_nodes[index]

    print(f"\n{'MAX' if is_max else 'MIN'} Node")
    print(f"Alpha = {alpha if alpha != float('-inf') else '-INF'}")
    print(f"Beta = {beta if beta != float('inf') else '+INF'}")

    best = float("-inf") if is_max else float("inf")

    for i in range(2):
        direction = "Left Subtree" if i == 0 else "Right Subtree"

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


print("ALPHA-BETA PRUNING")
print("\nRoot Player : MAX")
print("Starting Search...\n")

optimal_value = alpha_beta(
    TREE_DEPTH,
    0,
    True,
    float("-inf"),
    float("inf"),
    ["MAX"]
)

print("\nSearch Completed")

print(f"\nOptimal Utility Value : {optimal_value}")

print("\nOptimal Decision Path")
print("MAX")
for step in best_path:
    print("↓")
    print(step)
print("↓")
print("Terminal Node")

print("\nPerformance Statistics")
print(f"Total Nodes      : {TOTAL_NODES}")
print(f"Nodes Evaluated  : {nodes_evaluated}")
print(f"Nodes Pruned     : {TOTAL_NODES - nodes_evaluated}")
print(f"Optimal Utility  : {optimal_value}")

print("\nPerformance Comparison")
print(f"{'Algorithm':<15}{'Evaluated':<15}{'Pruned'}")
print(f"{'Minimax':<15}{32:<15}{0}")
print(f"{'Alpha-Beta':<15}{nodes_evaluated:<15}{TOTAL_NODES - nodes_evaluated}")

print(f"\nOptimal Utility Value : {optimal_value}")

print("\nConclusion")
print("Alpha-Beta gives the same result as Minimax")
print("while evaluating fewer nodes by pruning unnecessary branches.")