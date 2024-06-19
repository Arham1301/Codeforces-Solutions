test=int(input())
while test!=0:
    L1 = input()
    L1 = L1.split()
    L1 = list(map(int, L1))
    x=L1[0]
    y=L1[1]
    count=0
    while(x!=0 and y!=0):
        if x%2==y%2:
            x=x//2
            y=y//2
            count=count+1
        else:
            break
    if x==0 or y==0:
        z=x+y
        while(z%2==0 and z!=0):
            count=count+1
            z=z//2
    print(pow(2,count))
    test=test-1
