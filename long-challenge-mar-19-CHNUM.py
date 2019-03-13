# 2019-03-01 16:38:12
# Nitish S. Prajapati
# CHNUM

t = int(input())

for i in range(t):
    n = int(input())
    l = list(map(int, input().strip().split()))
    positiveCount = 0
    negativeCount = 0
    
    for num in l:
        if num < 0:
            negativeCount = negativeCount + 1
        else:
            positiveCount = positiveCount + 1
    
    if negativeCount == 0:
        print(positiveCount, positiveCount)
    elif positiveCount == 0:
        print(negativeCount, negativeCount)
    elif positiveCount > negativeCount:
        print(positiveCount, negativeCount)
    else:
        print(negativeCount, positiveCount)
    l.clear()
