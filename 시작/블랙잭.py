nm=[int (x) for x in input().strip().split()]
ca=[int (x) for x in input().strip().split()]
sum=0
for i in range(0,nm[0]-2):
    a=ca[i]
    for j in range(i+1,nm[0]-1):
        b=ca[j]
        for k in range(j+1,nm[0]):
            c=ca[k]
            t=a+b+c
            if t>sum and t<=nm[1]:
                sum=t
print(sum)