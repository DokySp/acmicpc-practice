
# n = int(input())

# time = []
# price = []


# for i in range(0,n):
#     tmp = input().split()
#     time.append(int(tmp[0]))
#     price.append(int(tmp[1]))


# n = 10
# time = [5,4,3,2,1,1,2,3,4,5]
# price = [50,40,30,20,10,10,20,30,40,50]

n = 5
time = [1,2,3,4,5]
price = [10,20,30,40,50]



initIdx = 0
idx = 0
totalPrices = []

for i in range(0, n):
    
    idx = initIdx

    # 첫 작업부터 시간 넘어가는 경우 스킵
    if len(time) < (idx + time[idx]): 
        initIdx += 1
        continue

    totalPrice = 0
    totalPrice += price[idx]
    idx += time[idx]
    
    while( len(time) > idx ):
        
        # 일수가 넘어갈 때 다음 작업으로 넘어감
        if len(time) < (idx + time[idx]): 
            idx += 1
            continue
        
        totalPrice += price[idx]
        idx += time[idx]
    
    totalPrices.append(totalPrice)
    initIdx += 1


print(totalPrices)
max = -1

for i in totalPrices:
    if max < i: max = i

print(max)





