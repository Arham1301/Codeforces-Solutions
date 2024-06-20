test=int(input())
while test!=0:
    n=int(input())
    L1 = input()
    L1 = L1.split()
    L1 = list(map(int, L1))
    L=[]
    for i in range(n-1):
        L.append(max(L1[i],L1[i+1]))
    print(min(L)-1)
    test=test-1
