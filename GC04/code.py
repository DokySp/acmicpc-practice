
inp = int(input())

arr = [5, 10, 15, 19, 23, 30, 47, 56, 78, 80]

# 이진탐색
# Divide and conquer

# n = int((len(arr)/2) + 0.6)

left = []
right = []


def c_half(target):
    return int(len(target)/2 + 0.5)


def divide(left: list[int], right: list[int], target: int, idx: int):
    right_idx = len(left) + idx

    if len(right) == 0:
        return -1

    # conquer
    if right[0] == target:
        return right_idx

    if right[0] < target:
        # right
        return divide(right[0: c_half(right)], right[c_half(
            right): len(right)], target, right_idx)
    else:
        # left
        return divide(left[0: c_half(left)], left[c_half(
            left): len(left)], target, idx)


result = divide(arr[0: c_half(arr)], arr[c_half(arr): len(arr)], inp, 0)
print(result)
