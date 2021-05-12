#@author: sareeliu
#@date: 2021/5/8 11:00
import requests

def login(email,passwd):
    data = {
        "email": email,
        "password": passwd,
        "captcha": ""
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    res = requests.post("https://www.kurun.com/login_pass_email?request_time=1620471526608",data=data,headers=headers)
    if res.json()["msg"] == "登录成功":
        print(str(email) + '---' + str(passwd) + "，登录成功")
    else:
        print(str(email) + '---' + str(passwd) + "，登录失败")

if __name__ == "__main__":
    login("linbi4887321@163.com","qazws123")