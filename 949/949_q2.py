import math
test=int(input())
while test!=0:
    x=input()
    x = x.split()
    x = list(map(int, x))
    num=x[0]
    times=x[1]
    if times==0:
        print(num)
        test=test-1
        continue
    ans = math.ceil(math.log2(times))+1
    while(ans!=0):
        num=(num-1)|(num)|(num+1)
        ans=ans-1
    print(num)
    test=test-1