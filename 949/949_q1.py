import math
test=int(input())
while test!=0:
    x=input()
    x = x.split()
    x = list(map(int, x))
    num=x[1]
    ans=math.floor(math.log2(num))
    print(int(ans))
    test=test-1