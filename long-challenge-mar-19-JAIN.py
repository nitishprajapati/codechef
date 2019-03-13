# 2019-03-01 19:03:12
# Nitish S. Prajapati

t = int(input())

for _1 in range(t):
    n = int(input())
    List = []
    
    for _2 in range(n):
        string = input()
        Set = set(string)
        List.append(Set)
        
    counter = 0    
    for i in range(len(List)-1):
        for j in range(i+1,len(List)):
            #print(List[i], List[j])
            tempset = List[i].union(List[j])
            if len(tempset) == 5:
                counter = counter + 1
    
    print(counter)
    List.clear()
