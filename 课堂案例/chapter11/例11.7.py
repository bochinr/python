import tkinter as tk

win = tk.Tk()
win.geometry('450x400+500+100')
win.title('我的画布')

# 创建画布
canvas = tk.Canvas(win)
canvas.pack(fill=tk.BOTH, expand=True)

# 在画布上绘制图片
image_file = tk.PhotoImage(file='image/hua.png')
image = canvas.create_image(0,0, anchor='n', image=image_file)

# 画矩形,填充橙色
x0 = 50  # 距离窗口左上角的横向距离
y0 = 50  # 距离窗口左上角纵向距离
x1 = x0 + 100  # x0到x1之间的距离
y1 = y0 + 100  # y0到y1之间的距离
canvas.create_rectangle(x0, y0, x1, y1, fill='orange')
# 画矩形,填充橙色,设置边框宽度为10
canvas.create_rectangle(x0 + 150, y0, x0 + 250, y0 + 100, fill='orange', width=10)
# 画矩形,填充橙色,设置边框是红色
canvas.create_rectangle(x0 + 300, y0, x0 + 350, y0 + 100, fill='orange', outline='red', width=2)

# 画圆,填充蓝色
canvas.create_oval(50, 250, 150, 350, fill='blue')
# 画椭圆,填充红色,设置边框宽度5，边框颜色pink
canvas.create_oval(200, 250, 350, 350, fill='red', width=5, outline='pink')
win.mainloop()
