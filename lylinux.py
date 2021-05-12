#@author: sareeliu
#@date: 2021/5/7 13:14
import requests,re

def login(username,password):
    session = requests.session()
    html = session.get("https://www.lylinux.net/login/")
    token = re.search('<input type="hidden" name="csrfmiddlewaretoken" value="(.*?)">',html.text,re.I).group(1)
    data = {
        'csrfmiddlewaretoken':token,
        'username': username,
        'password': password,
        'next': '/'
    }
    res = session.post("https://www.lylinux.net/login/",data=data)
    # print(res.text)
    if "请输入一个正确的 用户名 和密码. 注意他们都是大区分大小写的" in res.text:
        print(str(username) + "---" + str(password) + "，登录失败")
    else:
        print(str(username) + "---" + str(password) + "，登录成功")

if __name__ == '__main__':
    login('qq1788lover','qazws123')
