test=int(input())
while test!=0:
    n=int(input())
    L = input()
    L = L.split()
    L = list(map(int, L))
    pos=-1
    if L[1]-L[0]!=0:
        pos=1
        L1 = ['R' for _ in range(len(L))]
        L1[pos] = 'B'
        print("YES")
        print(''.join(L1))
        test=test-1
        continue

    for i in range(0,len(L)-1):
        if L[i+1]-L[i]!=0:
            pos=i
            break
    if pos==-1:
        print("NO")
        test=test-1
        continue
    L1=['R' for _ in range(len(L))]
    L1[pos]='B'
    print("YES")
    print(''.join(L1))

    test=test-1