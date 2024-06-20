test=int(input())
while test!=0:
    x = input()
    x = x.split()
    x = list(map(int, x))
    n=x[0]
    f=x[1]
    k=x[2]
    L = input()
    L = L.split()
    L = list(map(int, L))
    key=L[f-1]
    L.sort(reverse=True)
    find=L[k-1]
    if key<find:
        print("NO")
        test=test-1
        continue
    if key>find:
        print("YES")
        test=test-1
        continue
    if k in range(len(L)):
        if L[k-1]!=L[k] :
            print("YES")
        else:
            print("MAYBE")
    else:
        print("YES")



    test=test-1