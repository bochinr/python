import tkinter as tk
import time  # 使用time模块改变时间


def gettime():
    v.set(time.strftime("%Y-%m-%d %H:%M:%S")) # 获取当前时间
    window.after(1000, gettime) # 每隔1s调用函数gettime自身获取时间


window = tk.Tk()  # 实例化对象，建立窗口window
window.title("唐诗一首")  # 设置窗口标题
window.geometry('400x300')  # 设置窗口大小
window.resizable(False, False)  # 设置窗口的宽高不可以改变

label1 = tk.Label(window, text="山行", justify="center", font=('隶书', 30))
label2 = tk.Label(window, text="唐  杜牧", justify="center", font=('隶书', 20))
label3 = tk.Label(window, text="  远上寒山石径斜，\n  白云深处有人家。\n  停车坐爱枫林晚，\n  霜叶红于二月花。\n", justify="center", font=('隶书', 20))

v = tk.StringVar()
v.set(time.strftime("%Y-%m-%d %H:%M:%S"))
label4 = tk.Label(window, textvariable=v, justify="center", font=('隶书', 10))

label1.pack()  # pack()是按照添加顺序排列组件
label2.pack()
label3.pack()
label4.pack()

gettime()
window.mainloop()  # 显示窗体
