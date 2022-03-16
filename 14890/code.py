
# N = 6
# L = 2
# board = [[3, 3, 3, 3, 3, 3], [2, 3, 3, 3, 3, 3], [2, 2, 2, 3, 2, 3], [1, 1, 1, 2, 2, 2], [1, 1, 1, 3, 3, 1], [1, 1, 2, 3, 3, 2]]


inp = input().split(" ")

N = int(inp[0])
L = int(inp[1])

board = []

for i in range(0,N):
    inp = input().split(" ")
    tmp = []
    for j in range(0, N):
        tmp.append(int(inp[j]))
    board.append(tmp)


# 완전탐색
def search(target):

    obs = []
    for n in range(0, N):
        obs.append(False)

    for t in range(0, N):

        # 오르막
        if t+1 < N and target[t+1] == target[t] + 1:

            # 범위가 넘는지
            if t - (L - 1) < 0:
                return False

            # t-(L-1) ~ t 까지의 높이가 같은지 / 기설치 오르막 검사
            for l in range(1, L + 1):
                if target[t - (l - 1)] != target[t] or obs[t - (l - 1)]:
                    return False

            # 오르막 설치
            for l in range(1, L + 1):
                obs[t - (l - 1)] = True

        # 내리막
        elif t+1 < N and target[t + 1] == target[t] - 1:

            # 범위가 넘는지
            if t + L >= N:
                return False

            # t+1 ~ t+L 까지의 높이가 같은지 / 기설치 오르막 검사
            for l in range(1, L+1):
                if target[t + l] != target[t + 1] or obs[t + l]:
                    return False

            # 내리막 설치
            for l in range(1, L+1):
                obs[t + l] = True

        # 두 칸 이상 높이 차이 날 때
        # 오르막
        if t + 1 < N and target[t + 1] > target[t] + 1:
            return False
        # 내리막
        elif t + 1 < N and target[t + 1] < target[t] - 1:
            return False

        # 평지는 그냥 넘어감

    return True


count = 0

# row
for i in range(0, N):
    target = board[i]
    if search(target):
        count += 1
# col
for i in range(0, N):
    target = []
    for j in range(0, N):
        target.append(board[j][i])
    if search(target):
        count += 1

print(count)
