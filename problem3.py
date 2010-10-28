#!/usr/bin/python

num = 600851475143
n = 2
while (n != num):
    if num % n == 0:
        num = num/n
    n += 1

print num
