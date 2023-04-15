'''
This is the GUI that the user will use when
using the application. Provides functionality
to the tree class by properly displaying the
word data and suggesting what the user can
type from what was input. 
'''

from WordCompleter import tree

import tkinter as tk

def find_auto_complete_part(s1:str, s2:str): # returns part of the word that would be auto completed
    try:
        print('replaced:',s2.replace(s1, ""))
        return s2.replace(s1, "")
    except Exception:
        return " - No suggestions"

global window, frm, input_box, clear_btn
window = tk.Tk()
window.title("Word Completer")

window.geometry("300x60")
# Changes window background to black
window.configure(bg="black")

frm = tk.Frame(window)
# Adds frame to window
frm.pack()

input_box = tk.Text(frm, height=1, font=('Arial', 14), wrap='word', fg="white", insertbackground="white", bg="black")

# Function to be called upon button click
def clear():
    input_box.delete("1.0", "end")

# Instantiates button object
clear_btn = tk.Button(frm, height=1, width=3, text="Clear", fg="white", bg="black",command=clear)

def auto_completer(event):
    cursor_index = input_box.index(tk.INSERT) # get index of the cursor
    space_index = input_box.search(" ", "end", backwards=True) # keep track of the space character

    if space_index != "": # if space was typed
        typed = input_box.get(space_index+"+1c", cursor_index) # return the text after the space
    else:
        typed = input_box.get("1.0", cursor_index) # return the text that the user type

    key_code = 0
    try:
        key_code = ord(event.keysym) # find the unicode of the key
    except TypeError:
        pass

    if typed == "": # if nothing was typed
        input_box.delete(tk.INSERT, "end") # clear any recommendations
    
    elif (key_code >= 65 and key_code <= 122) or (event.keysym == "BackSpace" or event.keysym == "space"):
        #print('typed:',typed, 'reccomended:',tree.find_closest_word(typed))
        closest_word = tree.find_closest_words(typed,1)[0] # find closest word
        #closest_word = tree.find_closest_word(typed) # find closest word
        auto_complete_part = find_auto_complete_part(typed, closest_word) # find the auto-completed part 

        input_box.delete(cursor_index, "end") # delete everything after the cursor

        input_box.insert(cursor_index, auto_complete_part) # insert the auto completed text after the cursor
        input_box.mark_set(tk.INSERT, cursor_index)

        input_box.tag_add(auto_complete_part, cursor_index, "end") # create a tag for the autocompleted part
        input_box.tag_config(auto_complete_part, foreground="gray") # gray it out

    elif event.keysym == "Return": # if the user hits the ENTER key
        word = input_box.get(tk.INSERT, "end") # retrieve the word from the text box
        input_box.delete(tk.INSERT, "end") # clear the text box
        input_box.insert(tk.INSERT, word) # insert the word back with default font color
        input_box.mark_set(tk.INSERT, "end-2c")
    else:
        print("press a letter key")

input_box.pack(fill='both', expand=True) # add Text widget to the frame
clear_btn.pack(fill='both') # Add Button widget to frame

window.bind("<Key>", auto_completer) # bind the key_pressed function whenever a key is pressed

window.mainloop()
