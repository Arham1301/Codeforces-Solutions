test=int(input())
while test!=0:
    chess1=input()
    chess2=chess1.split()
    chess=list(map(int,chess2))
    if(sum(chess)%2==1):
        print(-1)
        test=test-1
        continue
    maximum=0
    ind=-1
    for i in range(len(chess)):
        if chess[i]>maximum:
            maximum=chess[i]
            ind=i
    for j in range(len(chess)):
        if j!=ind:
            a=chess[j]
            break
    b=sum(chess)-maximum-a
    count=0
    while((a+b)>maximum and a!=0 and b!=0):
        a=a-1
        b=b-1
        count=count+1
    count=count+a+b
    print(count)
    test=test-1