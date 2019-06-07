num=int(input())
lis=list(map(int,input().split()))
a=0
for i in range(1,len(lis)):
    if (sum(lis[:i]))//len(lis[:i])==(sum(lis[i:]))//len(lis[i:]):
        a+=1
        break
    else:
        a=0
if a>=1:
    print("yes")
else:
    print("no")
