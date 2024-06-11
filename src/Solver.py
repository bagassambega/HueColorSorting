import colorsys
import math

import ColorImage
from Node import Node


def sort_by_cost(priority_queue:list[Node]):
    priority_queue.sort(key=lambda x: (x.cost + x.heuristic))
    print([x.heuristic for x in priority_queue][:10])
    return priority_queue


def generate_successors(matrix, fixed_indices):
    successors = []
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if (i, j) in fixed_indices:
                continue
            for k in range(n):
                for l in range(n):
                    if (k, l) in fixed_indices:
                        continue
                    new_matrix = [row.copy() for row in matrix]
                    new_matrix[i][j], new_matrix[k][l] = new_matrix[k][l], new_matrix[i][j]
                    successors.append(new_matrix)
    return successors

visited = []
def UCS(matrix, fixed_position):
    pq = Node(matrix, 0)
    priority_queue:list[Node] = [pq]

    while len(priority_queue) > 0:
        priority_queue = sort_by_cost(priority_queue)
        current_node = priority_queue.pop(0)
        current_state = current_node.data

        if current_node.heuristic == 0:
            return current_state

        if current_state in visited:
            continue

        visited.append(current_state)

        successors = generate_successors(current_state, fixed_position)
        for successor in successors:
            if successor not in visited:
                priority_queue.append(Node(successor, current_node.cost+1))
            # if successor == target:
            #     return successor

    return None

def convert_to_hsv(matrix):
    n = len(matrix)
    hsv_matrix = []
    for i in range(n):
        hsv_matrix.append([])
        for j in range(n):
            r, g, b = matrix[i][j]
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
            hsv_matrix[i].append((h, s, v))
    return hsv_matrix

if __name__ == '__main__':
    matrix = [
    [(232, 150, 139), (229, 171, 134), (140, 131, 160), (94, 122, 170)],
    [(186, 140, 150), (175, 185, 148), (84, 145, 176), (133, 153, 162)],
    [(225, 193, 132), (180, 162, 150), (169, 207, 148), (124, 176, 164)],
    [(222, 216, 128), (74, 167, 182), (116, 199, 169), (64, 190, 187)]]

    target = [
    [(232, 150, 139), (186, 140, 150), (140, 131, 160), (94, 122, 170)],
    [(229, 171, 134), (180, 162, 150), (133, 153, 162), (84, 145, 176)],
    [(225, 193, 132), (175, 185, 148), (124, 176, 164), (74, 167, 182)],
    [(222, 216, 128), (169, 207, 148), (116, 199, 169), (64, 190, 187)]]

    ColorImage.generate_image_from_rgb_matrix(target, 100, 'color.png')
    ColorImage.generate_image_from_rgb_matrix(matrix, 100, 'start.png')
    n = len(matrix)
    fixed_indices = [(0, 0), (0, n - 1), (n - 1, 0), (n - 1, n - 1)]
    print(Node.calculate_heuristic(Node(matrix, 0)))
    temp = UCS(matrix, fixed_indices)
    ColorImage.generate_image_from_rgb_matrix(temp, 100, 'end.png')
