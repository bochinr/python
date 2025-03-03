from tkinter import *

win = Tk()  # 创建窗口
win.title("显示信息")

# 在窗口上添加标签和输入框
Label(win, text="作品：").grid(row=0)
Label(win, text="作者：").grid(row=1)
e1 = Entry(win, width=20)
e2 = Entry(win)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)


# 显示信息函数
def show():
    print("作品：《%s》" % e1.get())
    print("作者：%s" % e2.get())
    e1.delete(0, END) # 删除输入框中的信息
    e2.delete(0, END) # 删除输入框中的信息


# 添加按钮
Button(win, text="获取信息", width=10, command=show).grid(row=3, column=0, sticky=W, padx=10, pady=5)
Button(win, text="退出", width=10, command=win.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)

mainloop()
