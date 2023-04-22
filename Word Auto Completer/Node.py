'''
Node class that represents a letter in the tree data structure.
Multiple nodes can represent the same letter but determining
if that node is a word will help distinguish what word it is.
'''

class Node:
    """The node class that will represents letters and hold references
    to any letters that it might be connected to.

    Attributes:
        data: chr
        children: dictionary
        is_word: Boolean
        is_Root: Node
    """

    def __init__(self, data: chr) -> None:
        """The node constructor.

        Args:
            data (chr): A letter of a word.
        """

        self.data = data
        self.children = {}  # Represents each letter in the connection.
        self.is_word = False
        self.is_root = None

    def get_children(self) -> list:
        """Gets each child of the associated node and returns the children.

        Returns:
            list: A list of the characters that are children of the current node.
        """

        return sorted(list(self.children.keys()))
