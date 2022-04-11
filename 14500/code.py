
inp = input().split(" ")
N = int(inp[0])
M = int(inp[1])

board = []

for i in range(N):
    tmp = []
    inp = input().split(" ")

    for j in range(M):
        tmp.append(int(inp[j]))
    board.append(tmp)


# N, M = 5, 5
# board = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [1, 2, 1, 2, 1]]


def check_range(n: int, m: int, x: int, y: int):
    if n+(y-1) >= N:
        return False
    if m+(x-1) >= M:
        return False
    return True


# 작대기
def b1(n: int, m: int):
    if not check_range(n, m, 4, 1):
        return 0
    sums = board[n][m] + board[n][m+1] + board[n][m+2] + board[n][m+3]
    return sums

def b2(n: int, m: int):
    if not check_range(n, m, 1, 4):
        return 0
    sums = board[n][m] + board[n+1][m] + board[n+2][m] + board[n+3][m]
    return sums




# 네모
def x1(n: int, m: int):
    if not check_range(n, m, 2, 2):
        return 0
    sums = board[n][m] + board[n+1][m] + board[n+1][m+1] + board[n][m+1]
    return sums





# ㅗ
def f1(n: int, m: int):
    if not check_range(n, m, 3, 2):
        return 0
    sums = board[n][m+1] + board[n+1][m] + board[n+1][m+1] + board[n+1][m+2]
    return sums
# ㅏ
def f2(n: int, m: int):
    if not check_range(n, m, 2, 3):
        return 0
    sums = board[n][m] + board[n+1][m] + board[n+1][m+1] + board[n+2][m]
    return sums
# ㅜ
def f3(n: int, m: int):
    if not check_range(n, m, 3, 2):
        return 0
    sums = board[n][m] + board[n][m+1] + board[n+1][m+1] + board[n][m+2]
    return sums
# ㅓ
def f4(n: int, m: int):
    if not check_range(n, m, 2, 3):
        return 0
    sums = board[n][m+1] + board[n+1][m+1] + board[n+2][m+1] + board[n+1][m]
    return sums




# 번개
def l1(n: int, m: int):
    if not check_range(n, m, 2, 3):
        return 0
    sums = board[n][m] + board[n+1][m] + board[n+1][m+1] + board[n+2][m+1]
    return sums

def l2(n: int, m: int):
    if not check_range(n, m, 2, 3):
        return 0
    sums = board[n][m+1] + board[n+1][m+1] + board[n+1][m] + board[n+2][m]
    return sums

def l3(n: int, m: int):
    if not check_range(n, m, 3, 2):
        return 0
    sums = board[n+1][m] + board[n+1][m+1] + board[n][m+1] + board[n][m+2]
    return sums

def l4(n: int, m: int):
    if not check_range(n, m, 3, 2):
        return 0
    sums = board[n][m] + board[n][m+1] + board[n+1][m+1] + board[n+1][m+2]
    return sums





# ㄴ
def n1(n: int, m: int):
    if not check_range(n, m, 2, 3):
        return 0
    sums = board[n][m] + board[n+1][m] + board[n+2][m] + board[n+2][m+1]
    return sums
def n2(n: int, m: int):
    if not check_range(n, m, 2, 3):
        return 0
    sums = board[n][m] + board[n][m+1] + board[n+1][m+1] + board[n+2][m+1]
    return sums
def n3(n: int, m: int):
    if not check_range(n, m, 3, 2):
        return 0
    sums = board[n+1][m] + board[n+1][m+1] + board[n+1][m+2] + board[n][m+2]
    return sums
def n4(n: int, m: int):
    if not check_range(n, m, 3, 2):
        return 0
    sums = board[n+1][m] + board[n][m] + board[n][m+1] + board[n][m+2]
    return sums



# ㄴ 대칭
def m1(n: int, m: int):
    if not check_range(n, m, 2, 3):
        return 0
    sums = board[n+2][m] + board[n+2][m+1] + board[n+1][m+1] + board[n][m+1]
    return sums
def m2(n: int, m: int):
    if not check_range(n, m, 2, 3):
        return 0
    sums = board[n+2][m] + board[n+1][m] + board[n][m] + board[n][m+1]
    return sums
def m3(n: int, m: int):
    if not check_range(n, m, 3, 2):
        return 0
    sums = board[n][m] + board[n][m+1] + board[n][m+2] + board[n+1][m+2]
    return sums
def m4(n: int, m: int):
    if not check_range(n, m, 3, 2):
        return 0
    sums = board[n][m] + board[n+1][m] + board[n+1][m+1] + board[n+1][m+2]
    return sums



block = [b1, b2, x1, f1, f2, f3, f4, l1, l2, l3, l4, n1, n2, n3, n4, m1, m2, m3, m4]


max_val = -1

for selected_bloc in block:
    for n in range(N):
        for m in range(M):
            tmp = selected_bloc(n, m)
            if tmp > max_val:
                max_val = tmp

print(max_val)