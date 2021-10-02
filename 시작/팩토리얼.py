def fac(a,n):
    if n==0:
        print(a)
        return
    a*=n
    n-=1
    fac(a,n)

x=int(input())
fac(1,x)