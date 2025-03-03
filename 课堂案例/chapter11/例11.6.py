import tkinter as tk

window = tk.Tk()
window.title('其它控件')
window.geometry('500x350')
var1 = tk.StringVar()  # 创建变量，用var1用来接收鼠标点击具体选项的内容
l1 = tk.Label(window, text="单选框      列表框       复选框", font=('隶书', 20), width=50)
l1.pack()


def print_selection():
    try:
        value = lb.get(lb.curselection())  # 获取当前选中的文本
        var1.set(value)  # 为label设置值
    except:
        pass

def print_selection2():
    value = '单选选项：' + str(var.get())  # 获取当前选中的单选框文本
    var1.set(value)  # 为label设置值

def print_selection3():
    if check1.get() == 1:
        value = '黄蓉'  # 获取当前选中的复选框值
    else:
        value = ' '  # 取消
    var1.set(value)  # 为label设置值

def print_selection4():
    if check2.get() == 1:  # 获取当前选中的复选框值
        value = '华筝'  # 设置值
    else:
        value = ' '
    var1.set(value)  # 为label设置值

# list增加内容三种方法
# 第一种方法，为list关键字listvariable设置值
var2 = tk.StringVar()
var2.set(('红七公', '周伯通', 66, '黄药师'))
# 创建列表框
lb = tk.Listbox(window, listvariable=var2)  # 将var2的值赋给Listbox
# 第二种方法，创建一个list并将值循环添加到Listbox控件中
list_items = ['欧阳峰', '一灯大师', '李莫愁', '梅超风']
for item in list_items:
    lb.insert('end', item)  # 从最后一个位置开始加入值
# 第三种方法，在列表对应索引值位置插入值
lb.insert(1, '王重阳')
lb.insert(2, '段智兴')
# lb.delete(2)  # 删除第二个位置的字符，去掉注释后有效
lb.pack()

# 单选框
var = tk.IntVar()
r1 = tk.Radiobutton(window, text='郭靖', variable=var, value=1, command=print_selection2)
r1.place(relx=0.1, rely=0.15)
r2 = tk.Radiobutton(window, text='杨康', variable=var, value=2, command=print_selection2)
r2.place(relx=0.1, rely=0.25)
r3 = tk.Radiobutton(window, text='欧阳克', variable=var, value=3, command=print_selection2)
r3.place(relx=0.1, rely=0.35)

# 复选框
check1 = tk.IntVar()
check2 = tk.IntVar()
c1 = tk.Checkbutton(window, text="黄蓉", variable=check1, onvalue=1, offvalue=0, height=3, width=20,
                    command=print_selection3)
c2 = tk.Checkbutton(window, text="华筝", variable=check2, onvalue=1, offvalue=0, height=3, width=20,
                    command=print_selection4)
c1.place(relx=0.7, rely=0.15)
c2.place(relx=0.7, rely=0.30)

l = tk.Label(window, bg='pink', fg='blue', font=('Arial', 12), width=50, textvariable=var1)
l.place(relx=0.04, rely=0.68)

b1 = tk.Button(window, text='测试列表框选中状态', width=20, height=1, command=print_selection)
b1.place(relx=0.35, rely=0.8)

window.mainloop()
