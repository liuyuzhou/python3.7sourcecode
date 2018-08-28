from tkinter import *
root = Tk()
v = IntVar()
v.set(1)
for i in range(3):
    Radiobutton(root,  
                    variable = v,
                    indicatoron = 0,
                    text = 'python & tkinter',
                    value = i
                    ).pack()
root.mainloop()