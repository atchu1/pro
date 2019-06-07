A=int(input())
M=list(map(int,input().split()))
p=[]
for i in M:
	s=bin(i)[2::]
	p.append(([s.count("1"),i]))
p.sort(reverse=True)
for i in range(0,len(p)):
	print(p[i][1])
