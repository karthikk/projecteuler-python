#!/usr/bin/python
ones = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    }

tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
    }
def numberofletters(n):
    if n < 20:
        return len(ones[n])
    elif n < 100:
        return len(tens[n/10]) + len(ones[n%10])
    elif n < 1000:
        l = len(ones[n/100]) + len('hundred')
        n = n % 100
        if n:
            return l + len('and') + numberofletters(n)
        else:
            return l
        
    else:
        return len('onethousand')

print sum([numberofletters(x) for x in range(1, 1001)])
