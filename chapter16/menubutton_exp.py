from tkinter import *

top = Tk()
top.title("IT SKILL")
top.geometry('250x150')
mb_lang = Menubutton(top, text ='Language')

mb_lang.menu = Menu(mb_lang)
# 生成菜单项
for item in ['Python', 'PHP', 'CPP', 'C', 'Java', 'JavaScript', 'VBScript']:
    mb_lang.menu.add_command(label = item)
mb_lang['menu'] = mb_lang.menu
mb_lang.pack(side = LEFT)

# 添加向菜单中添加checkbutton项
mb_os = Menubutton(top, text ='OS')
mb_os.menu = Menu(mb_os)
for item in ['Unix', 'Linux', 'Soloris', 'Windows']:
    mb_os.menu.add_checkbutton(label = item)
mb_os['menu'] = mb_os.menu
mb_os.pack(side = LEFT)

# 向菜单中添加radiobutton项
mb_linux = Menubutton(top, text ='Linux')
mb_linux.menu = Menu(mb_linux)
for item in ['Redhat', 'Fedra', 'Suse', 'ubuntu', 'Debian']:
    mb_linux.menu.add_radiobutton(label = item)
mb_linux['menu'] = mb_linux.menu
mb_linux.pack(side = LEFT)

# 对菜单项进行操作
# 向Language菜单中添加一项"Ruby",以分隔符分开
mb_lang.menu.add_separator()
mb_lang.menu.add_command(label ='Ruby')

# 向OS菜单中第二项添加"FreeBSD",以分隔符分开
mb_os.menu.insert_separator(2)
mb_os.menu.insert_checkbutton(3, label ='FreeBSD')
mb_os.menu.insert_separator(4)

# 将Linux中的“Debian”删除
mb_linux.menu.delete(5)

top.mainloop()
