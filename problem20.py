#!/usr/bin/python

def problem20():
    print sum(int(x) for x in str(reduce(lambda x, y: x * y, range(1, 101))))

if __name__ == "__main__":
    problem20()
