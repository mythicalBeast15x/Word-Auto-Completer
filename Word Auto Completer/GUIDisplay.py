'''
This is the GUI that the user will use when
using the application. Provides functionality
to the tree class by properly displaying the
word data and suggesting what the user can
type from what was input. 
'''

import tkinter as tk
from SaveData import tree


# gui = GUI() # instantiate GUI object
# gui.display() # displays the GUI

class Text_box(tk.Text): # inherits from tkinter's Text class
    """Class for the textbox where the user will type

    Attributes:
        num_words: int
        word_index: int
    """

    def __init__(self, master=None, **kwargs):
        """The constructor that inherit from the super class.

        Args:
            master (_type_, optional): The class it will inherit from.
            num_words (int): Number of words to display.
            word_index (int): Spot the word is at.
        """

        super().__init__(master, **kwargs)
        self.num_words = 5
        self.word_index = 0

    def find_auto_complete_part(self, s1:str, s2:str) -> str:
        """Returns part of the word that would be auto completed

        Args:
            s1 (str): The current word.
            s2 (str): The word to replace it.

        Returns:
            str: Auto completed part of word.
        """

        try:
            return s2.replace(s1, "")
        except Exception:
            return ""
    
    def recommend_word(self, typed:str, event:tk.Event) -> None:
        """Displays part of the word which will be recommended.

        Args:
            typed (str): What has been typed.
            event (tk.Event): The event handler that is called.
        """

        cursor_index = self.index(tk.INSERT) # get the cursor's index
        closest_word = self.toggle_recommendation(typed, event) # get the closest word to what the user typed
        faded_part = self.find_auto_complete_part(typed, closest_word) # recommended portion will be faded

        self.delete(cursor_index, "end") # clear any previous recommendations

        self.insert(tk.INSERT, faded_part) # insert the faded part after the cursor
        self.mark_set(tk.INSERT, cursor_index)

        self.tag_add(faded_part, cursor_index, "end") # create tag for the faded part
        self.tag_config(faded_part, foreground="gray") # give a gray color

    def complete_word(self, event:tk.Event) -> None:
        """Function to complete the word when user hits enter key.

        Args:
            event (tk.Event): The event that is called to fill in the word.
        """

        word = self.get(tk.INSERT, "end") # retrieve the word from the text box
        self.delete(tk.INSERT, "end") # clear the text box
        self.insert(tk.INSERT, word) # insert the word back with default font color
        self.mark_set(tk.INSERT, "end-2c")

    def get_typed(self) -> str:
        """Return the text that was typed by the user.

        Returns:
            str: The text the user typed.
        """

        space_index = self.search(" ", "end", backwards=True)

        if space_index != "":
            return self.get(space_index+"+1c", tk.INSERT)
        else:
            return self.get("1.0", tk.INSERT)
        
    def auto_completer(self, event:tk.Event, window:tk.Tk):
        """Main auto completer function.

        Args:
            event (tk.Event): The event to happen.
            window (tk.Tk): The window to be updated.
        """

        typed = self.get_typed()

        if typed == "": # if nothing was typed
            self.delete(tk.INSERT, "end") # clear any recommendations
        else:        
            if self.valid_input(typed):
                self.recommend_word(typed, event)
                window.bind("<Return>", lambda event: self.complete_word(event))

    def valid_input(self, typed:str) -> bool:
        """Validates what the user typed.

        Args:
            typed (str): The user input.

        Returns:
            bool: Returns a value depending if there was a word found.
        """

        for char in typed:
            if not char.isalpha(): # check if the character is an alphabet
                self.delete(tk.INSERT, "end") # clear any recommendations
                print("Invalid input")
                return False
        return True

    def toggle_recommendation(self, typed:str, event:tk.Event) -> str:
        """Return other recommended words.

        Args:   
            typed (str): The current typed word.
            event (tk.Event): The event to call other words.

        Returns:
            str: Returns more words.
        """

        recommended_words = tree.find_closest_words(typed, self.num_words)
        if recommended_words is not None:
            if len(recommended_words) > 0:
                if event.keysym == "Up":
                    self.word_index += 1

                if self.word_index >= len(recommended_words):
                    self.word_index = 0

                return recommended_words[self.word_index]
            else:
                return None

    def clear(self):
        """Clears the text box.
        """

        self.delete("1.0", "end")

class GUI():
    """Main GUI class encapsulates the window, buttons and textbox.

    Attributes:
        window: Tk
        frm: Frame
        text_box: Text_box
        clear_btn: Button
    """

    def __init__(self) -> None:
        """This is the constructor for the GUI to build.
        """
        
        self.window = tk.Tk() # create window
        self.frm = tk.Frame(self.window) # create frame
        # create textbox
        self.text_box = Text_box(self.frm, height=1, font=('Arial', 14), wrap='word', fg="white", insertbackground="white", bg="black")
        # Instantiates button object
        self.clear_btn = tk.Button(self.frm, height=1, width=3, text="Clear", fg="white", bg="black",command=self.text_box.clear)

    def display(self):
        """Display the GUI.
        """

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
