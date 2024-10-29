import sys
from typing import List, Set


class TSPSolver:
    def __init__(self, n: int, cost_matrix: List[List[int]]):
        """
        Initialize TSP solver

        Args:
            n: Number of cities
            cost_matrix: Matrix of costs between cities
        """
        self.N = n
        self.cost_matrix = cost_matrix
        self.final_path = [None] * (n + 1)  # Store final solution
        self.visited = [False] * n  # Keep track of visited vertices
        self.final_cost = sys.maxsize  # Store final minimum cost

    def copy_solution(self, curr_path: List[int]) -> None:
        """Copy current solution path to final path"""
        self.final_path[:self.N] = curr_path[:]
        self.final_path[self.N] = curr_path[0]

    def first_min(self, i: int) -> int:
        """Find minimum cost edge from vertex i"""
        minimum = sys.maxsize
        for k in range(self.N):
            if self.cost_matrix[i][k] < minimum and i != k:
                minimum = self.cost_matrix[i][k]
        return minimum

    def second_min(self, i: int) -> int:
        """Find second minimum cost edge from vertex i"""
        first, second = sys.maxsize, sys.maxsize
        for j in range(self.N):
            if i == j:
                continue
            if self.cost_matrix[i][j] <= first:
                second = first
                first = self.cost_matrix[i][j]
            elif self.cost_matrix[i][j] <= second and self.cost_matrix[i][j] != first:
                second = self.cost_matrix[i][j]
        return second

    def tsp_recursive(self, curr_bound: int, curr_weight: int, level: int,
                      curr_path: List[int], curr_included: Set[int]) -> None:
        """
        Recursive function to solve TSP using Branch and Bound

        Args:
            curr_bound: Current lower bound
            curr_weight: Current path weight
            level: Current level in decision tree
            curr_path: Current path being explored
            curr_included: Set of vertices included in current path
        """
        if level == self.N:
            # Check if we can complete the cycle
            if self.cost_matrix[curr_path[level - 1]][curr_path[0]] != 0:
                curr_res = curr_weight + self.cost_matrix[curr_path[level - 1]][curr_path[0]]
                if curr_res < self.final_cost:
                    self.copy_solution(curr_path)
                    self.final_cost = curr_res
            return

        for i in range(self.N):
            if self.cost_matrix[curr_path[level - 1]][i] != 0 and not self.visited[i]:
                temp = curr_bound
                curr_weight += self.cost_matrix[curr_path[level - 1]][i]

                # Calculate bound for the current node
                if level == 1:
                    curr_bound -= ((self.first_min(curr_path[level - 1]) +
                                    self.first_min(i)) / 2)
                else:
                    curr_bound -= ((self.second_min(curr_path[level - 1]) +
                                    self.first_min(i)) / 2)

                # If current bound + weight is less than final_cost, explore path
                if curr_bound + curr_weight < self.final_cost:
                    curr_path[level] = i
                    curr_included.add(i)
                    self.visited[i] = True

                    self.tsp_recursive(curr_bound, curr_weight, level + 1,
                                       curr_path, curr_included)

                    # Backtrack
                    curr_included.remove(i)
                    self.visited[i] = False

                # Reset changes
                curr_weight -= self.cost_matrix[curr_path[level - 1]][i]
                curr_bound = temp

    def solve(self) -> tuple:
        """
        Solve the TSP problem

        Returns:
            Tuple of (minimum cost, optimal path)
        """
        curr_bound = 0
        curr_path = [-1] * (self.N + 1)
        self.visited = [False] * self.N

        # Calculate initial bound
        for i in range(self.N):
            curr_bound += (self.first_min(i) + self.second_min(i))

        curr_bound = curr_bound // 2

        # Start from vertex 0
        self.visited[0] = True
        curr_path[0] = 0

        curr_included = {0}

        # Call recursive function
        self.tsp_recursive(curr_bound, 0, 1, curr_path, curr_included)

        return self.final_cost, self.final_path


# Example usage
if __name__ == "__main__":
    # Cost matrix from the problem
    cost_matrix = [
        [0, 3, 14, 18, 15],
        [3, 0, 4, 22, 20],
        [17, 9, 0, 16, 4],
        [6, 2, 7, 0, 12],
        [9, 15, 11, 5, 0]
    ]

    n = 5  # Number of cities
    solver = TSPSolver(n, cost_matrix)
    min_cost, optimal_path = solver.solve()

    print(f"Minimum cost: {min_cost}")
    print("Optimal path:", end=" ")
    for i in optimal_path:
        if i is not None:
            print(i + 1, end=" ")  # Adding 1 to convert to 1-based indexing
    print()