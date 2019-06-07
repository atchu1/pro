num=int(input())
i=0
li=[]
while(i<num):
    lis=list(map(int,input().split(" ")))
    li.extend(lis)
    i=i+1
li.sort() 
i=0
while(i<len(li)):
    print(li[i],end=" ")
    i+=1
 
