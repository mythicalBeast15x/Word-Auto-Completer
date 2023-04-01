class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.is_word = False
        self.is_root = None

    def get_children(self):
        return sorted(list(self.children.keys()))


    #Creates a list of all lower case letters
    def create_letterLst(self):
        #List to store all lower case letters
        letters = []
        #ASCII code for lower case 'a'
        i = 97
        #122 is ASCII code for lower case 'z'
        while i <= 122:
            #Converts ASCII code to a char and adds this to list
            letters.append(chr(i))
            i = i + 1
        return letters

    #Checks if word contains anything other than a lower case letter
    def check_word_validity(self,str):
        #Stores all letters from the create_letterLst function
        all_letters = self.create_letterLst()
        #Flag for a valid or invalid word
        valid_word = True
        for char in str:
            #If a character in the word is not in the all_letters list, it is not a letter
            if char not in all_letters:
                valid_word = False
                break
        return valid_word


    def insert(self,str):
        #valid receives a Boolean value indicating whether the word is valid or not
        valid = self.check_word_validity(str)
        if valid == True:
            #Insert word
        else:
            pass