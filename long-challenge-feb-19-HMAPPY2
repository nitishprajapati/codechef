
# 09:02 AM 02/02/19

import math

def function(tn, wanted, notwanted):
    tn = tn - tn%wanted #adjust proper tn
    w = int((tn-wanted)/wanted) + 1
    n = int((tn-notwanted)/notwanted) + 1
    if (wanted > tn):
        return 0
    if (notwanted > tn):
        return w
    if (wanted == notwanted):
        return 0
    if (wanted > notwanted):
        if (wanted%notwanted == 0):
            return 0
    if (notwanted > wanted):
        if (notwanted%wanted == 0):
            r = w - n
            return r
    if (wanted*notwanted > tn):
        return w
    i = int((tn - wanted*notwanted)/(notwanted*wanted)) + 1
    u = w + n - i
    r = u - n
    return r


t = int(input())
for i in range(t):
    n, a, b, k = map(int, input().strip().split())
    tot = function(n, a, b) + function(n, b, a)
    if(tot>=k):
        print("Win")
    else:
        print("Lose")
