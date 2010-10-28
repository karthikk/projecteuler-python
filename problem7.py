#!/usr/bin/python

import time

def primegen():
    primelist = []
    current = 3
    yield 2
    while 1:
        isprime = 1
        for i in primelist:
            if current % i == 0:
                isprime = 0
                break
        if isprime:
            primelist.append(current)
            yield current
        current += 2


i = 1
pg = primegen()
start = time.time()
while i < 10001:
    pg.next()
    i += 1
end = time.time()
print "The 10001st prime is %d" % pg.next()
print "Time elapsed: %d" % (end - start)
