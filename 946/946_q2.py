test=int(input())
while test:
    length=int(input())
    s=input()
    set1=set()
    L=[]
    for i in s:
        if i not in set1:
            L.append(i)
            set1.add(i)
    L.sort()
    mapping={}
    sort_len=len(L)
    for i in range(0,int(sort_len/2),1):
        mapping[L[i]]=L[sort_len-i-1]
        mapping[L[sort_len-i-1]]=L[i]
    L1=[]
    for i in s:
        if i in mapping:
            L1.append(mapping[i])
            continue
        L1.append(i)
    print(''.join(L1))
    test=test-1