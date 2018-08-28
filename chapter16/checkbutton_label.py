from tkinter import *

def checkbutton_use():
    tk = Tk()
    # 特殊的int
    special_int = IntVar()
    # 通过这个V可以反映出是否被选中
    check_b = Checkbutton(tk, text="测试", variable=special_int)
    check_b.pack()

    # 要想Label中的文字是可以变的，那么就得写textvariable
    lab = Label(tk, textvariable=special_int)
    lab.pack()

    mainloop()


if __name__ == "__main__":
    checkbutton_use()