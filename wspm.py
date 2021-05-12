import requests

def login(account,password):
    data = {
        "FS": "PM",
        "REDIRECT": "http://www.woshipm.com/",
        "account": account,
        "pwd": password
    }
    res = requests.post("http://passport.woshipm.com/user/loginByTop.html?_protocol=http",data=data)
    r = res.json()["MESSAGE"]
    print(r)
    if r == "操作成功":
        print(str(account) + "---" + str(password) + "，登录成功")
    else:
        print(str(account) + "---" + str(password) + "，登录失败")

if __name__ == "__main__":
    login("18411632869","qqwoshi")
