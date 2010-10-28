#!/usr/bin/python

maxval = 0
chaincount = 0
for i in xrange(2,1000000):
    counter = 0
    val = i
    while (i != 1):
        if i % 2:
            i = 3*i + 1
        else:
            i = i / 2
        counter += 1
    if (counter > chaincount):
        chaincount, maxval = counter, val

print chaincount, maxval
