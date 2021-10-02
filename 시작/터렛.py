import math
a=int(input())
for i in range(a):
    R=[int (x) for x in input().strip().split()]
    r=math.sqrt((R[0]-R[3])**2+(R[1]-R[4])**2)
    ra=R[2]+R[5]

    if r>ra:
        print(0)
    elif r==ra:
        print(1)
    else:
        if R[2]>R[5]:
            k=R[2]
            l=R[5]
        else:
            k=R[5]
            l=R[2]
        if k>(r+l):
            print(0)
        elif k==(r+l):
            if R[2] == R[5]:
                print(-1)
            else:
                print(1)

        else:
            print(2)