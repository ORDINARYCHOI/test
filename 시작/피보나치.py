def P(a, b, c, n):
    if n == c:
        print(a)
        return
    k=a
    a+=b
    c+=1

    P(a,k,c,n)

x=int(input())
P(0,1,0, x)