# 2019-02-04 20:00:38

t = int(input())

for i in range(t):
    minjars = 1;
    n = int(input())
    myList = list(map(int, input().strip().split()))
    for x in myList:
        minjars = minjars + x - 1
    print(minjars)
    myList.clear()
