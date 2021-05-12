import requests

def login(account,password):
    data = {
        "account": account,
        "password": password
    }
    res = requests.post("https://passport.zhihuishu.com/user/validateAccountAndPassword",data=data)
    r = res.json()['status']
    # print(res.text)
    # print(r)
    if str(r) == "1":
        print(str(account) + "---" + str(password) + "，登录成功")
    else:
        print(str(account) + "---" + str(password) + "，登录失败")

if __name__ == "__main__":
    login("17868810687","qq1010351486")
    # {"pwdErrorCount": 1, "status": -2}