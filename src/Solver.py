import ColorImage
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
def UCS(matrix, fixed_position):
    pq = Node(matrix, 0, None, [])
    priority_queue:list[Node] = [pq]

    while len(priority_queue) > 0:
        priority_queue = sort_by_cost(priority_queue)
        current_node = priority_queue.pop(0)
        current_state = current_node.data

        if current_node.heuristic == 0:
            changes = []
            while current_node.parent is not None:
                print(current_node.changes)
                changes += current_node.changes
                current_node = current_node.parent
            changes.reverse()
            print(len(changes))

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
    # t = [
    # [(232, 150, 139), (225, 193, 132), (140, 131, 160), (94, 122, 170)],
    # [(186, 140, 150), (175, 185, 148), (84, 145, 176), (133, 153, 162)],
    # [(180, 162, 150), (124, 176, 164), (169, 207, 148), (229, 171, 134)],
    # [(222, 216, 128),(116, 199, 169), (74, 167, 182), (64, 190, 187)]]
    # ColorImage.generate_image_from_rgb_matrix(t, 100, '../test/start.png')
    #
    # target = [
    # [(232, 150, 139), (186, 140, 150), (140, 131, 160), (94, 122, 170)],
    # [(229, 171, 134), (180, 162, 150), (133, 153, 162), (84, 145, 176)],
    # [(225, 193, 132), (175, 185, 148), (124, 176, 164), (74, 167, 182)],
    # [(222, 216, 128), (169, 207, 148), (116, 199, 169), (64, 190, 187)]]

    # ColorImage.generate_image_from_rgb_matrix(target, 100, '../test/color.png')
    # ColorImage.generate_image_from_rgb_matrix(matrix, 100, '../test/start.png')
    # n = len(matrix)
    # fixed_indices = [(0, 0), (0, n - 1), (n - 1, 0), (n - 1, n - 1)]
    # print(Node.calculate_heuristic(Node(matrix, 0)))
    # temp = UCS(matrix, fixed_indices)
    # ColorImage.generate_image_from_rgb_matrix(temp, 100, '../test/end.png')

    matrix = ColorImage.convert_image_to_rgb_matrix('../test/start.png', 100)
    n = len(matrix)
    fixed_indices = [(0, 0), (0, n - 1), (n - 1, 0), (n - 1, n - 1)]
    temp, changes = UCS(matrix, fixed_indices)
    if temp is None:
        print("No solution found")
    else:
        ColorImage.generate_image_from_rgb_matrix(temp, 100, '../test/end.png')
