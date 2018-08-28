import tkinter

top = tkinter.Tk()
hello = tkinter.Label(top, text = 'Hello World!')
hello.pack()

quit_tk = tkinter.Button(top, text='QUIT', command=top.quit, bg='red', fg='white')
quit_tk.pack(fill=tkinter.X, expand=1)

tkinter.mainloop()
