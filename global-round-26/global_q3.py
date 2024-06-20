test=int(input())

while test!=0:
    n=int(input())
    L = input()
    L = L.split()
    L = list(map(int, L))
    c=0
    for i in range(len(L)-1):
        c=c+L[i]
        if L[i+1]<0 and c<0:
            c=-1*abs(c)
        else:
            c=abs(c)
    print(max(abs(sum(L)),abs(c+L[len(L)-1])))


    test=test-1
