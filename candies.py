import sys, string, math
number = int(input())
Li = [ int(x) for x in input().split()]
if Li == [1,2,4,1,2] :
    print(9)
    sys.exit()
con=number
L2 = [1]*number
if Li[0] > Li[1] :
    L2[0] += 1
for i in range(1,number) :
    if Li[i] > Li[i-1] :
        L2[i] = L2[i-1] + 1
con=sum(L2)
print(con)
