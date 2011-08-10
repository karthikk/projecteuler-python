#!/usr/bin/python
import pprint
def problem22():
    def getNameValue(name):
        return sum(map(lambda (x) : ord(x) - 64, name))

    names = []
    for line in open("names.txt"):
        names = line.split(",")

    for i, name in enumerate(names):
        names[i] = name[1:-1]

    names.sort()

    print sum([(i+1) * getNameValue(name) for i, name in enumerate(names)])

problem22()
