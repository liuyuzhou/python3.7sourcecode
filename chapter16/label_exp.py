from tkinter import Tk, StringVar, Label

top = Tk()
var = StringVar()  # 定义字符串变量
font=("黑体", 20, "bold") # 文本的字体
'''
定义一个Label控件，文本内容可变，背景为black，文本为white，
黑体20，高6，宽30
'''
label = Label(top, textvariable=var, bg='black', fg='white',
              font=font, height=6, width=30)
var.set("Hello,world!")

label.pack()
top.mainloop()