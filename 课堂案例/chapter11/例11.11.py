from tkinter import *

win = Tk()
win.title("相对布局")  # #窗口标题
win.geometry("300x250")
'''
pack布局,也叫相对布局，窗体改变对空间有影响
'''
label1 = Label(win, text="桃花岛", bg="pink")
label2 = Label(win, text="华山之巅", bg="yellow")
label3 = Label(win, text="牛家村", bg="red")
label1.pack(fill=Y, side=LEFT)  # 填充左侧y方向
label2.pack(fill=X, side=TOP)  # 填充顶部x方向
label3.pack(anchor='ne')   # 以ne方式对齐

win.mainloop()