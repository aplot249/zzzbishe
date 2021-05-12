#@author: sareeliu
#@date: 2021/5/9 7:54
import requests

def login(username,password):
    data = {
        "email": username,
        "passwd": password,
        "remember_me": "week"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
    }
    res = requests.post("https://www.baacloud89.com/modules/_login.php",data=data,headers=headers)
    r = res.text
    if "ok" in r:
        print(str(username) + "---" + str(password) + "，登录成功")
    else:
        print(str(username) + "---" + str(password) + "，登录失败")

if __name__ == "__main__":
    login("linbi4887321@163.com","Qqazws123")

