#!/usr/bin/python

def ispalin(num):
    s = (str(num))
    return s == s[::-1]

def palingen():
    b = 999
    while b > 100:
        a = 999
        while a > 100:
            p = a * b
            if ispalin(p):
                yield p
            a -= 1
        b -= 1

pg = palingen()
maxval = 0
while 1:
    try :
        next = pg.next()
        if next > maxval:
            maxval = next
    except StopIteration:
        break

print maxval
