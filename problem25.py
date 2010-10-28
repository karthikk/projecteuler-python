#!/usr/bin/python

def problem25():
    def numdigits(n):
        return len(str(n))

    a = 1
    b = 1
    term = 1
    while numdigits(a) < 1000:
        a, b = b, a + b
        term += 1
    print term

problem25()
