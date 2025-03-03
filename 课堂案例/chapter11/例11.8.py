import tkinter as tk

win = tk.Tk()
win.geometry('600x400')
win.title('Frame框架布局')

label_0 = tk.Label(win, text='社会主义核心价值观', font=('隶书', 25))
label_0.place(relx=0.25, rely=0.05)
# 定义第一个容器
frame_left = tk.Frame(win, bg="green")
frame_left.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.4)

label_1 = tk.Label(frame_left, text="富强")
label_1.place(relx=0.2, rely=0.2)

label_2 = tk.Label(frame_left, text="民主")
label_2.place(relx=0.6, rely=0.2)

label_3 = tk.Label(frame_left, text="文明")
label_3.place(relx=0.2, rely=0.6)

label_4 = tk.Label(frame_left, text="和谐")
label_4.place(relx=0.6, rely=0.6)

# 定义第二个容器
frame_right = tk.Frame(win, bg="yellow")
frame_right.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.4)
label_1 = tk.Label(frame_right, text="自由")
label_1.place(relx=0.2, rely=0.2)

label_2 = tk.Label(frame_right, text="平等")
label_2.place(relx=0.6, rely=0.2)

label_3 = tk.Label(frame_right, text="公正")
label_3.place(relx=0.2, rely=0.6)

label_4 = tk.Label(frame_right, text="法治")
label_4.place(relx=0.6, rely=0.6)

# 定义第三个容器
frame_bottom = tk.Frame(win, bg="pink")
frame_bottom.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.2)

label_5 = tk.Label(frame_bottom, text="发\n表\n评\n论", background='pink')
label_5.place(relx=0.01, rely=0.04)

txt1 = tk.Text(frame_bottom, height=5, width=60)
txt1.place(relx=0.05, rely=0.06)

bt = tk.Button(frame_bottom, text='发\n送')
bt.place(relx=0.94, rely=0.2)

win.mainloop()
