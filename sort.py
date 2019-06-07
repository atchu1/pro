x,y=map(int,input().split())
if x<=y:
  d=x
else:
  d=y
z=[]
for i in range(0,d):
  z.append(sorted(list(map(int,input().split()))))
c=sorted(z)
for i in range(0,len(c[0])):
  for j in range(0,len(c)-1):
    if c[j][i]>c[j+1][i]:
      c[j][i],c[j+1][i]=c[j+1][i],c[j][i]
for i in c:
  print(*i)
