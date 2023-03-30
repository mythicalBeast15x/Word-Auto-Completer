class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.is_word = False
        self.is_root = None

    def get_children(self):
        return sorted(list(self.children.keys()))
