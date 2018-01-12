"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@time: 2018/1/9 15:18
"""
# 1
guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')
# 2
start = 1
while (True):
    if start < guess_me:
        print('too low')
        start += 1
    else:
        if start == guess_me:
            print('found it!')
        elif start > guess_me:
            print('oops')
        break
# 3
for i in [3, 2, 1, 0]:
    print(i)
# 4
odd = [i for i in range(10) if i % 2 == 0]
print(odd)
# 5
squares = {x: x ** 2 for x in range(10)}
print(squares)
# 6
odd = {j for j in range(10) if j % 2 == 1}
print(odd)


# 7
def my_range():
    yield 'Got'
    for k in range(10):
        yield k


myrange = my_range()
for i in myrange:
    print(i, end=' ')
print()


# 8
def good():
    return ['Harry', 'Ron', 'Hermione']


# 9
def get_odds():
    for l in range(10):
        if l & 1:
            yield l


j = 0
for i in get_odds():
    j += 1
    if j == 3:
        print(i)


# 10
def document_it(func):
    def new_func(*args, **kwargs):
        print('start')
        res = func(*args, **kwargs)
        print(res)
        print('end')
        return res

    return new_func


new_good = document_it(good)  # good 是第8步创建的函数
new_good()


# 11
class OopsException(Exception):
    pass


try:
    raise OopsException('Caught an oops')
except OopsException as e:
    print(e)

# 12
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
for title, plot in zip(titles, plots):
    print(title, plot)
