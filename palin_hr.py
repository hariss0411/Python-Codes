#!/bin/python3

import os
import sys
from itertools import combinations
#
# Complete the buildPalindrome function below.
#
def substr(a):
    '''length = len(string) + 1
    return [string[x:y] for x, y in combinations(range(length), r=2)]
    return [a[i:j] for i in range(len(a)) for j in range(i+1,len(a)+1)]'''
    s=[]
    v=""
    for i in range(len(a)):
        for j in range(i+1,len(a)+1):
            v=a[i:j]
            if v not in s:
                s+=[a[i:j]]
    return s
    
def buildPalindrome(a, b):
    # Write your code here.
    s_a,s_b = substr(a),substr(b)
    sub=[]
    s_aa,s_bb=[],[]

    for i in s_a:
        for j in s_b:
            c=i+j
            if c==c[::-1]:
                sub+=[c]
    if sub:
        sub=sorted(sub,key=len)
        l=len(sub[-1])
        ns_sub=[]
        for i in sub:
            if len(i)==l:
                ns_sub+=[i]
        ns_sub.sort()
        return (ns_sub[0])
    else: return "-1"


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        a = input()

        b = input()

        result = buildPalindrome(a, b)

        print(result + '\n')
