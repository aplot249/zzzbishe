#@author: sareeliu
#@date: 2021/5/8 7:49
import requests, rsa, base64


def _str2key(s):
    # 对字符串解码
    b_str = base64.b64decode(s)
    if len(b_str) < 162:
        return False
    hex_str = ''
    # 按位转换成16进制
    for x in b_str:
        h = hex(x)[2:]
        h = h.rjust(2, '0')
        hex_str += h
    # 找到模数和指数的开头结束位置
    m_start = 29 * 2
    e_start = 159 * 2
    m_len = 128 * 2
    e_len = 3 * 2
    modulus = hex_str[m_start:m_start + m_len]
    exponent = hex_str[e_start:e_start + e_len]
    return modulus, exponent


def rsa_encrypt(s, pubkey_str):
    key = _str2key(pubkey_str)
    modulus = int(key[0], 16)
    exponent = int(key[1], 16)
    pubkey = rsa.PublicKey(modulus, exponent)
    return base64.b64encode(rsa.encrypt(s.encode(), pubkey)).decode()


def login(username,password):
    session = requests.Session()
    response1 = session.post("https://file.chuanyun101.com/homeController/getPublicKey.ajax")
    publicKey = response1.json()['publicKey']
    time = response1.json()['time']
    loginInfo = {"accountId": username, "accountPwd": password, "time": time}
    ec_str = rsa_encrypt(str(loginInfo), publicKey)
    response2 = session.post("https://file.chuanyun101.com/homeController/doLogin.ajax", {"encrypted": ec_str})
    # print(response2.text)
    if response2.text == 'permitlogin':
        print(str(username) + "---" + str(password) + "，登录成功")
    else:
        print(str(username) + "---" + str(password) + "，用户名或者密码错误")


def logout(username,password):
    data = {
        "name":username,
        "passwd":password
    }
    res = requests.post("https://deluser.chuanyun101.com/index/",data=data)
    if res.json()['status'] == 'success':
        print(str(username) + "---" + str(password) + "，删除成功")
    else:
        print(str(username) + "---" + str(password) + "，删除失败，用户名或者密码错误")