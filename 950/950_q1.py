from collections import Counter
test=int(input())
while test!=0:
    x = input()
    x = x.split()
    x = list(map(int, x))
    m=x[0]
    n=x[1]
    L=input()
    mapping=Counter(L)
    ans=0
    for i in mapping:
        if mapping[i]<n:
            ans=ans+(n-mapping[i])
    ans=ans+((7-len(mapping))*n)
    print(ans)
    test=test-1