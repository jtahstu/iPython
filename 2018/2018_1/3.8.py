"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@time: 2018/1/9 14:39
"""
# 1
years_list = [1980, 1981, 1982, 1983, 1984, 1985]
# 2
print(years_list[3])  # 1983
# 3
print(years_list[-1])  # 1985
# 4
things = ['mozzarella', 'cinderella', 'salmonella']  # 意大利干酪 灰姑娘 沙门氏菌
# 5
things[1] = things[1].capitalize()
print(things)
# 6
things[0] = things[0].upper()
print(things)
# 7
things.remove('salmonella')
print(things)
# 8
surprise = ['Groucho', 'Chico', 'Harpo']
# 9
surprise[-1] = surprise[-1].lower()[::-1].capitalize()
print(surprise[-1])
# 10
e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}
# 11
for (key, value) in e2f.items():
    if key == 'walrus':
        print(value)
# 12
f2e = {}
for (key, value) in e2f.items():
    f2e[value] = key
print(f2e)
# 13
for (key, value) in f2e.items():
    if key == 'chien':
        print(value)
# 14
eng = [k for k in e2f.keys()]
print(eng)
# 15
life = {
    'animals': {
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': {},
        'emus': {}
    },
    'plants': {},
    'others': {}
}
# 16
print(life.keys())
# 17
print(life['animals'].keys())
# 18
print(life['animals']['cats'])
