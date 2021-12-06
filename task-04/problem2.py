#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a=1
    b=2
    sum=0
    for i in range(2,n):
        c=a+b
        if a%2==0 and a<n:
            sum+=a
        a=b
        b=c
    print(sum)