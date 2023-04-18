'''
This is the GUI that the user will use when
using the application. Provides functionality
to the tree class by properly displaying the
word data and suggesting what the user can
type from what was input. 
'''

import tkinter as tk
from WordCompleter import tree

# class for the textbox where the user will type
class Text_box(tk.Text): # inherits from tkinter's Text class
    def __init_subclass__(cls) -> None: # constructor inherits from super class
        return super().__init_subclass__()
    
    def find_auto_complete_part(self, s1:str, s2:str): # returns part of the word that would be auto completed
        try:
            #print('replaced:',s2.replace(s1, ""))
            return s2.replace(s1, "")
        except Exception:
            return " - No suggestions"
    
    def recommend_word(self, typed:str): # displays part of the word which will be recommended
        cursor_index = self.index(tk.INSERT) # get the cursor's index
        closest_word = tree.find_closest_word(typed) # get the closest word to what the user typed
        faded_part = self.find_auto_complete_part(typed, closest_word) # recommended portion will be faded

        self.delete(cursor_index, "end") # clear any previous recommendations

        self.insert(tk.INSERT, faded_part) # insert the faded part after the cursor
        self.mark_set(tk.INSERT, cursor_index)

        self.tag_add(faded_part, cursor_index, "end") # create tag for the faded part
        self.tag_config(faded_part, foreground="gray") # give a gray color

    def complete_word(self, event:tk.Event): # function to complete the word when user hits enter key
        word = self.get(tk.INSERT, "end") # retrieve the word from the text box
        self.delete(tk.INSERT, "end") # clear the text box
        self.insert(tk.INSERT, word) # insert the word back with default font color
        self.mark_set(tk.INSERT, "end-2c")

    def get_typed(self) -> str: # return the text that was typed by the user
        space_index = self.search(" ", "end", backwards=True)

        if space_index != "":
            return self.get(space_index+"+1c", tk.INSERT)
        else:
            return self.get("1.0", tk.INSERT)
        
    def auto_completer(self, event:tk.Event, window:tk.Tk): # main auto completer function
        typed = self.get_typed()

        if typed == "": # if nothing was typed
            self.delete(tk.INSERT, "end") # clear any recommendations
        else:        
            if self.valid_input(typed):
                self.recommend_word(typed)
                window.bind("<Return>", lambda event: self.complete_word(event))

    def valid_input(self, typed:str) -> bool: # validates what the user typed
        for char in typed:
            if not char.isalpha(): # check if the character is an alphabet
                self.delete(tk.INSERT, "end") # clear any recommendations
                print("Invalid input")
                return False
        return True

    def toggle_recommendation(self): # return other recommended words
        pass

    def clear(self): # clear the textbox
        self.delete("1.0", "end")

class GUI(): # main GUI class encapsulates the window, buttons, textbox
    def __init__(self) -> None:
        self.window = tk.Tk() # create window
        self.frm = tk.Frame(self.window) # create frame
        # create textbox
        self.text_box = Text_box(self.frm, height=1, font=('Arial', 14), wrap='word', fg="white", insertbackground="white", bg="black")
        
        # Instantiates button object
        self.clear_btn = tk.Button(self.frm, height=1, width=3, text="Clear", fg="white", bg="black",command=self.text_box.clear)

    def display(self): # display the GUI
        self.window.title("Word Completer") # add window title
        self.window.geometry("300x60") # customize window size/dimensions
        # Changes window background to black
        self.window.configure(bg="black")

        # Adds frame to window
        self.frm.pack()

        self.text_box.pack(fill='both', expand=True) # add Text widget to the frame
        self.clear_btn.pack(fill='both') # Add Button widget to frame

        # auto completion will execute whenever the user starts typing
        self.window.bind("<Key>", lambda event: self.text_box.auto_completer(event, self.window))

        self.window.mainloop()

gui = GUI() # instantiate GUI object
gui.display() # displays the GUI