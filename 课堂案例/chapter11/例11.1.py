import tkinter as tk  # 导入tkinter模块
window = tk.Tk()  # 实例化对象，建立窗口window
window.title("我的窗体")  # 设置窗口标题
window.geometry('600x400')  # 设置窗口大小，这里的乘号是小写字母x
window.maxsize(1200, 800)  # 设置窗口最大化的最大值
window.minsize(400, 200)  #设置窗口最小化的最小值
# window.resizable(False, False)  # 设置窗口的宽高不可以改变
# window.attributes('-toolwindow', 1)  # 设置窗口只有关闭按钮
window.attributes('-alpha', 0.9)  # 设置窗口的透明度，1为不透明，0为完全透明
window.mainloop()  # 显示窗体
