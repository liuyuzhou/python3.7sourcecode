from tkinter import *
root = Tk()  
# 创建一个Canvas，设置其背景色为白色  
cv = Canvas(root,bg = 'white')  
# 创建两个同样的rectangle，比较移动前后的不同  
rt1 = cv.create_rectangle(  
    10,10,110,110,  
    tags = ('r1','r2','r3'))  
cv.create_rectangle(  
    10,10,110,110,  
    tags = ('r1','r2','r3'))  
# 移动rt1  
cv.move(rt1,20,-10)  
cv.pack()  
root.mainloop()  