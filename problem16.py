#!/usr/bin/python

def sumofdigits(n):
    return sum(int(x) for x in str(n))

print sumofdigits(2**1000)
