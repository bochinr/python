import tkinter as tk
import time

win = tk.Tk()
win.title('我的记事本')

txt1 = tk.Text(win, height=10, width=60, relief='groove')
# 插入文本
txt1.insert(tk.END, '乡愁\n')
txt1.insert(tk.INSERT, '作者：余光中\n小时候，\n乡愁是一枚小小的邮票，'
                       '\n我在这头，\n母亲在那头。\n长大后，\n乡愁是'
                       '一张窄窄的船票，\n我在这头，\n新娘在那头。\n'
                       '后来啊，\n乡愁是一方矮矮的坟墓，\n我在外头，'
                       '\n母亲在里头。\n而现在，\n乡愁是一湾浅浅的海峡'
                       '，\n我在这头，\n大陆在那头。')
# 增加滚动条
yscrollbar = tk.Scrollbar(win)
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# 滚动条与text联动
yscrollbar.config(command=txt1.yview)
# text与滚动条联动
txt1.config(yscrollcommand=yscrollbar.set)
txt1.pack()

v = tk.StringVar()
v.set('登录时间：' + time.strftime("%Y-%m-%d %H:%M:%S"))  # 获取当前时间
lable4 = tk.Label(win, textvariable=v, font=('隶书', 10))
lable4.pack()

win.mainloop()
