number,k=map(int,input().split())
lis=list(map(int,input().split()))
a=1
for i in range(0,len(lis)):
    for j in range(i+1,len(lis)):
        r=lis[i]+lis[j]
        if r==k:
            a=0
if a==0:
    print("yes")
else:
    print("no")
