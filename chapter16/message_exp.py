# from tkinter import Tk, StringVar, Message, RAISED
#
# root = Tk()
# var = StringVar()
# label = Message( root, textvariable=var, relief=RAISED )
#
# var.set("Hey!? How are you doing?")
# label.pack()
# root.mainloop()

from tkinter import *
root = Tk()
for i in [LEFT,RIGHT,CENTER]:
    Message(root,text = 'ABC DEF GHI',justify = i).pack()
root.mainloop()