#!/usr/bin/python

def doubletgen(n):
    a = 1
    while a < n:
        yield a, n - a
        a += 1

def tripletgen(n):
    a = 1
    while a < n - 1:
        dg = doubletgen(n-a)
        for doublet in dg:
            yield a, doublet
        a += 1

def square(n):
    return n * n

for i in tripletgen(1000):
    if square(i[0]) == (square(i[1][0]) + square(i[1][1])):
        print i[0] * i[1][0] * i[1][1]
        break
    
