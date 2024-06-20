from collections import Counter
test=int(input())
while test!=0:
    n=int(input())
    L=input()
    if n%2==1:
        print("NO")
        test=test-1
        continue
    mapping=Counter(L)
    ans={}
    a=['N','S','E','W']
    flag_h=-1
    flag_r=-1
    flag=1
    for i in a:
        ans[i]=[]
    if 'N' in mapping and 'S' in mapping:
        flag_r = 1
        flag_h = 1
        minimum=min(mapping['N'],mapping['S'])
        mapping['N']=mapping['N']-minimum
        mapping['S']=mapping['S']-minimum
        minimum1=int(minimum/2)
        minimum2=minimum-minimum1
        ans['N'].extend(['H']*minimum1)
        ans['S'].extend(['H']*minimum1)
        ans['N'].extend(['R'] * minimum2)
        ans['S'].extend(['R'] * minimum2)
        if minimum1==0:
            flag_h=-1
        if minimum2==0:
            flag_r=-1
    if 'E' in mapping and 'W' in mapping:
        minimum=min(mapping['E'],mapping['W'])
        mapping['W']=mapping['W']-minimum
        mapping['E']=mapping['E']-minimum
        minimum1 = int(minimum/2)
        minimum2 = minimum - minimum1
        if flag_r==1 and flag_h==1:
            ans['E'].extend(['H'] * minimum1)
            ans['W'].extend(['H'] * minimum1)
            ans['E'].extend(['R'] * minimum2)
            ans['W'].extend(['R'] * minimum2)
        if flag_r==-1 and flag_h==-1:
            ans['E'].extend(['H'] * minimum1)
            ans['W'].extend(['H'] * minimum1)
            ans['E'].extend(['R'] * minimum2)
            ans['W'].extend(['R'] * minimum2)
        elif flag_r==-1 and flag_h!=-1:
            ans['E'].extend(['R'] * minimum)
            ans['W'].extend(['R'] * minimum)
        elif flag_h==-1 and flag_r!=-1:
            ans['E'].extend(['H'] * minimum)
            ans['W'].extend(['H'] * minimum)
    for i in mapping:
        if mapping[i]%2!=0:
            print("NO")
            flag=-1
            break
        else:
            ans[i].extend(['H']*(int(mapping[i]/2)))
            ans[i].extend(['R'] * int((mapping[i]/2)))
    if flag==-1:
        test=test-1
        continue
    a=0
    b=0
    c=0
    d=0
    answer=[]
    for i in L:
        if i=='N':
            answer.append(ans['N'][a])
            a=a+1
        elif i=='S':
            answer.append(ans['S'][b])
            b=b+1
        elif i=='E':
            answer.append(ans['E'][c])
            c=c+1
        elif i=='W':
            answer.append(ans['W'][d])
            d=d+1
    if 'H' not in answer or 'R' not in answer:
        print("NO")
    else:
        x=''.join(answer)
        print(x)
    test=test-1