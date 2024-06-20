test=int(input())
while test!=0:
    L = input()
    flag=1
    if len(L)==1:
        print("NO")
        test=test-1
        continue
    if L[-1]=='9' or L[0]!='1':
        print("NO")
        test=test-1
        continue
    for i in range(1,len(L)-1):
        if L[i]=='0':
            flag=-1
            break
    if flag==-1:
        print("NO")
    else:
        print("YES")

    test=test-1