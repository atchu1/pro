M=input()
A=""
p=0
li=[]
 if M==M[::-1]:
     li.append(0)
for i in range(0,len(M)-1):
   for j in range(i+1,len(M)):
       A=M[i:j+1]
       if A==A[::-1]:
          li.append(len(M)-len(A))
print(min(li))
