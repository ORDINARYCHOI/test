i=[]
i.append(int(input()))
i.append(int(input()))
b=[int(i[1]/100),int(i[1]/10)%10,i[1]%10]
sum=0
for x in range(0, 3):
    A=i[0]*b[2-x]
    print(A)
    sum+=A*10**x
print(sum)