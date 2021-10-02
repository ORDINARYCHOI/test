a=int(input())
l=[]
si=0
for i in range(a):
    b=input().split()
    if b[0]=='push':
        l.append(int(b[1]))
        si+=1
    elif b[0]=='pop':
        if si==0:
            print(-1)
        else:
            print(l.pop())
            si-=1
    elif b[0]=='size':
        print(si)
    elif b[0]=='empty':
        if si==0:
            print(1)
        else:
            print(0)
    else:
        if si==0:
            print(-1)
        else:
            print(l[si-1])