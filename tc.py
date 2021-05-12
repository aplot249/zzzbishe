#@author: sareeliu
#@date: 2021/5/12 16:18
import requests

res = requests.post(
    url="http://stms.crssg.com:88/seeyon/main.do?method=login",
    data={
        "authorization":"",
        "login.timezone": "GMT+0:00",
        "province": "",
        "city": "",
        "rectangle":"",
        "login_username": "513721198104147752",
        "trustdo_type":"",
        "login_password": "U2FsdGVkX1+eGjQZp+5Q3hWQmT6O1qgV",
        "login_validatePwdStrength": "1",
        "random":"",
        "fontSize": "12",
        "screenWidth": "1536",
        "screenHeight": "864"
    }
)

print(res.request.headers)
