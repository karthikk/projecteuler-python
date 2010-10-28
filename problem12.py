#!/usr/bin/python

def gentrianglenumber():
    total = 0
    i = 1
    while 1:
        total += i
        yield total
        i += 1

def getprimefactors(n):
    i = 2
    pdict = {}
    while n > 1:
        while n % i == 0:
            n = n / i
            pdict[i] = pdict.get(i, 0) + 1
        i += 1
    return pdict
        

gtn = gentrianglenumber()
while 1:
    tn = gtn.next()
    pdict = getprimefactors(tn)
    numfactors = reduce(lambda x, y: x * (y+1), pdict.values(), 1)
    if numfactors >= 500:
        print "The number with over 500 divisors %d" % tn
        break
