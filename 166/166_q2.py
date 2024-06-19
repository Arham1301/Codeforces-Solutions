import sys
test=int(input())
while test!=0:
    n=int(input())
    L1=input()
    L1 = L1.split()
    L1 = list(map(int, L1))
    L2 = input()
    L2 = L2.split()
    L2 = list(map(int, L2))
    x=L2[n]
    flag=-1
    count=0
    minimum=sys.maxsize
    for i in range(n):
        a=min(L1[i],L2[i])
        b=L1[i]+L2[i]-a
        minimum=min(minimum,abs(L2[i]-x),abs(L1[i]-x))
        if x in range(a,b+1):
            flag=1
        count=count+(b-a)
    if flag==1:
        count=count+1
        print(count)
        test=test-1
        continue
    count=count+minimum+1
    print(count)


    test=test-1