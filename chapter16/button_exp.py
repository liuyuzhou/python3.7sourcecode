from tkinter import Tk, Button

top = Tk()  # 创建顶层窗口
text='hello world!' # 文本内容为 hello world!
bg='black' # 背景为黑色
fg='white' # 文本字体为白色
font=("黑体", 20, "bold") # 文本的字体
'''
创建一个按钮，高为6，宽为30，文本内容为hello world!，黑色背景，白色黑体字体，
大小20，点击按钮，背景变为红色，字体为绿色，松开按钮后图形界面退出
'''
bt_tk = Button(top, text=text, height=6, width=30, command=top.quit, bg=bg, fg=fg,
               font=font, activebackground='red', activeforeground='green')
bt_tk.pack()   # 将按钮控件放置到主窗口中
top.mainloop()   # 进入消息循环
