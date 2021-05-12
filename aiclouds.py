import requests,re

def get_token():
    html = requests.get("https://iaclouds.iaclouds.com/clientarea.php")
    token = re.search('<input type="hidden" name="token" value="(.*?)" />',html.text,re.I).group(1)
    # print(token)

def login(username,password):
    data = {
        'username': username,
        'password': password,
        'token': get_token()
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'
    }
    res = requests.post("https://iaclouds.iaclouds.com/dologin.php",data=data,headers=headers)
    if "账户或密码错误，请重试" in res.text:
        print(str(username) + '---' + str(password) + "，登录失败")

    else:
        print(str(username) + '---' + str(password) + "，登录成功")


if __name__ == '__main__':
    login('3232584441@qq.com','Qq3232584441')
