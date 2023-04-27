'''
The tree structure that will hold the all the letters
for the words. The tree will be traversed in order to
produce a word and determine how many words can come
from those combination of letters.
'''

from Node import Node


class Stack():
    """A basic stack.

    Attributes:
        stack: list
    """

    def __init__(self) -> None:
        """The constructor for the stack.
        """

        self.stack = []

    def push(self, data: chr) -> None:
        """Push data onto the stack.

        Args:
            data (chr): The data to be pushed.
        """

        self.stack.append(data)

    def pop(self) -> chr:
        """Remove and return data from the stack.

        Returns:
            _type_: Data from a word.
        """

        return self.stack.pop()

    def peek(self) -> chr:
        """Checks the top of the stack.

        Returns:
            _type_: The object at the top of the stack.
        """

        return self.stack[-1]

    def get_stack(self) -> list:
        """Get the stack.

        Returns:
            list: The whole stack.
        """

        return self.stack


class Tree:
    """The tree that will hold all information for every word.
    Each node acts as a letter in a word.

    Attributes:
        letters: list
        root: Node
        root.is_root: Boolean
    """

    letters = []

    def __init__(self) -> None:
        """Constructor for the tree.
        """

        self.root = Node(None)
        self.root.is_root = True
    '''
    #Creates a list of all lower case letters
    def create_letterLst(self):
        #ASCII code for lower case 'a'
        i = 97
        #122 is ASCII code for lower case 'z'
        while i <= 122:
            #Converts ASCII code to a char and adds this to list
            Tree.letters.append(chr(i))
            i = i + 1
    
    #Checks if word contains anything other than a lower case letter
    def check_word_validity(self,str):
        #Flag for a valid or invalid word
        valid_word = True
        for char in str:
            #If a character in the word is not in the all_letters list, it is not a letter
            if char not in Tree.letters:
                valid_word = False
                break
        return valid_word
    '''

    def insert_word(self, word: str) -> None:
        """Inserts a word into the tree.

        Args:
            word (str): The string to be input.
        """

        # Sets the word to be uniformly all lowercase
        word = word.lower()
        # valid receives a Boolean value indicating whether the word is valid or not
        # valid = self.check_word_validity(word)
        valid = True
        for letter in word:
            valid = letter.isalpha()  # checks if the char is a letter
            if not valid:
                break
        if valid:
            # Insert word
            self._insert(word, self.root)

    def _insert(self, word: str, node: Node) -> None:
        """Insert a node into the tree.

        Args:
            word (str): The word to be inserted.
            node (Node): The current node to be inserted.
        """

        if word[0] not in node.get_children():
            # node.children.update({word[0]:Node(word[0])})
            node.children[word[0]] = Node(word[0])
        #print('node:',node.data,'->' , node.get_children())
        if len(word) > 1:
            return self._insert(word[1:], node.children[word[0]])
        else:
            #print(node.data, '->', node.get_children(), word[0])
            node.children[word[0]].is_word = True
            #print(node.is_word, node.data, '->', node.get_children(), word[0], node.children[word[0]].is_word)

    def find_closest_word(self, word: str) -> str:
        """Returns the closest word.

        Args:
            word (str): The current word.

        Returns:
            str: The word that was closest to the current word.
        """

        node = self.root
        in_db = True
        for letter in word:
            if letter in node.get_children():
                node = node.children[letter]
            else:
                print('not in database')
                in_db = False
                break
        if in_db:
            closest_word = self._return_leftmost(node)
            return word[:-1] + closest_word
        else:
            return None

    def _return_leftmost(self, node: Node) -> chr:
        """Return a word.

        Args:
            node (Node): The current node.

        Returns:
            chr: The data from the next node.
        """

        #found_word = ""
        if not node.is_word:
            # print(node.is_word)
            # print(node.data)
            return node.data + self._return_leftmost(
                node.children[node.get_children()[0]])
        else:
            return node.data

    def find_closest_words(self, word: str, num: int) -> list:
        """Find multiple words.

        Args:
            word (str): The current word.
            num (int): The number of words.

        Returns:
            list: A list of close words.
        """

        words = []
        node = self.root
        in_db = True
        for letter in word:
            if letter in node.get_children():
                node = node.children[letter]
            else:
                print('not in database')
                in_db = False
                break
        stack = Stack()
        if in_db:
            ignore = False
            if node.is_word:
                ignore = True
            self._return_leftmost2(node, stack, words, num, ignore)
            words = [word[:-1]+"".join(map(str, x)) for x in words]
            return words
        else:
            return None

    def _return_leftmost2(self, node: Node, stack: Stack, words: list, num: int, ignore=False) -> None:
        """Another way to return words.

        Args:
            node (Node): The current node.
            stack (Stack): The stack of current letters.
            words (list): The current words.
            num (int): Amount of words.
            ignore (bool, optional): To ignore a certain word. Defaults to False.
        """
        
        stack.push(node.data)
        #print(node.data)
        if not node.is_word or ignore:
            counter = 0
            while not len(words) == num and counter < len(node.get_children()):
                self._return_leftmost2(
                    node.children[node.get_children()[counter]], stack, words, num)
                if stack.peek() is not None:
                    stack.pop()
                counter += 1
        else:
            words.append(stack.get_stack()[:])


            if not len(words) == num:
                if len(node.get_children()) > 0:  # still connections from node
                    stack.pop()
                    self._return_leftmost2(node, stack, words, num, True)


