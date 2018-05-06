import itchat
import requests
import json
import time

API_KEY = 'a3a52ca53821762b3fb458b63b6e16da'
TULINURL = "http://www.tuling123.com/openapi/api?key=%s&info=" % API_KEY
tail = "\n\n     —— 来自Jin Tao同学微信专属客户端的自动回复 n(*≧▽≦*)n "


def getHtml(url):
    html = requests.get(url)
    return html.text


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    friend_text = msg['Text']
    print(time.asctime(), "，Get：", friend_text)
    request = TULINURL + friend_text
    response = getHtml(request)
    print(time.asctime(), "，Return：", response)
    dic_json = json.loads(response, encoding='utf-8')
    print(time.asctime(), "，Send：", dic_json['text'])
    return dic_json['text'] + tail


itchat.auto_login(enableCmdQR=2)
itchat.run()

