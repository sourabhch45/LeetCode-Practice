n=int(input())
res=[]
res.append([1])
for i in range(n-1):
    res.append([1,1])
res[2].insert(1,2)
for i in range(3,n):
    insrt=1
    endat=len(res[i-1])
    for j in range(1,endat):
            print('j=',j)
            temp=res[i-1][j]+res[i-1][j-1]
            res[i].insert(insrt,temp)
print('final:',res)