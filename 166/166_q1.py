test=int(input())
while test!=0:
    x=int(input())
    y=input()
    ind=0
    flag=-1
    for i in range(len(y)-1):
        if ord(y[i])>ord(y[i+1]):
            print("NO")
            flag=1
            break
    if flag==-1:
        print("YES")
    test=test-1