from Node import Node

class Tree:
    letters = []

    def __init__(self):
        self.root = Node(None)
        self.root.is_root = True

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

    def insert_word(self, word):
        #Sets the word to be uniformly all lowercase
        word = word.lower()
        #valid receives a Boolean value indicating whether the word is valid or not
        valid = self.check_word_validity(word)
        if valid == True:
            #Insert word
            self._insert(word, self.root)
        else:
            pass


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
