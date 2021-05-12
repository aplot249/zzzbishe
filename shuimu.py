#@author: sareeliu
#@date: 2021/5/7 22:31
import requests

def login(username,password):
    session = requests.session()
    data = {
        "password": password,
        "t": "1620427554444",
        "username": username
    }
    headers = {
        "origin": "https://wap.newsmth.net",
        "pragma": "no-cache",
        # "referer": "https://wap.newsmth.net/login",
        # "sec-ch-ua": 'Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        # "sec-ch-ua-mobile": "?0",
        # "sec-fetch-dest": "empty",
        # "sec-fetch-mode": "cors",
        # "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    session.get("https://wap.newsmth.net/wap/authorize/sign-in",headers=headers)
    res = session.post("https://wap.newsmth.net/wap/authorize/sign-in",data=data,headers=headers)
    r = res.json()['message']
    if r == "您输入的用户名或者密码错误,请确认后重新输入":
        print(str(username) + "---" + str(password) + "，登录失败")
    else:
        print(str(username) + "---" + str(password) + "，登录成功")

if __name__ == "__main__":
    login("qazws123","@qq3232584441")