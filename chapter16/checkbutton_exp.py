from tkinter import Tk, Checkbutton, IntVar

top = Tk()
check_music = IntVar()  # 定义整数变量
check_video = IntVar()
'''
创建选择按钮，文本值Music，选中为1，清除选中为0，背景色为white，
高5，宽50，选择框颜色为red
'''
c_m = Checkbutton(top, text="Music", variable=check_music, onvalue=1, offvalue=0,
                  bg='white', height=5, width=50, selectcolor='red')
'''
创建选择按钮，文本值Video，选中为1，清除选中为0，背景色为yellow，
高8，宽25，选择框颜色为blue
'''
c_v = Checkbutton(top, text="Video", variable=check_video, onvalue=1, offvalue=0,
                  bg='yellow', height=8, width=25, selectcolor='blue')
c_m.pack()
c_v.pack()
top.mainloop()