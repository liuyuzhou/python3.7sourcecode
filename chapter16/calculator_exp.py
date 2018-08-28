import decimal
import math
from tkinter import Tk, StringVar, Button, Label, Menu, messagebox

top = Tk()
top.title('计算器')
top.resizable(0, 0)
global cun_cu, var_text, result, fu_hao
result, fu_hao = None, None
var_text = StringVar()
cun_cu = []


class AnJianZhi(object):
    global cun_cu, var_text, result, fu_hao
    def __init__(self, an_jian):
        self.an_jian = an_jian

    def jia(self):
        cun_cu.append(self.an_jian)
        var_text.set(''.join(cun_cu))

    def tui(self):
        if cun_cu is not None and cun_cu.__len__() > 0:
            cun_cu.pop()
        var_text.set(''.join(cun_cu))

    def clear(self):
        cun_cu.clear()
        var_text.set('')
        result = None
        fu_hao = None

    def zheng_fu(self):
        if cun_cu is None or cun_cu.__len__() == 0:
            var_text.set(''.join(cun_cu))
            return

        if cun_cu[0]:
            if cun_cu[0] == '-':
                cun_cu[0] = '+'
            elif cun_cu[0] == '+':
                cun_cu[0] = '-'
            else:
                cun_cu.insert(0, '-')
        var_text.set(''.join(cun_cu))

    def xiao_shu_dian(self):
        if cun_cu.count('.') >= 1:
            pass
        else:
            if cun_cu.__len__() == 0:
                cun_cu.append('0')
            cun_cu.append('.')
            var_text.set(''.join(cun_cu))

    def yun_suan(self):
        global cun_cu, var_text, result, fu_hao
        if var_text.get() == '':
            pass
        else:
            get1 = decimal.Decimal(var_text.get())
            if self.an_jian in ('1/x', 'sqrt'):
                if self.an_jian == '1/x':
                    try:
                        result = 1/get1
                    except ZeroDivisionError as ex:
                        result = 0
                        messagebox.showinfo('异常', '被除数等于:{}'.format(get1))
                elif self.an_jian == 'sqrt':
                    result = math.sqrt(get1)
            elif  self.an_jian in ('+', '-', '*', '/', '=', '%'):
                if fu_hao is not None:
                    get1 = decimal.Decimal(result)
                    get2 = decimal.Decimal(var_text.get())
                    if fu_hao == '+':
                        result = get1 + get2
                    elif fu_hao == '-':
                        result = get1 - get2
                    elif fu_hao == '*':
                        result = get1 * get2
                    elif fu_hao == '/':
                        try:
                            result = get1 / get2
                        except ZeroDivisionError:
                            result = 0
                            messagebox.showerror('异常', '被除数等于:{}'.format(get2))
                        except Exception as et:
                            result = 0
                            messagebox.showerror('异常', '异常信息:{}'.format(et))
                    elif fu_hao == '%':
                        result = get1 % get2
                else:
                    result = get1
                if self.an_jian == '=':
                    fu_hao = None
                else:
                    fu_hao = self.an_jian
            print(fu_hao)
            print(result)
            var_text.set(str(result))
            cun_cu.clear()

