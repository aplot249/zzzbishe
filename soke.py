import requests

def login(username,password):
    data = {
        "log": username,
        "pwd": password,
        "action": "mobantu_login"
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    res = requests.post("https://www.soke.me/wp-content/themes/modown/action/login.php",data=data, headers=headers)
    if str(res.text) == '1':
        print(str(username) + "---" + str(password) + "，登录成功")
    else:
        print(str(username) + "---" + str(password) + "，登录失败")


def register():
    session = requests.session()
    session.get("https://www.soke.me/")
    response_img = session.get("https://www.soke.me/wp-content/themes/modown/action/captcha2.php?0.15834161888973552")
    img = response_img.content
    with open('./img.png', 'wb') as f:
        f.write(img)
    captcha = input("输入验证码：")
    data = {
        "user_register": "Beverly Silver",
        "user_email": "3232584441@qq.com",
        "password": "qwert123",
        "captcha": captcha,
        "action": "mobantu_register"
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    res = session.post("https://www.soke.me/wp-content/themes/modown/action/login.php",data=data,headers=headers)
    print(res.text)

if __name__ == "__main__":
    login("3232584441@qq.com","qazws123")
    # register()