'''
The main class that will import all other modules
and run the program. Calls the saved data structure
from a saved file to improve speed of the application.
'''

import logging
import sys
from WordTree import Tree
from SaveData import *


# Gets the tree from the binary file.
# Ensures that the it finds the file in the directory.
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
                'tempSaveInformationdata')
        except Exception as e:
            logging.log(40, e)
            sys.exit(0)
    except Exception as e:
        logging.log(40, e)
        sys.exit(0)
except Exception as e:
    logging.log(40, e)
    sys.exit(0)

# tree.insert_word('byte')

# word_part = input('enter a word: ')
# print(tree.find_closest_word('br'))
# print(tree.find_closest_words('br', 3))
