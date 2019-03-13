# 2019-03-08 17:49:53
# Nitish S. Prajapati

import math
from decimal import *

def subarray(List, k, count):
    end = len(List)
    count = 0
    while end != 0:
        for j in range(0, end):
            subarray = List[j:end]
            subarray.sort()
            #print(subarray)
            m = math.ceil(Decimal(k)/Decimal(len(subarray)))
            index = math.ceil(Decimal(k)/Decimal(m))
            X = subarray[index-1]
            F = subarray.count(X)
            if F in subarray:
                count = count + 1
        end = end - 1
    print(count)

t = int(input())

for _1 in range(t):
    n,k = map(int, input().strip().split())
    l = list(map(int, input().strip().split()))
    subarray(l, k, 0)
