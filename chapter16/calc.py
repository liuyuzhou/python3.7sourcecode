from tkinter import *

# 创建横条型框架
def frame(root, side):
    w = Frame(root)
    w.pack(side = side, expand = YES, fill = BOTH)
    return w


# 创建按钮
def button(root, side, text, command = None):
    w = Button(root, text = text, command = command)
    w.pack(side = side, expand = YES, fill = BOTH)
    return w


# 继承了Frame类，初始化程序界面的布局
class Calculator(Frame):
    def __init__(self):

        Frame.__init__(self)

        self.pack(expand = YES, fill = BOTH)
        self.master.title('Simple Calculater')

        display = StringVar()
        # 添加输入框
        Entry(self, relief = SUNKEN,
              textvariable = display).pack(side = TOP, expand = YES,
                                           fill = BOTH)
        # 添加横条型框架以及里面的按钮
        for key in('123', '456', '789', '-0.'):
            keyF = frame(self, TOP)
            for char in key:
                button(keyF, LEFT, char, lambda w = display, c = char:w.set(w.get() + c))
        # 添加操作符按钮
        opsF = frame(self, TOP)
        for char in '+-*/=':
            if char == '=':
                btn = button(opsF, LEFT, char)
                btn.bind('<ButtonRelease - 1>', lambda e, s = self, w = display:s.calc(w), '+')

            else:
                btn = button(opsF, LEFT, char, lambda w = display, s = '%s' %char:w.set(w.get() + s))
        # 添加清除按钮
        clearF = frame(self, BOTTOM)
        button(clearF, LEFT, 'clear', lambda w = display:w.set(''))

    # 调用eval函数计算表达式的值
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")


# 程序的入口
if __name__ == '__main__':
    print('ok')
    Calculator().mainloop()
