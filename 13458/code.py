
import math

n = int(input())
a = input().split(" ")
b = input().split(" ")
c = int(b[1])
b = int(b[0])

total = 0

for i in range(0,n):

    classroom = int(a[i])
    classroom -= b

    if classroom < 0: classroom = 0

    rest = math.ceil(classroom / c)
    total += (rest + 1)

print(total)

