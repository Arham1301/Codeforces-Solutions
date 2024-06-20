test=int(input())
while test:
    x=input()
    x1=x.split()
    L=list(map(int,x1))
    x=L[0]
    y=L[1]
    total=y/2
    if(total%1!=0):
        total=int(total)+1
    else:
        total=int(total)
    cells_left=(15*total)-(4*y)
    if(x<=cells_left):
        print(total)
        test=test-1
        continue
    else:
        extra=x-cells_left
        extra_square=extra/15
        if extra_square%1!=0:
            extra_square=int(extra_square)+1
        else:
            extra_square=int(extra_square)
        total=total+extra_square
        print(total)
        test=test-1
        continue
