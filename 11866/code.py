inp = input()
inp = inp.split(" ")

n = int(inp[0])
k = int(inp[1])

arr = []
res_arr = []

for i in range(1,n+1):
    arr.append(i)

currIdx = -1
while len(arr) != 0:
    currIdx = (currIdx + k) % len(arr)
    res_arr.append(arr.pop(currIdx))
    currIdx = currIdx - 1

print("<", end="")
for i in range(0, len(res_arr)-1):
    print(res_arr[i], end=", ")
print(res_arr[len(res_arr)-1], end=">\n")
