#!/usr/bin/python

a = []
for i in range(20):
    for j in a:
        if i % j == 0:
            i = i/j
    if i > 1:
        a.append(i)

product = 1
print (reduce (lambda x, y: x*y, a))
