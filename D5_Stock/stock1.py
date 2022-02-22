prices=[7,1,2,4,6,5]
j=0
res=0
for i in range(len(prices)-1):
    j=i
    print('i',i)
    while j <= len(prices)-1:
        
        print(prices[i],prices[j])
        maxx=max(prices[i:])
        profati=maxx-prices[i]
        res=max(res,profati)
        print('res',res)
        j+=1
print(res)