test=int(input())
while test!=0:
    length=int(input())
    L = input()
    L = L.split()
    L = list(map(int, L))
    ab={}
    bc={}
    ac={}
    abc={}
    ans=0
    for i in range(length-2):
        x=L[i]
        y=L[i+1]
        z=L[i+2]
        if (x,y) not in ab:
            ab[(x, y)]=0
        if (y,z) not in bc:
            bc[(y, z)]=0
        if (x,z) not in ac:
            ac[(x, z)]=0
        if (x,y,z) not in abc:
            abc[(x,y,z)]=0

        ab[(x,y)]+=1
        bc[(y,z)]+=1
        ac[(x,z)]+=1
        abc[(x,y,z)]+=1
        ans=ans+ab[(x,y)]+bc[(y,z)]+ac[(x,z)]-(3*abc[(x,y,z)])
    print(ans)


    test=test-1


