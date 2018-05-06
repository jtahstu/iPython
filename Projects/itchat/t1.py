# coding=utf8
import itchat
import json
import time

itchat.auto_login(True)


# 注意实验楼环境的中文输入切换
# itchat.send(u'测试消息发送', 'filehelper')


# friends = itchat.get_friends(update=True)[0:]


# print(json.dumps(friends))
# print(json.dumps(chat_rooms))

# for i in range(5):
#     text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ': 测试消息发送'
#     itchat.send(text, '@@ea93433e75cb98eb412cc6e9c498e9dfda5ca10853657355d4f421de15d047ac')
#     time.sleep(2)
def getUserName():
    chat_rooms = itchat.get_chatrooms(update=True)[0:5]
    user_name = ''
    for item in chat_rooms:
        if item['NickName'] == '财务自由小组' or item['NickName'].find('2018-05') >= 0:
            user_name = item['UserName']
    return user_name


old_name = '财务自由小组'
for i in range(10):
    name = 'now is ' + time.strftime("%Y-%m-%d %H:%M", time.localtime())
    itchat.set_chatroom_name(chatroomUserName=getUserName(), name=name)
    time.sleep(60)

itchat.set_chatroom_name(chatroomUserName=getUserName(), name=old_name)
