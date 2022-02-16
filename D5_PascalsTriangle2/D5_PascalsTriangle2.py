rowIndex=int(input())
res=[]

if rowIndex == 1:
    res=[1]
elif rowIndex==2:
    res=[1,1]
elif rowIndex>=3:
    res=[1,2,1]
for i in range(3,rowIndex):
    insrt=1
    endat=len(res)
    print('endat=',endat)
    temp=[]
    for j in range(1,endat):
        summ=res[j]+res[j-1]
        temp.append(summ)
    temp.append(1)
    temp.insert(0,1)
    res.clear()
    res.extend(temp)

print(res)