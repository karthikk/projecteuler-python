#!/usr/bin/python

def problem48():
    def powergen():
        i = 1
        while i <= 1000:
            if i % 10 == 0:
                yield 0
            else:
                temp = 1
                prod = 1
                while temp <= i:
                    prod *= i
                    prod = prod % 10000000000
                    temp += 1
                yield prod
            i += 1

    print sum(powergen()) % 10000000000

if __name__ == "__main__":
    problem48()
