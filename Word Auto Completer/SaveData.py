'''
This class saves the data of the search tree. It is 
important to know that if any classes that made up the
tree are changed, the data and the search tree will
not work properly. Work on the temporary tree when
using the application. The main tree will be for
the final product.
'''

from WordTree import Tree
import pickle

'''
Use this for the main tree.
'Word-Auto-Completer/Word Auto Completer/saveInformation.data'

Use this for the temporary tree.
'Word-Auto-Completer/Word Auto Completer/tempSaveInformation.data'

Here is an example of how to use this class.

This is how to create the tree.
tree = createTree()

This is how to save the tree to a file.
saveInformation(
    'Word-Auto-Completer/Word Auto Completer/tempSaveInformation.data', 'r')

This gets the object from the file.
tree = retrieveInformation(
    'Word-Auto-Completer/Word Auto Completer/tempSaveInformation.data')
'''


# Saves the object as binary to a file.
def saveInformation(inputFile, inputObject):
    with open(inputFile, 'wb') as file:
        # Converts the file to a binary file.
        pickle.dump(inputObject, file)


# Loads the object from the binary file.
def retrieveInformation(inputFile):
    with open(inputFile, 'rb') as file:
        # Returns the object.
        return pickle.load(file)


# Creates the tree and the information.
def createTree():
    tree = Tree()
    # Open and read the file.
    file = open('Word-Auto-Completer/Word Auto Completer/Words.txt', 'r')
    words = file.readlines()
    # Appends each letter to the tree.
    for word in words:
        tree.insert_word(word.strip())
    return tree
