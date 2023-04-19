'''
The main class that will import all other modules
and run the program.
'''

from GUIDisplay import GUI

# Creates the GUI that calls all other needed files
# to allow the program to run. Use SaveData.py 
# to to retrieve the tree data.
gui = GUI()
gui.display()