#@author: sareeliu
#@date: 2021/5/7 21:56
import requests

def login(username,password):
    data = {
        "mobile": username,
        "password": password
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    res = requests.post("https://www.yzp.cn/login/doLogin",data=data,headers=headers)
    r = res.json()['msg']
    # print(r)
    if r == "登录成功!":
        print(str(username) + "---" + str(password) + "，登录成功")
    else:
        print(str(username) + "---" + str(password) + "，登录失败")


if __name__ == "__main__":
    login("18411631209","qazws123")