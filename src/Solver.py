import ColorImage
import time
from Node import Node


def sort_by_cost(priority_queue:list[Node]):
    priority_queue.sort(key=lambda x: x.fn)
    # print([x.heuristic for x in priority_queue][:10])
    return priority_queue


def generate_successors(node:Node, fixed_indices) -> list[Node]:
    successors = []
    n = len(node.data)
    for i in range(n):
        for j in range(n):
            if (i, j) in fixed_indices:
                continue
            for k in range(n):
                for l in range(n):
                    if (k, l) in fixed_indices or (i, j) == (k, l):
                        continue
                    new_matrix = [row.copy() for row in node.data]
                    new_matrix[i][j], new_matrix[k][l] = new_matrix[k][l], new_matrix[i][j]
                    successors.append(Node(new_matrix, node.cost+1, node, [(i, j), (k, l)]))
    return successors


visited = []
def solve(matrix, fixed_position):
    pq = Node(matrix, 0, None, [])
    print(pq.heuristic)
    if pq.heuristic == 0:
        return pq.data, []
    priority_queue:list[Node] = [pq]

    while len(priority_queue) > 0:
        priority_queue = sort_by_cost(priority_queue)
        current_node = priority_queue.pop(0)
        current_state = current_node.data

        if current_node.heuristic == 0:
            changes = []
            while current_node.parent is not None:
                changes += current_node.changes
                current_node = current_node.parent
            changes.reverse()

            return current_state, changes

        if current_state in visited:
            continue

        visited.append(current_state)

        successors = generate_successors(current_node, fixed_position)
        for successor in successors:
            if successor.data not in visited:
                priority_queue.append(successor)

    return None, None


if __name__ == '__main__':
    fileInput = input("File name to be sort (the file will be relative to folder test): ")
    matrix = ColorImage.convert_image_to_rgb_matrix(fileInput + '.png', 100)
    n = len(matrix)
    fixed_indices = [(0, 0), (0, n - 1), (n - 1, 0), (n - 1, n - 1)]
    time_start = time.time()
    temp, changes = solve(matrix, fixed_indices)
    time_end = time.time()
    if temp is None:
        print("No solution found")
    else:
        fileOutput = input("File name to save the sorted image (the file will be relative to folder test): ")
        ColorImage.generate_image_from_rgb_matrix(temp, 100, fileOutput + '.png')
        for i in range(0, len(changes), 2):
            print(f"{changes[i]} - {changes[i+1]}")
        print(f"Changes done in {len(changes) // 2} moves")
        print(f"Iterated in {len(visited)}")
    print(f"Time taken: {time_end - time_start}")