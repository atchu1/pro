num=int(input())
li=list(map(int,input().split()))
x=[]
c=1
for i in range(num-1):
	if li[i]<li[i+1]:
		c+=1
	else:
		x.append(c)
		c=1
x.append(c)
print(max(x))
