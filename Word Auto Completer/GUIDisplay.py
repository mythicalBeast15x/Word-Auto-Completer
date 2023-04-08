import tkinter as tk

global window
window = tk.Tk()

window.geometry("300x30")

global input_box
input_box = tk.Text(window, height=3, font=('Arial', 14), wrap='word', fg="white", insertbackground="white", bg="black")

def key_pressed(event):
    key_code = 0
    try:
        key_code = ord(event.keysym)
    except TypeError:
        pass
    if key_code >= 65 and key_code <= 122:
        cursor_index = input_box.index(tk.INSERT) # get index of the cursor
        typed = input_box.get("1.0", cursor_index) # return the text that the user type
        auto_complete = "at" # word autocompleter function 

        input_box.delete(cursor_index, "end") # delete everything after the cursor

        input_box.insert(cursor_index, auto_complete) # insert the auto completed text after the cursor
        input_box.mark_set(tk.INSERT, cursor_index)

        input_box.tag_add(auto_complete, cursor_index, "end") # create a tag for the autocompleted part
        input_box.tag_config(auto_complete, foreground="gray") # gray it out

    else:
        print("press a letter key")


input_box.pack(fill='both', expand=True) # add Text widget to the window

window.bind("<Key>", key_pressed) # bind the key_pressed function whenever a key is pressed

window.mainloop()
