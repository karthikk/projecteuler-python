#! /usr/bin/python
import pprint
def problem21():
    def getsumoffactors(x):
        factors = set()
        tempx = x
        n = 2
        while x > 1:
            while x % n == 0:
                new_items = [n]
                for i in factors:
                    new_items.append(i * n)
                factors = factors.union(new_items)
                x /= n
            n += 1
        factors.add(1)
        factors.remove(tempx)
        return sum(factors)

    num_factors = {}
    for i in xrange(1, 10000):
        num_factors[i] = getsumoffactors(i)
    s = 0
    amic_numbers = set()
    for x in num_factors.keys():
        try:
            if x == num_factors[num_factors[x]] and x != num_factors[x]:
                amic_numbers.add(x)
        except KeyError:
            pass
    print sum(amic_numbers)

problem21()
        
