#atchu
num=int(input())
x=list(map(int,input().split()))
y=[]
z=[]
for i in range(len(x)):
    if(i%2==0):
        y.append(x[i])
    else:
        z.append(x[i])
for j in y:
    d=sum(y)
for k in z:
    f=sum(z)
if(d>f):
    print(d)
else:
    print(f)
