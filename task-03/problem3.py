#!/bin/python3

import sys
def if_prime(n):
    if n==1:
        return False
    counter=1
    for i in range(2,n+1):
        if n%i==0:
            counter+=1
    return counter==2


def prime_factors(num):
    arr=[]
    for i in range (2,num+1):
        if if_prime(i):
            if num%i==0:
                arr.append(i)
    return arr

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(max(prime_factors(n)))
    

    
