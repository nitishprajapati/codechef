# 2019-03-02 19:28:37
# Nitish S. Prajapati

t = int(input())

for _ in range(t):
    n,d = input().strip().split()
    l = [int(x) for x in n]
    d = int(d)
    # print(l)

    # list  d

    if len(l) == 1:
        num = l[0]
        if num > d:
            print(d)
        else:
            print(num)
        continue

    index = len(l)-1
    previous = index
    index = index - 1
    while True:
        #print('debug a ')
        over = False

        while l[index] <= l[previous]:
            index = index - 1
            previous = previous - 1
            if index == -1:
                over = True
                break

        if over:
            break

        # here index > previous

        savepoint = index

        stuff = 0
        while l[index] >= l[previous]:
            index = index - 1
            previous = previous - 1
            stuff = stuff + 1
            if index == -1:
                over = True
                break

        # now delete everything from previous to savepoint
        del l[previous:savepoint+1]

        # now fill with 'd'
        while stuff!=0:
            l.append(d)
            stuff = stuff - 1
        if over:
            break



        skip = l[previous]
        index = previous - 1
        while True:
            if index == -1:
                over = True
                break
            if l[index] != skip:
                break
            if l[index] == skip:
                index = index - 1

        if over:
            break


        previous = index + 1


    stuff = 0
    i = 0
    while True:
        if i == len(l):
            break
        if l[i] > d:
            del l[i]
            stuff = stuff + 1
        else:
            i = i + 1

    while stuff:
        l.append(d)
        stuff = stuff - 1
    # print(l)
    for x in l:
        print(x,sep='',end='')
    print()
