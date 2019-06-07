x,y=map(int,input().split())
li=list(map(int,input().split()))
li.sort(reverse=True)
c=0
for i in range(0,len(li)):
	if y>=li[i]:
	    r=y//li[i]
	    c=c+r
	y=y%li[i]
	if y==0:
		break
print(c)
