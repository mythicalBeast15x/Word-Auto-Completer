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
import logging
import sys

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
    'Word-Auto-Completer/Word Auto Completer/tempSaveInformation.data', createTree())

This gets the object from the file.
tree = retrieveInformation(
    'Word-Auto-Completer/Word Auto Completer/tempSaveInformation.data')

If the file retrieveInformation is not working then the directory must be changed.
Use these if that happens.

tree = retrieveInformation(
    'Word Auto Completer/tempSaveInformation.data')

tree = retrieveInformation(
    'tempSaveInformation.data')
'''


# Saves the object as binary to a file.
def saveInformation(inputFile: str, inputObject: Tree) -> None: 
    try:
        with open(inputFile, 'wb') as file:
            # Converts the file to a binary file.
            pickle.dump(inputObject, file)
    except Exception as e:
        logging.log(e)
        sys.exit(0)


# Loads the object from the binary file.
def retrieveInformation(inputFile: str) -> Tree:
    with open(inputFile, 'rb') as file:
        # Returns the object.
        return pickle.load(file)


# Creates the tree and the information.
def createTree(file: str) -> Tree:
    tree = Tree()
    # Open and read the file.
    try:
        file = open('Word-Auto-Completer/Word Auto Completer/' + file, 'r')
    except FileNotFoundError:
        try:
            file = open('Word Auto Completer/' + file, 'r')
        except FileNotFoundError:
            try:
                file = open(file, 'r')
            except Exception as e:
                logging.log(40, e)
                sys.exit(0)
        except Exception as e:
            logging.log(40, e)
            sys.exit(0)
    except Exception as e:
        logging.log(40, e)
        sys.exit(0)
    words = file.readlines()
    # Appends each letter to the tree.
    for word in words:
        tree.insert_word(word.strip())
    return tree


# Gets the tree from the binary file.
# Ensures that the it finds the file in the directory.
try:
    tree = retrieveInformation(
        'Word-Auto-Completer/Word Auto Completer/saveInformation.data')
except FileNotFoundError:
    try:
        tree = retrieveInformation(
            'Word Auto Completer/saveInformation.data')
    except FileNotFoundError:
        try:
            tree = retrieveInformation(
                'saveInformation.data')
        except Exception as e:
            logging.log(40, e)
            sys.exit(0)
    except Exception as e:
        logging.log(40, e)
        sys.exit(0)
except Exception as e:
    logging.log(40, e)
    sys.exit(0)