#!/usr/bin/python
import time

def problem10():
    def primegen(maxval):
        a = range(maxval + 1)
        a[1] = 0
        alen = len(a)
        for i, val in enumerate(a):
            if val:
                val += i
                while val < alen:
                    a[val] = 0
                    val += i
                yield i

    print sum(list(primegen(2000000)))

problem10()
