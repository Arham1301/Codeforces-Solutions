def count_bit(x):
    count = 0
    while (x != 0):
        count = count + 1
        x = x // 2
    return count


test=int(input())
while test!=0:
    x=int(input())
    L=[0]*32
    while(True):
        count1=count_bit(x)
        remaining=pow(2,count1)-abs(x)
        if count1-count_bit(remaining)==1:
            x=x-pow(2,count1-1)
            L[count1-1]=1
        else:
            x=x-pow(2,count1)
            L[count1]=1

    test=test-1


