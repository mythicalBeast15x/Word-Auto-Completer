'''
The main class that will import all other modules
and run the program. Calls the saved data structure
from a saved file to improve speed of the application.
'''

from WordTree import Tree
from SaveData import *


# Gets the tree from the binary file.
# Ensures that the if finds the file in the directory.
try:
    tree = retrieveInformation(
        'Word-Auto-Completer/Word Auto Completer/tempSaveInformation.data')
except FileNotFoundError:
    try:
        tree = retrieveInformation(
            'Word Auto Completer/tempSaveInformation.data')
    except FileNotFoundError:
        try:
            tree = retrieveInformation(
                'tempSaveInformation.data')
        except:
            print("There was an error.")
    except:
        print("There was an error.")
except:
    print("There was en error.")

tree.insert_word('byte')

word_part = input('enter a word: ')
print(tree.find_closest_word(word_part))
print(tree.find_closest_words(word_part, 3))
