test=int(input())
while test!=0:
    x = input()
    x1 = x.split()
    L = list(map(int, x1))
    n=L[0]
    m=L[1]
    if n<m:
        print("No")
        test=test-1
        continue
    if n%2==0 and m%2==1:
        print("No")
        test = test - 1
        continue
    if n%2==1 and m%2==0:
        print("No")
        test = test - 1
        continue
    print("Yes")
    test=test-1
