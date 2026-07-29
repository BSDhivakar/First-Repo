flat_leaf_nodes = [
    3, 5, 6, 9, 1, 2, 0, -1,
    7, 4, 5, 8, 9, 6, 2, 1,
    4, 8, 6, 7, 3, 2, 9, 5,
    1, 6, 4, 8, 7, 5, 2, 3
]

nodes_evaluated = 0


def minimax(values, is_max_player, level_name):
    global nodes_evaluated

    if len(values) == 1:
        return values[0]

    next_level = []

    for i in range(0, len(values), 2):
        left = values[i]
        right = values[i + 1]

        nodes_evaluated += 2

        if is_max_player:
            value = max(left, right)
        else:
            value = min(left, right)

        next_level.append(value)

        print(f"{level_name} ({'MAX' if is_max_player else 'MIN'}): "
              f"{left}, {right} -> {value}")

    return minimax(
        next_level,
        not is_max_player,
        f"Level {int(level_name.split()[-1]) - 1}"
    )


print("Root Player : MAX\n")

# -------------------------------------------------
# Step 1 : Each terminal node has 4 leaf values
# (B1, B2, ..., B8 are MIN nodes)
# -------------------------------------------------

terminal_nodes = []

for i in range(0, len(flat_leaf_nodes), 4):
    group = flat_leaf_nodes[i:i + 4]

    nodes_evaluated += 4

    value = min(group)

    terminal_nodes.append(value)

    print(f"Terminal Node B{i//4 + 1} (MIN): {group} -> {value}")

print()

# -------------------------------------------------
# Continue normal binary minimax
# MAX -> MIN -> MAX
# -------------------------------------------------

root_value = minimax(
    terminal_nodes,
    is_max_player=True,
    level_name="Level 2"
)

print(f"\nRoot (MAX): {root_value}")

total_nodes = 47

print("\nStatistics")
print(f"Depth of Tree              : 5")
print(f"Branching Factor           : 2 (4 at terminal level)")
print(f"Total Nodes                : {total_nodes}")
print(f"Terminal Leaf Nodes        : {len(flat_leaf_nodes)}")
print(f"Terminal Parent Nodes      : {len(terminal_nodes)}")
print(f"Internal Nodes             : 15")
print(f"Nodes Evaluated            : {nodes_evaluated}")
print("Time Complexity            : O(b^m)")
print("Algorithm                  : Minimax")