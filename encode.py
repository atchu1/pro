n1=input()
n2=input()
n3=''
for i in range(0,len(n1)):
p1=(ord(str1[i]))-96
p2=(ord(str2[i]))-96
if((p1+p2)<=26):
  n3=n3+(chr(96+p1+p2))
else:
  n3=n3+(chr(96+(p1+p2-26)))
print(n3)        
