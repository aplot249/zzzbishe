import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
import kift, aiclouds, ewshop, lylinux, soke, zto, yzp, dujiao, shuimu, kurun, wspm, zhihuishu, baacloud89
import threading,re

window = tk.Tk()    # 第1步，实例化object，建立窗口window
window.title('李瑶毕业设计')   # 第2步，给窗口的可视化起名字
window.geometry('400x560')  # # 第3步，设定窗口的大小(长 * 宽)，这里的乘是小x
window.resizable(False, False)  # 设置窗口大小不可改变

l1 = tk.Label(window, bg='white', font=('Arial', 12), width=30, height=5,text='''
老师好！这是李瑶的毕业设计
利用爬虫，判断账号密码
是否在以下网站注册过
输入完用户名和密码
点对应网站按钮开始
''')    #在图形界面上设定标签

# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l1.pack()  # 放置标签，Label内容content区域放置位置，自动调节尺寸，# 放置lable的方法有：1）l.pack(); 2)l.place()

# b = ttk.Separator(window,orient='horizontal')
# b.pack(fill=tk.X)
# s = ttk.Style()
# s.configure('red.TSeparator',background='red')
# b = ttk.Separator(window,orient='horizontal',style='red.TSeparator')
# b.pack(fill=tk.X)

info = tk.Label(window,bg='white',font=('Arial', 12), width=30,)
info.pack()
# 第5步，用户信息
tk.Label(info, text='用户名：', font=('Arial', 14)).grid(row=0, column=0)
tk.Label(info, text='密码：', font=('Arial', 14)).grid(row=1, column=0)
# 第6步，用户登录输入框entry
# 用户名
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(info, textvariable=var_usr_name, font=('Arial', 14))
entry_usr_name.grid(row=0, column=1)
# 用户密码
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(info, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
entry_usr_pwd.grid(row=1, column=1)

# b = ttk.Separator(window,orient='horizontal')
# b.pack(fill=tk.X)

def handle(val):
    account = var_usr_name.get()
    password = var_usr_pwd.get()
    if len(account) == 0 or len(password) == 0:
        # print("用户名或密码不能为空")
        lbl.configure(text="用户名或密码不能为空")
        return False
    for ac in account:
        if '\u4e00' <= ac <= '\u9fa5':
            # print("用户名或密码不能含有中文")
            lbl.configure(text="用户名或密码不能为空")
            return False
    for pa in password:
        if '\u4e00' <= pa <= '\u9fa5':
            # print("用户名或密码不能含有中文")
            lbl.configure(text="用户名或密码不能含有中文")
            return False

    lbl.configure(text="")
    if val == 'aiclouds':
        # print("正在用【用户名：{0}---密码：{1}】,尝试登录网站 https://iaclouds.iaclouds.com/".format(account, password))
        lbl.configure(text="正在尝试登录网站 \nhttps://iaclouds.iaclouds.com/")
        aiclouds.login(account, password)
    elif val == "kurun":
        # print("正在用【用户名：{0}---密码：{1}】,尝试登录网站 https://www.kurun.com/".format(account, password))
        lbl.configure(text="正在尝试登录网站 \nhttps://www.kurun.com/")
        kurun.login(account,password)
    elif val == 'kift':
        # print("正在用【用户名：{0}---密码：{1}】,尝试登录网站 https://file.chuanyun101.com".format(account, password))
        lbl.configure(text="正在尝试登录网站 \nhttps://file.chuanyun101.com")
        kift.login(account,password)
    elif val == 'ewshop':
        # print("正在用【用户名：{0}---密码：{1}】,尝试登录网站 http://ewshop.58email.xyz".format(account, password))
        lbl.configure(text="正在尝试登录网站 \nhttp://ewshop.58email.xyz")
        ewshop.login(account,password)
    elif val == 'kift_logout':
        # print("正在用【用户名：{0}---密码：{1}】,尝试永久注销网站 https://file.chuanyun101.com".format(account, password))
        lbl.configure(text="永久注销网站\nhttps://file.chuanyun101.com")
        kift.logout(account,password)
    elif val == 'lylinux':
        # print("正在用【用户名：{0}---密码：{1}】,尝试登录网站 https://www.lylinux.net/login/".format(account, password))
        lbl.configure(text="正在尝试登录网站 \nhttps://www.lylinux.net/login/")
        lylinux.login(account, password)
    elif val == 'soke':
        # print("正在用【用户名：{0}---密码：{1}】,尝试登录网站 https://www.soke.me/".format(account, password))
        lbl.configure(text="正在尝试登录网站 \nhttps://www.soke.me/")
        soke.login(account, password)
    elif val == 'zto':
        # print("正在用【用户名：{0}---密码：{1}】,尝试登录网站 https://www.zto.com/".format(account, password))
        lbl.configure(text="正在尝试登录网站 \nhttps://www.zto.com/")
        zto.login(account, password)
    elif val == 'yzp':
        # print("正在用【用户名：{0}---密码：{1}】,尝试登录网站 https://www.yzp.cn/".format(account, password))
        lbl.configure(text="正在尝试登录网站 \nhttps://www.yzp.cn/")
        yzp.login(account, password)
    elif val == "dujiao":
        # print("正在用【用户名：{0}---密码：{1}】,尝试登录网站 https://dujiao.net/".format(account, password))
        lbl.configure(text="正在尝试登录网站 \nhttps://dujiao.net/")
        dujiao.login(account,password)
    elif val == "shuimu":
        # print("正在用【用户名：{0}---密码：{1}】,尝试登录网站 https://wap.newsmth.net/index".format(account, password))
        lbl.configure(text="正在尝试登录网站 \nhttps://wap.newsmth.net/index")
        shuimu.login(account,password)
    elif val == "wspm":
        # print("正在用【用户名：{0}---密码：{1}】,尝试登录网站 http://www.woshipm.com/".format(account, password))
        lbl.configure(text="正在尝试登录网站 \nhttp://www.woshipm.com/")
        wspm.login(account,password)
    elif val == "zhihuishu":
        # print("正在用【用户名：{0}---密码：{1}】,尝试登录网站 https://passport.zhihuishu.com/login".format(account, password))
        lbl.configure(text="正在尝试登录网站 \nhttps://passport.zhihuishu.com/login")
        zhihuishu.login(account,password)
    elif val == "baacloud89":
        # print("正在用【用户名：{0}---密码：{1}】,尝试登录网站 https://www.baacloud89.com/modules/login.php".format(account, password))
        lbl.configure(text="正在尝试登录网站 \nhttps://www.baacloud89.com/modules/login.php")
        baacloud89.login(account,password)
    var_usr_name.set('')
    var_usr_pwd.set('')

#开启多线程
def handle_thread(val):
    t = threading.Thread(target=handle,args=(val,))
    t.start()

b = ttk.Separator(window,orient='horizontal',style='red.TSeparator')
b.pack(fill=tk.X)
lbl = tk.Label(window, font=("Arial Bold", 10),bg='#fff',height=2,width=36,fg = 'red')
lbl.pack()


#放置按钮的容器
l3 = tk.Label(window)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l3.pack()

# 第5步，在窗口界面设置放置Button按键
tk.Button(l3, text='Kift文件管理', font=('Arial', 12), width=10, height=1, command=lambda: handle_thread('kift')).grid(row=0, column=0)
tk.Button(l3, text='Kift永久注销', font=('Arial', 12), width=10, height=1, command=lambda: handle_thread('kift_logout')).grid(row=0, column=1)
tk.Button(l3, text='ewshop商城', font=('Arial', 12), width=10, height=1, command=lambda: handle_thread('ewshop')).grid(row=1, column=0)
tk.Button(l3, text='lylinux博客', font=('Arial', 12), width=10, height=1, command=lambda: handle_thread('lylinux')).grid(row=1, column=1)
tk.Button(l3, text='aiclouds云', font=('Arial', 12), width=10, height=1, command=lambda: handle_thread('aiclouds')).grid(row=2, column=0)
tk.Button(l3, text='kurun云', font=('Arial', 12), width=10, height=1, command=lambda: handle_thread('aiclouds')).grid(row=2, column=1)
tk.Button(l3, text='搜课网', font=('Arial', 12), width=10, height=1, command=lambda: handle_thread('soke')).grid(row=3, column=0)
tk.Button(l3, text='中通快递', font=('Arial', 12), width=10, height=1, command=lambda: handle_thread('zto')).grid(row=3, column=1)
tk.Button(l3, text='医直聘', font=('Arial', 12), width=10, height=1, command=lambda: handle_thread('yzp')).grid(row=4, column=0)
tk.Button(l3, text='独角招聘', font=('Arial', 12), width=10, height=1, command=lambda: handle_thread('dujiao')).grid(row=4, column=1)
tk.Button(l3, text='水木社区', font=('Arial', 12), width=10, height=1, command=lambda: handle_thread('shuimu')).grid(row=5, column=0)
tk.Button(l3, text='产品人网', font=('Arial', 12), width=10, height=1, command=lambda: handle_thread('wspm')).grid(row=5, column=1)
tk.Button(l3, text='智慧树网课', font=('Arial', 12), width=10, height=1, command=lambda: handle_thread('zhihuishu')).grid(row=6, column=0)
tk.Button(l3, text='baacloud', font=('Arial', 12), width=10, height=1, command=lambda: handle_thread('baacloud89')).grid(row=6, column=1)

# 第6步，主窗口循环显示
window.mainloop()