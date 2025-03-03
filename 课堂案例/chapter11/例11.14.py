from tkinter import messagebox
import tkinter as tk
import pickle

# 创建主窗口
win = tk.Tk()
win.resizable(width=False,height=False) # 窗口大小不可改变
win.title("登陆")
win.geometry("450x300+200+200")

# 设置欢迎画面
canvas = tk.Canvas(win,height=100,width=500)
image_file = tk.PhotoImage(file="image/welcome.gif")
image = canvas.create_image(0,0,anchor="nw",image=image_file)
canvas.pack(side="top")

# 用户名和密码文字显示
tk.Label(win,text="用户名:",font=("宋体", 15)).place(x= 50, y= 150)
tk.Label(win,text="密  码:",font=("宋体", 15)).place(x= 50, y= 200)

# 用户名和密码输入框
var_usr_name = tk.StringVar()
var_usr_name.set("example@python.com")
entry_usr_name=tk.Entry(win, textvariable=var_usr_name,font=("宋体", 15))
entry_usr_name.place(x=160, y=150)

var_usr_pwd = tk.StringVar()
entry_usr_pwd=tk.Entry(win, textvariable=var_usr_pwd,show="*",font=("宋体", 15))
entry_usr_pwd.place(x=160, y=200)

# 登陆按钮功能函数
def usr_login():
    # 获取输入框中的值
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    # 打开文件将信息存储到字典中，如果文件不存在则创建
    try:
        with open("usrs_info.pickle","rb") as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open("usrs_info.pickle","wb") as usr_file:
            usrs_info = {"admin":"admin"}
            pickle.dump(usrs_info, usr_file)

    # 判断用户名和密码是否正确
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title="欢迎光临",message="你好"+usr_name+"!")
        else:
            tk.messagebox.showerror(title="欢迎光临",message="错误提示：您输入的密码有误，请重新输入！")
    else:
        is_sign_up = tk.messagebox.askyesno(title="欢迎光临",message="错误提示:你还没有注册，现在注册吗？")
        if is_sign_up:
            usr_sign_up()

# 注册按钮功能函数
def usr_sign_up():
    # 定义注册按钮功能函数
    def sign_to_File():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        # 密码较验
        with open("usrs_info.pickle","rb") as usr_file:
            exist_usr_info = pickle.load(usr_file)
        if np != npf:
            tk.messagebox.showerror("错误提示","两次输入的密码不一致！")
        elif nn in exist_usr_info:
            tk.messagebox.showerror("错误提示","用户名已经存在")
        else:
            exist_usr_info[nn] =np
            with open("usrs_info.pickle","wb") as usr_file:
                pickle.dump(exist_usr_info,usr_file)
            tk.messagebox.showinfo("欢迎您","您已经注册成功！")
            # 关闭窗口（即摧毁窗口）
            win_sign_up.destroy()

    # 注册窗口
    win_sign_up = tk.Toplevel(win)
    win_sign_up.resizable(width=False, height=False)
    win_sign_up.geometry("350x200+250+250")
    win_sign_up.title("用户注册")
    # 用户名输入框
    new_name = tk.StringVar()
    new_name.set("example@python.com")
    tk.Label(win_sign_up, text="用户名:",font=("宋体", 15)).place(x=30, y=10)
    entry_new_name = tk.Entry(win_sign_up,textvariable=new_name,font=("宋体", 15))
    entry_new_name.place(x=120, y=10)
    # 密码输入框
    new_pwd = tk.StringVar()
    tk.Label(win_sign_up, text="密 码:",font=("宋体", 15)).place(x=30, y=50)
    entry_new_pwd = tk.Entry(win_sign_up,textvariable=new_pwd, show="*",font=("宋体", 15))
    entry_new_pwd.place(x=120, y=50)
    # 确认密码输入框
    new_pwd_confirm = tk.StringVar()
    tk.Label(win_sign_up, text="确认密码:",font=("宋体", 15)).place(x=20, y=90)
    entry_new_pwd_confirm = tk.Entry(win_sign_up,textvariable=new_pwd_confirm, show="*",font=("宋体", 15))
    entry_new_pwd_confirm.place(x=120, y=90)
    # 注册按钮
    btn_confirm_sign_up = tk.Button(win_sign_up,text="注 册",font=("宋体", 15),command=sign_to_File)
    btn_confirm_sign_up.place(x=150,y=140)

# 登陆注册按钮(创建好后定义两个功能函数usr_login、usr_sign_up)
btn_login = tk.Button(win,text="登 陆",font=("宋体", 15),command=usr_login)
btn_login.place(x=130,y=240)
btn_sign_up = tk.Button(win,text="注 册",font=("宋体", 15),command=usr_sign_up)
btn_sign_up.place(x=270,y=240)

win.mainloop()