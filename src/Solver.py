import numpy as np
import heapq

def calculate_cost(matrix, gradient_matrix):
    return np.sum(np.abs(matrix - gradient_matrix))



def generate_successors(matrix, fixed_indices):
    successors = []
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if (i, j) in fixed_indices:
                continue
            for k in range(n):
                for l in range(n):
                    if (k, l) in fixed_indices or (i == k and j == l):
                        continue
                    new_matrix = matrix.copy()
                    new_matrix[i][j], new_matrix[k] [l] = new_matrix[k] [l], new_matrix[i] [j]
                    successors.append(new_matrix)
    return successors


def ucs(matrix, fixed_indices, gradient_matrix):
    n = matrix.shape[0]
    initial_state = matrix.copy()
    initial_cost = calculate_cost(matrix, gradient_matrix)

    pq = [(initial_cost, initial_state)]
    heapq.heapify(pq)
    visited = set()

    while pq:
        cost, current_matrix = heapq.heappop(pq)
        current_tuple = tuple(map(tuple, current_matrix))

        if current_tuple in visited:
            continue
        visited.add(current_tuple)

        if cost == 0:
            return current_matrix

        for successor in generate_successors(current_matrix, fixed_indices):
            new_cost = calculate_cost(successor, gradient_matrix)
            heapq.heappush(pq, (new_cost, successor))

    return None

if __name__ == '__main__':

    # n = 4
    matrix = [
    [(255, 0, 0), (255, 60, 0), (255, 120, 10), (255, 206, 12)],
    [(255, 0, 255), (0, 255, 255), (255, 255, 255), (128, 128, 128)],
    [(128, 0, 0), (0, 128, 0), (0, 0, 128), (128, 128, 0)],
    [(0, 128, 128), (128, 0, 128), (192, 192, 192), (64, 64, 64)]]
    n = len(matrix)
    fixed_indices = [(0, 0), (0, n - 1), (n - 1, 0), (n - 1, n - 1)]
    t = generate_successors(matrix, fixed_indices)
    for i in t:
        print(i)
    print(len(t))
    # gradient_matrix = np.zeros((n, n, 3))
    #
    # # Define the desired gradient values
    # gradient_matrix[0, 0] = matrix[0][0]
    # gradient_matrix[0, n - 1] = matrix[0][n - 1]
    # gradient_matrix[n - 1, 0] = matrix[n - 1][0]
    # gradient_matrix[n - 1, n - 1] = matrix[n - 1][n - 1]
    #
    # # Fill the gradient matrix (manually, based on desired gradient)
    # # This is an example; you might want to create a more complex gradient
    # for i in range(n):
    #     for j in range(n):
    #         if (i, j) in fixed_indices:
    #             continue
    #         gradient_matrix[i, j] = (gradient_matrix[0, 0] * (n - i - 1) * (n - j - 1) +
    #                                  gradient_matrix[0, n - 1] * (n - i - 1) * j +
    #                                  gradient_matrix[n - 1, 0] * i * (n - j - 1) +
    #                                  gradient_matrix[n - 1, n - 1] * i * j) / (n * n)
    #
    # sorted_matrix = ucs(matrix, fixed_indices, gradient_matrix)
    # print(sorted_matrix)