import datetime

import jwt


def method_name():
    global key
    headers = {
        'typ': "jwt",
        'alg': "HS256"
    }
    key = 'dsadasdasdasdsadasdsadas'
    play = {
        "username": "admin",
        "password": "<PASSWORD>",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
    }
    res = jwt.encode(payload=play, key=key, algorithm='HS256')
    print(res)
    print(jwt.decode(res, key, algorithms=['HS256']))


# 下面三段都是通过base64进行编码加密
# jwt是由三部分组成headers为头部表明加密类型和加密方式
# payload为加密内容
# key为加密的盐进行加密
# 通过点的方式进行拼接
# method_name()


def jiamia():
    try:
        key = 'dsadasdasdasdsadasdsadas'
        ii='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiI8UEFTU1dPUkQ-IiwiZXhwIjoxNzE1NjUwMzcxfQ.5E_3yyK2dQjbwuWRmTQiG54-jcXsdU-c2ZYUjFJOlJM'
        res=jwt.decode(ii, key, algorithms=['HS256'])
        print(res)
        print("通过")
    except jwt.ExpiredSignatureError:
        print("token 过期")
    except jwt.InvalidTokenError:
        print("无效")
jiamia()
# method_name()