"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@time: 2018/1/9 16:19
"""

# 5
plain = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(plain)

# 6
from collections import OrderedDict

fancy = OrderedDict(plain)  # 有序字典，按键排序
print(fancy)

# 7 如果本人没理解错的话，感觉这道题好智障
dict_of_lists = plain
dict_of_lists['a'] = 'something for a'
print(dict_of_lists['a'])


