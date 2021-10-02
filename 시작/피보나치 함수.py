def P(a, b, c, n):
    if n==0:
        print(1, 0)
        return
    elif n == c:
        print(b, a)
        return
    k=a
    a+=b
    c+=1

    P(a,k,c,n)

x=int(input())
for i in range(x):
    k=int(input())
    P(0,1,0, k)