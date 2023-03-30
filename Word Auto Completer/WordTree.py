from Node import Node

class Tree:

    def __init__(self):
        self.root = Node(None)
        self.root.is_root = True

    def insert_word(self, word):
        self._insert(word, self.root)

    def _insert(self, word, node):

        if word[0] not in node.get_children():
            #node.children.update({word[0]:Node(word[0])})
            node.children[word[0]] = Node(word[0])
        #print('node:',node.data,'->' , node.get_children())
        if len(word) > 1:
            return self._insert(word[1:], node.children[word[0]])
        else:
            #print(node.data, '->', node.get_children(), word[0])
            node.children[word[0]].is_word = True
            #print(node.is_word, node.data, '->', node.get_children(), word[0], node.children[word[0]].is_word)

    def find_closest_word(self, word):
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

    def _return_leftmost(self, node: Node):
        #found_word = ""
        if not node.is_word:
            #print(node.is_word)
            #print(node.data)
            return node.data + self._return_leftmost(
                node.children[node.get_children()[0]])
        else:
            return node.data
