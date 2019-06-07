num=input()
ma=0
for i in range(1,len(num)):
    if num[0]<num[i]:
        ma=num.index(n[i]) 
        break
for i in range(ma,len(num)):
    print(num[i],end="")
