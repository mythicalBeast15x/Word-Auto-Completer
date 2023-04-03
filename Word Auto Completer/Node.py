# Node class that represents a letter in the tree data structure.
# Multiple nodes can represent the same letter but determining
# if that node is a word will help distinguish what word it is.

class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}  # Represents each letter in the connection.
        self.is_word = False
        self.is_root = None

    # Gets each child of the associated node and returns the children.
    def get_children(self):
        return sorted(list(self.children.keys()))
