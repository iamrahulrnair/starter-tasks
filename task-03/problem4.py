#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    max=0
    for i in range(100,1000):
        for j in range(100,1000):
            mul=i*j
            if checkPal(mul) and mul<n:
                if(mul>max):
                    max=mul
    print(max)


    
def checkPal(n):
    temp=n
    rem=0
    while(n>0):
        dig=n%10
        rem=rem*10+dig
        n=n//10
    return temp==rev