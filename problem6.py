#!/usr/bin/python

def sumofsquares(n):
    return n * (n + 1) * (2 * n + 1) / 6

def squareofsum(n):
    s = n * (n + 1) / 2
    return s * s

print (squareofsum(100) - sumofsquares(100))
