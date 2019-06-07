num=input()
li=[]
for i in num:
	if i not in li:
		li.append(i)
	else:
		break
print(len(li))