def bu_ju(top_var):
    global cun_cu, var_text, result, fu_hao
    entry1 = Label(top_var, width=30, height=2, bg='white', anchor='se', textvariable=var_text)
    entry1.grid(row=0, columnspan=5)
    button_mc = Button(top_var, text='MC', width=5)
    button_mr = Button(top_var, text='MR', width=5)
    button_ms = Button(top_var, text='MS', width=5)
    button_m1 = Button(top_var, text='M+', width=5)
    button_m2 = Button(top_var, text='M-', width=5)
    button_mc.grid(row=1,column=0)
    button_mr.grid(row=1,column=1)
    button_ms.grid(row=1,column=2)
    button_m1.grid(row=1,column=3)
    button_m2.grid(row=1,column=4)

    button_j = Button(top_var, text='←', width=5, command=AnJianZhi('c').tui)
    button_ce = Button(top_var, text='CE', width=5)
    button_c = Button(top_var, text=' C ', width=5, command=AnJianZhi('c').clear)
    button12 = Button(top_var, text='±', width=5, command=AnJianZhi('c').zheng_fu)
    button_d = Button(top_var, text='√', width=5, command=AnJianZhi('sqrt').yun_suan)
    button_j.grid(row=2,column=0)
    button_ce.grid(row=2,column=1)
    button_c.grid(row=2,column=2)
    button12.grid(row=2,column=3)
    button_d.grid(row=2,column=4)

    button7 = Button(top_var, text=' 7 ', width=5, command=AnJianZhi('7').jia)
    button8 = Button(top_var, text=' 8 ', width=5, command=AnJianZhi('8').jia)
    button9 = Button(top_var, text=' 9 ', width=5, command=AnJianZhi('9').jia)
    button_c = Button(top_var, text=' / ', width=5, command=AnJianZhi('/').yun_suan)
    button_f = Button(top_var, text=' % ', width=5, command=AnJianZhi('%').yun_suan)
    button7.grid(row=3,column=0)
    button8.grid(row=3,column=1)
    button9.grid(row=3,column=2)
    button_c.grid(row=3,column=3)
    button_f.grid(row=3,column=4)

    button4 = Button(top_var, text=' 4 ', width=5, command=AnJianZhi('4').jia)
    button5 = Button(top_var, text=' 5 ', width=5, command=AnJianZhi('5').jia)
    button6 = Button(top_var, text=' 6 ', width=5, command=AnJianZhi('6').jia)
    button_x = Button(top_var, text=' * ', width=5, command=AnJianZhi('*').yun_suan)
    button_fs = Button(top_var, text='1/x', width=5, command=AnJianZhi('1/x').yun_suan)
    button4.grid(row=4,column=0)
    button5.grid(row=4,column=1)
    button6.grid(row=4,column=2)
    button_x.grid(row=4,column=3)
    button_fs.grid(row=4,column=4)

    button1 = Button(top_var, text=' 1 ', width=5, command=AnJianZhi('1').jia)
    button2 = Button(top_var, text=' 2 ', width=5, command=AnJianZhi('2').jia)
    button3 = Button(top_var, text=' 3 ', width=5, command=AnJianZhi('3').jia)
    button_ = Button(top_var, text=' - ', width=5, command=AnJianZhi('-').yun_suan)
    button_dy = Button(top_var, text=' \n = \n ', width=5, command=AnJianZhi('=').yun_suan)
    button1.grid(row=5, column=0)
    button2.grid(row=5, column=1)
    button3.grid(row=5, column=2)
    button_.grid(row=5, column=3)
    button_dy.grid(row=5, column=4,rowspan=2)

    button0 = Button(top_var, text='   0   ', width=11, command=AnJianZhi('0').jia)
    button_jh = Button(top_var, text=' . ', width=5, command=AnJianZhi('c').xiao_shu_dian)
    button_jia = Button(top_var, text=' + ', width=5, command=AnJianZhi('+').yun_suan)
    button0.grid(row=6,column=0,columnspan=2)
    button_jh.grid(row=6,column=2)
    button_jia.grid(row=6,column=3)


def cai_dan(top_var):
    menu = Menu(top_var)
    sub_menu_1 = Menu(menu,tearoff=0)
    menu.add_cascade(label='查看',menu=sub_menu_1)
    sub_menu_2 = Menu(menu, tearoff=0)
    sub_menu_2.add_command(label='复制')
    sub_menu_2.add_command(label='粘贴')
    menu.add_cascade(label='编辑',menu=sub_menu_2)
    sub_menu = Menu(menu, tearoff=0)
    sub_menu.add_command(label='查看帮助')
    sub_menu.add_separator()
    sub_menu.add_command(label='关于计算机')
    menu.add_cascade(label='帮助',menu=sub_menu)
    top_var.config(menu=menu)


if __name__ == "__main__":
    bu_ju(top)
    cai_dan(top)
    top.mainloop()