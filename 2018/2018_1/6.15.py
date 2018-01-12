"""
@author: jtahstu
@contact: root@jtahstu.com
@site: http://www.jtahstu.com
@time: 2018/1/9 17:11
"""

# 1
from pprint import pprint


class Thing:
    pass


print(Thing)
example = Thing()
print(example)


# 2
class Thing2:
    def __init__(self, letters):
        self.letters = letters


l = Thing2('abc')
print(l.letters)


# 3 那肯定要先有个对象啊
class Thing3:
    def __init__(self, letters):
        self.letters = letters


ll = Thing3('xyz')
print(ll.letters)


# 4
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print('dump -> ', self.name, self.symbol, self.number)

    def __str__(self):
        print('__str__ -> ', self.name, self.symbol, self.number)
        return self.name


obj = Element('Hydrogen', 'H', 1)

# 5 用字典来构造一个命名元组
dic = {
    'name': 'Hydrogen',
    'symbol': 'H',
    'number': 1
}
hydrogen = Element(**dic)
print(hydrogen.name, hydrogen.symbol, hydrogen.number)

# 6 方法定义在问题4里
hydrogen.dump()

# 7 方法见问题4，这里打印的是 return 返回的东西
print(hydrogen)


# 8
class Element2:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number


ele2 = Element2('jtahstu', 'J', 96)
print('getter -> ', ele2.name, ele2.symbol, ele2.number)


# 9
class Bear:
    def eats(self):
        return 'berries'


class Rabbit:
    def eats(self):
        return 'clover'


class Octothorpe:
    def eats(self):
        return 'campers'


a = Bear()
b = Rabbit()
c = Octothorpe()
print(a.eats(), b.eats(), c.eats())


# 10
class Laser:
    def does(self):
        return 'disintegrate'


class Claw:
    def does(self):
        return 'crush'


class SmartPhone:
    def does(self):
        return 'ring'


class Robot:
    def __init__(self, laser, claw, smartphonr):
        self.laser = laser
        self.claw = claw
        self.smartphonr = smartphonr

    def does(self):
        print('robot -> ', self.laser.does(), self.claw.does(), self.smartphonr.does())


d = Laser()
e = Claw()
f = SmartPhone()
robot = Robot(d, e, f)
robot.does()
