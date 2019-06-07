num,con=map(int,input().split())
l=list(map(int,input().split()))
if con==1:
    print(min(l))
elif con==2:
    print(max(l[0],l[num-1]))
else:
    print(max(l))
