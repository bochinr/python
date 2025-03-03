from tkinter import *

# 创建窗口
win = Tk()
win.title("菜单")
win.geometry("400x300+300+100")
# 创建一个菜单项，类似于导航栏，顶层菜单
menubar = Menu(win)
# 创建菜单项
fmenu1 = Menu(win)
for item in ['新建', '打开', '保存', '另存为', '退出']:
    # 如果该菜单是顶层菜单的一个菜单项，则它添加的是下拉菜单的菜单项。则他添加的是下拉菜单的菜单项。
    fmenu1.add_command(label=item)

fmenu2 = Menu(win)
for item in ['复制', '粘贴', '剪切']:
    fmenu2.add_command(label=item)

fmenu3 = Menu(win)
for item in ['大纲视图', 'web视图', '普通视图']:
    fmenu3.add_command(label=item)

fmenu4 = Menu(win)
for item in ["查看帮助", "关于我们"]:
    fmenu4.add_command(label=item)

# add_cascade 的一个很重要的属性就是 menu 属性，它指明了要把那个菜单级联到该菜单项上，
# 当然，还必不可少的就是 label 属性，用于指定该菜单项的名称
menubar.add_cascade(label="文件", menu=fmenu1)
menubar.add_cascade(label="编辑", menu=fmenu2)
menubar.add_cascade(label="视图", menu=fmenu3)
menubar.add_cascade(label="关于", menu=fmenu4)

# 用窗口的 menu 属性指定使用哪一个作为它的顶层菜单
win.config(menu=menubar)

win.mainloop()
