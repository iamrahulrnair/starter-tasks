#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    counter=1
    while True:
        _loop=0
        for i in range(1,n+1):
            if(counter%i==0):
                _loop+=1
        if _loop==n:
            break
        counter+=1
    print(counter)

# pass all test case