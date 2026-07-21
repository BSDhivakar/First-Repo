class EightPuzzleHillClimbing:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.dimensions = 3

    def get_misplaced_tiles(self, state):
        count = 0
        for i in range(len(state)):
            if state[i] != '_' and state[i] != self.goal_state[i]:
                count += 1
        return count

    def generate_neighbors(self, state):
        neighbors = []
        blank_idx = state.index('_')
        row = blank_idx // self.dimensions
        col = blank_idx % self.dimensions

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < self.dimensions and 0 <= new_col < self.dimensions:
                neighbor_idx = new_row * self.dimensions + new_col

                state_list = list(state)
                state_list[blank_idx], state_list[neighbor_idx] = (
                    state_list[neighbor_idx],
                    state_list[blank_idx],
                )

                neighbors.append("".join(state_list))

        return neighbors

    def print_grid(self, state):
        for i in range(0, len(state), self.dimensions):
            print(" ".join(state[i:i + self.dimensions]))
        print()   # Blank line after each matrix

    def solve(self):
        current_state = self.initial_state
        moves_count = 0

        print("========== STARTING HILL CLIMBING SEARCH ==========")

        while True:
            current_h = self.get_misplaced_tiles(current_state)

            print(f"\nMove {moves_count}")
            print(f"Heuristic h = {current_h}")
            self.print_grid(current_state)

            # Goal Test
            if current_h == 0:
                print("\nSUCCESS: Goal State Reached!")
                self.report(moves_count, current_h, trapped=False)
                break

            neighbors = self.generate_neighbors(current_state)
            best_neighbor = None
            best_h = current_h

            print("\nEvaluating Neighboring States:")

            for idx, neighbor in enumerate(neighbors, start=1):
                neighbor_h = self.get_misplaced_tiles(neighbor)

                print(f"\nNeighbor {idx} (Heuristic h = {neighbor_h})")
                self.print_grid(neighbor)

                if neighbor_h < best_h:
                    best_h = neighbor_h
                    best_neighbor = neighbor

            if best_neighbor is None:
                print("\nTERMINATION: Stuck in a Local Optimum / Plateau.")
                self.report(moves_count, current_h, trapped=True)
                break

            current_state = best_neighbor
            moves_count += 1

    def report(self, total_moves, final_h, trapped):
        print("\n========== FINAL EXECUTION REPORT ==========")
        print(f"Total Moves Performed : {total_moves}")
        print(f"Final Heuristic Value : {final_h}")

        if trapped:
            print("Status                : Trapped in Local Optimum / Plateau")
        else:
            print("Status                : Goal Reached Successfully")


# Initial and Goal Configurations
initial_config = "2831647_5"
goal_config = "1238_4765"

# Create object and solve
solver = EightPuzzleHillClimbing(initial_config, goal_config)
solver.solve()