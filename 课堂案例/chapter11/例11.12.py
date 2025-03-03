from tkinter import *

win = Tk()
win.title("表格布局")  # #窗口标题
win.geometry("300x250")
'''
gird布局，也叫表格布局,窗体改变对空间无影响
'''
label1 = Label(win, text="桃花岛", bg="pink")
label2 = Label(win, text="华山之巅", bg="yellow")
label3 = Label(win, text="牛家村", bg="red")
label4 = Label(win, text="烟雨楼", bg="green")
label1.grid(row=0, column=0)  # 将label1放置在第一行第一列
label2.grid(row=0, column=1)  # 将label2放置在第一行第二列
label3.grid(row=1, column=0)  # 将label3放置在第二行第一列
label4.grid(row=1, column=1)  # 将label4放置在第二行第二列

win.mainloop()