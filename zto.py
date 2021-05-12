import requests

def login(account, password):
    data = {
        "isAgainBind": "false",
        "password": password,
        "userName": account
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    res = requests.post("https://hdgateway.zto.com/auth_account_loginByPassword",data=data,headers=headers)
    if res.json()['message'] == '账号或密码错误':
        print(str(account) + "---" + str(password) + "，登录失败")
    else:
        print(str(account) + "---" + str(password) + "，登录成功")

# if __name__ == "__main__":
#     login(account, password)