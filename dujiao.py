import requests

def login(username,password):
    data = {
        "email": username,
        "pass": password,
        "signin": "",
    }
    res = requests.post("https://dujiao.net/sign/in", data=data)
    print(res.text)
    if data['email'] in res.text:
        print(str(username) + "---" + str(password) + "，登录成功")
    else:
        print(str(username) + "---" + str(password) + "，登录失败")

if __name__ == "__main__":
    login("3232584441@qq.com","qazws123")