"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://blog.jtahstu.com
@time: 2018/5/7 17:19
"""


def init():
    import itchat

    # 先登录
    itchat.auto_login(hotReload=True)

    # 获取好友列表
    friends = itchat.get_friends(update=True)[0:]

    # 初始化计数器，有男有女，当然，有些人是不填的
    male = female = other = 0

    # 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
    # 1表示男性，2女性
    for i in friends[1:]:
        sex = i["Sex"]
        if sex == 1:
            male += 1
        elif sex == 2:
            female += 1
        else:
            other += 1

    # 总数算上，好计算比例啊～
    total = len(friends[1:])

    # 好了，打印结果
    print(u"男性好友：%.2f%%" % (float(male) / total * 100))
    print(u"女性好友：%.2f%%" % (float(female) / total * 100))
    print(u"其他：%.2f%%" % (float(other) / total * 100))


if __name__ == "__main__":
    init()

# 男性好友：57.14%
# 女性好友：36.26%
# 其他：6.59%