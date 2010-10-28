#!/usr/bin/python

def combtop(n, r):
    return reduce(lambda x, y: x * y, range(n, r, -1))

def fact(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

def comb(n,r):
    return combtop(n,r) / fact(r)


print comb(40,20)
