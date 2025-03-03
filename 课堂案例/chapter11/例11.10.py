import tkinter as tk

win = tk.Tk()
win.title('右键菜单示例')

def callback():
    print("~被调用了~")

# 创建一个弹出菜单
menu = tk.Menu(win, tearoff=False)
menu.add_command(label="撤销", command=callback)
menu.add_command(label="重做", command=callback)

frame = tk.Frame(win, width=300, height=200)
frame.pack()

# 单击鼠标右键响应事件
def popup(event):
    menu.post(event.x_root, event.y_root)

# 绑定鼠标右键
frame.bind("<Button-3>", popup)

win.mainloop()
