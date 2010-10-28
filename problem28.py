#!/usr/bin/python

def problem28():
    def diagonalnumgenerator():
        num = 1
        level = 1
        pos = 0
        while level < 1002:
            yield num
            if pos == 0:
                level += 2
            pos = (pos + 1) % 4
            num += level - 1

    dng = diagonalnumgenerator()
    print sum(dng)

if __name__ =="__main__":
    problem28()
            
