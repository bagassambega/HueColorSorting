from src import RGB
class Node:
    def __init__(self, data:list[list[RGB]] | None):
        self.data = data
        self.parent = None