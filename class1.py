"""from tkinter import *

window = Tk()
window.title("Demo window")
window.geometry('400x300')

window.mainloop()"""

from tkinter import *
from datetime import date

root = Tk()
root.title('Getting started with widgets')
root.geometry('400x300')


lbl = Label(text="Hey There!", fg='white', bg ="#072f5f", height= 1, width=300)

name_lbl = Label(text="Full Name", bg ="#3895d3")
name_entry = Entry()

def display():
    name = name_entry.get()
    global Message
    Message = "welcome to teh application! \nToday's date is: "
    greet = "Hello " + name + "\n"

    text_box.insert(END, greet)
    text_box.insert(END, Message)
    text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text="begin", command=display, height=1, bg="#1261a0", fg='white')

lbl.pack()
name_lbl.pack()
name_entry.pack()
text_box.pack()
btn.pack()

root.mainloop()