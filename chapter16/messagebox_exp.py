import tkinter
from tkinter import messagebox

top = tkinter.Tk()

def hello():
    messagebox.showinfo("Say Hello", "Hello World")

bt = tkinter.Button(top, text="Say Hello", command=hello)
bt.pack()

top.mainloop()