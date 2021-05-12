#@author: sareeliu
#@date: 2021/5/6 19:40
import requests

def login(email,password):
    data = {
        'email': email,
        'password': password
    }
    res = requests.post("https://api.shop.eduwork.cn/api/auth/login",data=data)
    # print(res.json())
    if 'access_token' in res.json().keys():
        print(str(email) + "---" + str(password) + "，登录成功")
    else:
        print(str(email) + "---" + str(password) + "，登录失败")

if __name__ == "__main__":
    login("3232584441@qq.com","547346dfdfhdsf")
    login("3232584441@qq.com","qazws123")