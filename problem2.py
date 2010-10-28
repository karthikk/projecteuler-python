#!/usr/bin/python

def evengen():
    a = 1
    b = 2
    while a < 4000000:
        a, b = b, a+b
        if a%2 == 0:
            yield a

def getsum():
    gen = evengen()
    total = 0
    while 1:
        try:
            total += gen.next()
        except StopIteration:
            break
    print total
        
if __name__ == "__main__":
    getsum()
