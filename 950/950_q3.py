test=int(input())
while test!=0:
    n1=int(input())
    L1 = input()
    L1 = L1.split()
    L1 = list(map(int, L1))
    L2 = input()
    L2 = L2.split()
    L2 = list(map(int, L2))
    m=int(input())
    L3 = input()
    L3 = L3.split()
    L3 = list(map(int, L3))
    mapping1={}
    mapping2={}
    set2=set()
    for i in L2:
        set2.add(i)
    for i in range(len(L1)):
        if L1[i]!=L2[i]:
            if L2[i] not in mapping1:
                mapping1[L2[i]]=0
            mapping1[L2[i]]+=1
    for i in range(len(L3)):
        if L3[i] not in mapping2:
            mapping2[L3[i]]=0
        mapping2[L3[i]]+=1
    flag=1
    for i in mapping1:
        if i not in mapping2:
            flag=-1
            break
        if i in mapping2:
            if mapping2[i]<mapping1[i]:
                flag=-1
                break
    if flag==-1:
        print("NO")
        test=test-1
        continue
    if L3[m-1] not in set2:
        print("NO")
        test = test - 1
        continue
    print("YES")
    test=test-1



