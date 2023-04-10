'''
This is the GUI that the user will use when
using the application. Provides functionality
to the tree class by properly displaying the
word data and suggesting what the user can
type from what was input. 
'''

from WordCompleter import tree

import tkinter as tk

def find_auto_complete_part(s1:str, s2:str):
    # return s2.replace(s1, "")
    try:
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
    key_code = 0
    try:
        key_code = ord(event.keysym)
    except TypeError:
        pass
    if key_code >= 65 and key_code <= 122:
        cursor_index = input_box.index(tk.INSERT) # get index of the cursor
        typed = input_box.get("1.0", cursor_index) # return the text that the user type
        closest_word = tree.find_closest_word(typed) # find closest word
        auto_complete_part = find_auto_complete_part(typed, closest_word) # find the auto-completed part 

        input_box.delete(cursor_index, "end") # delete everything after the cursor

        input_box.insert(cursor_index, auto_complete_part) # insert the auto completed text after the cursor
        input_box.mark_set(tk.INSERT, cursor_index)

        input_box.tag_add(auto_complete_part, cursor_index, "end") # create a tag for the autocompleted part
        input_box.tag_config(auto_complete_part, foreground="gray") # gray it out

    else:
        print("press a letter key")


input_box.pack(fill='both', expand=True) # add Text widget to the frame
clear_btn.pack(fill='both') # Add Button widget to frame

window.bind("<Key>", auto_completer) # bind the key_pressed function whenever a key is pressed

window.mainloop()
