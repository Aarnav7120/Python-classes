"""from tkinter import *


window = Tk()
window.title("Event Handler")
window.geometry('400x400')

def handle_keypress(event):
    print(event.char)

window.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nThe button was clicked")

button = Button(text="Click me!")
button.pack()

button.bind("<Button-1>", handle_click) 

window.mainloop()"""




from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x400')

def msg():
    messagebox.showwarning("Alert", "Stop! virus Found.")

button = Button(root, text="Scan for virus", command=msg)
button.place(x=40, y=80)

root.mainloop()