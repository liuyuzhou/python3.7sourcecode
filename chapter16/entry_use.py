#示例
from tkinter import *

top = Tk()

text = Entry(top, background = 'red', borderwidth = 3, font = ('Helvetica', '14', 'bold'))
text.pack()
text.insert(0, '内容一')
text.get()

text.pack()

mainloop()

import tkinter

top = tkinter.Tk()