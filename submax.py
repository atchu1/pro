import math
var,c=map(int,input().split())
p=a=[]
m=s=0
for i in range(0,var):
    d=list(map(int,input().split()))
    p.append(d) 
if var==2: var=var+1
for i in range(2,var):
    for j in range(0,i):
        for h in range(0,i):
            if a[j][h]==1: s=s+1
    if s==i**2: m=s
if m==0:
    s=1
    print(s)
else:
    m=math.sqrt(m)
    if m==1: m=m+1
    for i in range(0,int(m)):
        for j in range(0,int(m)):
            if j==int(m)-1:
                print("1",end="")
            else: print("1",end=" ")
        print("\r")
