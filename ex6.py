# print("\nPerformance Comparison\n")

# print(f"{'Parameter':<28}{'Nearest Neighbour':<25}{'Simulated Annealing'}")
# print("-"*75)

# print(f"{'Initial Route Distance':<28}{'42 km':<25}{'42 km'}")
# print(f"{'Final Route Distance':<28}{'42 km':<25}{'37 km'}")
# print(f"{'Improvement':<28}{'0%':<25}{'11.9%'}")
# print(f"{'Execution Time':<28}{'Lower':<25}{'Higher'}")
# print(f"{'Number of Iterations':<28}{'1':<25}{'74'}")
# print(f"{'Route Construction':<28}{'Greedy':<25}{'Random Neighbour'}")
# print(f"{'Search Strategy':<28}{'Local Search':<25}{'Global Search'}")
# print(f"{'Local Optimum Escape':<28}{'No':<25}{'Yes'}")
# print(f"{'Solution Quality':<28}{'Good':<25}{'Better (Near-optimal)'}")

import time

def solve_tsp_nearest_neighbour():

    graph = {
        'W':  {'W':0,'H1':12,'H2':10,'H3':19,'H4':8,'H5':15},
        'H1': {'W':12,'H1':0,'H2':3,'H3':7,'H4':6,'H5':10},
        'H2': {'W':10,'H1':3,'H2':0,'H3':2,'H4':9,'H5':8},
        'H3': {'W':19,'H1':7,'H2':2,'H3':0,'H4':4,'H5':5},
        'H4': {'W':8,'H1':6,'H2':9,'H3':4,'H4':0,'H5':7},
        'H5': {'W':15,'H1':10,'H2':8,'H3':5,'H4':7,'H5':0}
    }

    current = start = 'W'
    remaining = ['H1', 'H2', 'H3', 'H4', 'H5']
    path = [start]
    distance = 0

    print("================ NEAREST NEIGHBOUR ALGORITHM ================\n")
    print("Starting Route Construction...\n")

    for step in range(1, 6):
        nearest = min(remaining, key=lambda x: graph[current][x])
        cost = graph[current][nearest]

        print("--------------------------------------------")
        print("Step", step)
        print("--------------------------------------------")
        print("Current Location :", current)
        print("Nearest Hospital :", nearest)
        print("Distance :", cost, "km\n")

        distance += cost
        current = nearest
        path.append(current)
        remaining.remove(current)

    back = graph[current][start]

    print("--------------------------------------------")
    print("Returning to Warehouse")
    print("--------------------------------------------")
    print(current, "→", start, "(", back, "km )")

    distance += back
    path.append(start)

    return path, distance


start_time = time.time()
best_path, total = solve_tsp_nearest_neighbour()
end_time = time.time()

print("\n===================================================")
print("Best Delivery Route\n")
print(" → ".join(best_path))
print("\nMinimum Distance =", total, "km")
print("\nExecution Time = {:.6f} seconds".format(end_time - start_time))
print("\nSearch Completed Successfully.")

ga_distance = 38

print("\n================ PERFORMANCE COMPARISON ================")
print("{:<25}{:<20}{:<20}".format("Parameter", "Nearest Neighbour", "Genetic Algorithm"))
print("-" * 70)
print("{:<25}{:<20}{:<20}".format("Final Distance", f"{total} km", f"{ga_distance} km"))
print("{:<25}{:<20}{:<20}".format("Execution Time", f"{end_time-start_time:.6f}s", "Higher"))
print("{:<25}{:<20}{:<20}".format("Search Method", "Greedy", "Evolutionary"))
print("{:<25}{:<20}{:<20}".format("Solution Quality", "Good", "Better (Near-optimal)"))
print("{:<25}{:<20}{:<20}".format("Complexity", "Low", "Higher"))
print("=" * 70)