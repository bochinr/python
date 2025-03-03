import tkinter as tk  # 使用tkinter前需要先导入

window = tk.Tk()
window.title('登录')
window.geometry('300x200')
window.resizable(False, False)  # 窗口的高度和宽度不可变

L1 = tk.Label(window, text="账  号：")
L2 = tk.Label(window, text="密  码：")

e1 = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
e2 = tk.Entry(window, show='*', font=('Arial', 14))  # 显示成密文形式

L1.place(relx=0.1, rely=0.1)  # 显示位置布局
e1.place(width=150, relx=0.3, rely=0.1)  # 显示位置布局

L2.place(relx=0.1, rely=0.3)  # 显示位置布局
e2.place(width=150, relx=0.3, rely=0.3)  # 显示位置布局

window.mainloop()
