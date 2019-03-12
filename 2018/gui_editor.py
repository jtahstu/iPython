#!/usr/bin/env python
#-*- coding:utf-8 -*-

# Version: 1.0
# Author: jtahstu
# Software: PyCharm
# Time: 2018-12-13 19:16
# Description: todo list

from tkinter import *
from tkinter.scrolledtext import ScrolledText

def load():
    with open(filename.get()) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.readlines())

def save():
    pass

top = Tk()
top.title('Simple Editor')

contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)

filename = Entry()
filename.pack(side=LEFT, expand=True, fill=X)

Button(text='Open', command=load).pack(side=LEFT)
Button(text='Save', command=save).pack(side=LEFT)

mainloop()