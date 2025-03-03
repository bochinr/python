from tkinter import *

win = Tk()
win.title("绝对布局")  # #窗口标题
win.geometry("300x250")  # #窗口位置500后面是字母x
'''
place布局，也称绝对布局
'''
label1 = Label(win, text="桃花岛", bg="pink")
label2 = Label(win, text="华山之巅", bg="yellow")
label3 = Label(win, text="牛家村", bg="red")
label4 = Label(win, text="烟雨楼", bg="green")

label1.place(x=10, y=10)  # #固定坐标，按绝对布局显示，窗口大小的变化对布局没有影响
label2.place(x=50, y=50)
label3.place(x=100, y=100)
label4.place(x=150, y=150)

win.mainloop()