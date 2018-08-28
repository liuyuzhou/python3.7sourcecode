from tkinter import Tk, Text, INSERT, END

top = Tk()
font=("黑体", 30, "bold") # 文本的字体
'''
定义一个Text控件，高5，宽30，黑体30，背景为white，文本为black
'''
text = Text(top, height=5, width=30, font=font, bg='white', fg='black')
# 插入文本 Hello,world!
text.insert(INSERT, "Hello,world!")
# 尾部插入文本 How are you?
text.insert(END, "How are you?")
text.pack()

# 文本标签，标签名first，start index为0和end index为5，标记值为Hello
text.tag_add("first", "1.0", "1.5")
# 文本标签，标签名second，start index为12和end index为17，标记值为How a
text.tag_add("second", "1.12", "1.17")
# 配置标记属性，对first标记的属性，设置背景色为yellow，文本颜色为blue
text.tag_config("first", background="yellow", foreground="blue")
# 配置标记属性，对second标记的属性，设置背景色为black，文本颜色为green
text.tag_config("second", background="black", foreground="green")
top.mainloop()