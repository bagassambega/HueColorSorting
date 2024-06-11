import math


class Node:
    def __init__(self, data:list[list[tuple]] | None, cost:int):
        self.data = data
        self.cost = cost
        self.heuristic = self.calculate_heuristic()
    
    @staticmethod
    def calculate_distance(color1, color2):
        return math.sqrt(sum((color1[i] - color2[i]) ** 2 for i in range(3)))

    @staticmethod
    def check_order(color1, color2, order):
        """
        :param color1: the color before
        :param color2: the color now/after
        :param order: the R, G, B order. True means increase, False means decrease
        :return: Is the order correct
        """
        for i in range(3):
            if order[i]:
                if color1[i] > color2[i]:
                    return False
            else:
                if color1[i] < color2[i]:
                    return False
        return True

    def calculate_heuristic(self):
        """
        Calculate how many pixels are not in the correct position
        :return:
        """
        wrong = 0
        n = len(self.data)

        # Check whether the order should increase or decrease for every R, G, B value. True means increase, False means decrease
        # Order horizontal for every row
        order_horizontal = [[self.data[j][0][i] < self.data[j][n - 1][i] for i in range(3)]for j in range(n)]
        # Order vertical for every column
        order_vertical = [[self.data[0][i][j] < self.data[n - 1][i][j] for j in range(3)]for i in range(n)]
        # print(order_horizontal, order_vertical)

        # Check the horizontal gradient
        for i in range(n):
            startH = self.data[i][0]
            endH = self.data[i][n - 1]
            distance_horizontal = Node.calculate_distance(startH, endH)
            for j in range(n):
                if Node.calculate_distance(self.data[i][j], endH) > distance_horizontal:
                    wrong += 1
                    # print("horizont dist")
                else:
                    if j > 0:
                        if not Node.check_order(self.data[i][j-1], self.data[i][j], order_horizontal[i]):
                            wrong += 1
                            # print("horizont order", self.data[i][j-1], self.data[i][j], order_horizontal[i])

        # Check the vertical gradient

        for i in range(n):
            startV = self.data[0][i]
            endV = self.data[n - 1][i]
            distance_vertical = Node.calculate_distance(startV, endV)
            for j in range(n):
                if Node.calculate_distance(self.data[j][i], endV) > distance_vertical:
                    wrong += 1
                    # print("vertical dist")
                else:
                    if j > 0:
                        if not Node.check_order(self.data[j-1][i], self.data[j][i], order_vertical[i]):
                            wrong += 1
                            # print("vertical order", self.data[j-1][i], self.data[j][i], order_vertical[i])


        return wrong
