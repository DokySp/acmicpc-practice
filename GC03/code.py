

arr = [15, 80, 19, 56, 78, 23, 5, 30, 10, 47]

# # 삽입정렬
for i in range(len(arr)):
    target = arr[i]

    for n in range(0, i):
        if arr[n] >= arr[i]:
            tmp = arr.pop(i)
            arr.insert(n, tmp)

print(arr)
