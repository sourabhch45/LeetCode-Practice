prices=[7,1,2,4,6,5]
buy=0
sell=1
max_prof=0
while sell<len(prices):
    cur_prof=prices[sell]-prices[buy]
    if prices[buy]<prices[sell]:
        
        max_prof=max(max_prof,cur_prof)
    else:
        buy = sell
        
    sell+=1
print(max_prof)