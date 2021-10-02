N=int(input())
l1=[int (x) for x in input().strip().split()]
l2=[]
a=0
for i in l1:
    if (i in l2)==False:
        l2.append(i)
    else:
        a+=1
print(a)