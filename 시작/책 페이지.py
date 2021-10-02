def f(a,l):
    b=-1
    c=a
    d=a
    while(a!=0):
        a=int(a/10)
        b+=1

    if b!=0:
        c=int(c%(10**b))
        for i in range(0,10):
            l[i]+=(10**(b-1))*(int(d/(10**(b))))
        l[0]-=1
        if c!=0:
            f(c, l)
        else:
            print(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7], l[8], l[9])

    else:
        for i in range(c):
            l[i+1]+=1
        print(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9])

li=[0,0,0,0,0,0,0,0,0,0]
N=int(input())
f(N,li)
#미완