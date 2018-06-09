"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@time: 2018/1/10 13:17
"""
# 1
mystery = '\U0001f4a9'
print(mystery)
import unicodedata

print(unicodedata.name(mystery))
# 2
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)
# 3
pop_string = pop_bytes.decode('utf-8')
print(pop_string)
# 4
print("My kitty cat likes %s,My kitty cat likes %s,My kitty cat fell on his %sAnd now thinks he's a %s." % (
    'roast beef', 'ham', 'head', 'clam'))
# 5 这里大括号要加 0[]，不然格式化输出报错
letter = """
Dear {0[salutation]} {0[name]},
Thank you for your letter. We are sorry that our {0[product]} {0[verbed]} in your
{0[room]}. Please note that it should never be used in a {0[room]}, especially
near any {0[animals]}.
Send us your receipt and {0[amount]} for shipping and handling. We will send
you another {0[product]} that, in our tests, is {0[percent]}% less likely to
have {0[verbed]}.
Thank you for your support.
Sincerely,
{0[spokesman]}
{0[job_title]}
"""
# 6
response = {
    'salutation': 'A',
    'name': 'B',
    'product': 'C',
    'verbed': 'D',
    'room': 'E',
    'animals': 'F',
    'amount': 'G',
    'percent': 'H',
    'spokesman': 'I',
    'job_title': 'J'
}
print(letter.format(response))
# 7
mammoth = """
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.

All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.

Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.

May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.

Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.

We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon. cwr3 aiu 3xxr
"""
# 8 以 c 开头的单词
import re

cs = re.findall(r'\bc.*?\b', mammoth)
print(cs)
# 9 找到所有以 c 开头的4个字母的单词
cw = re.findall(r'\bc[a-zA-Z]{3}\b', mammoth)
print(cw)
# 10 找到所有以 r 结尾的单词
r = re.findall(r'\b[a-zA-Z]*?r\b', mammoth)
print(r)
# 11 找到所有包含且仅包含 3 个元音的单词
y = re.findall(r'\b[aoeiu]{3}\b', mammoth)
print(y)
# 12
import binascii

gif = binascii.unhexlify(b'47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b')
gif = bytes(gif)  # b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x01D\x00;'
# 13
print(gif[0:6] == b'GIF89a') # True
# 14 这里应该表示6 7和8 9，都为\x01\x00，因为是大端方案存储
print(gif[6:10])  # b'\x01\x00\x01\x00'
