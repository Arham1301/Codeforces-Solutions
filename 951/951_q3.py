import math
from functools import reduce
def lcm_multiple(*args):
    return reduce(math.lcm, args)
test=int(input())
while test!=0:
    n=int(input())
    L1 = input()
    L1 = L1.split()
    L1 = list(map(int, L1))
    lcm=lcm_multiple(*L1)
    count=0
    L2=[]
    for i in L1:
        count=count+int(lcm/i)
        L2.append(str(int(lcm/i)))
    if count>=lcm:
        print(-1)
    else:
        print(' '.join(L2))

    test=test-1