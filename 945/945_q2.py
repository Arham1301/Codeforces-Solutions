def set_bit(num,bit):
    if (num & pow(2,bit)) ==0:
        return False
    else:
        return True


test=int(input())
while test!=0 :
    length=int(input())
    bit2 = input()
    bit1 = bit2.split()
    bit = list(map(int, bit1))
    if (length==1):
        print(1)
        test=test-1
        continue
    global_max=1
    y=20
    while(True):
        if(y==-1):
            break
        local_max=1
        ind=[]
        for i in range(len(bit)):
            if set_bit(bit[i],y):
                ind.append(i)
        if len(ind)==0:
            y=y-1
            continue
        else:

            ind.append(-1)
            ind.append(len(bit))
            ind.sort()
            for i in range(len(ind)-1):
                local_max=max(local_max,(ind[i+1]-ind[i]))
            y=y-1
        global_max=max(global_max,local_max)
    print(global_max)




    test=test-1