
N, M = input().split(" ")

N = int(N)
M = int(M)

board = []
order = []

for i in range(N):
    tmp = []
    inp = input().split(" ")
    for t in inp:
        tmp.append(int(t))
    board.append(tmp)

for i in range(M):
    tmp = []
    d, s = input().split(" ")
    d = int(d)
    s = int(s)
    dx = 0
    dy = 0

    if d == 1 or d == 2 or d == 8:
        dx = -1
    elif d == 4 or d == 5 or d == 6:
        dx = 1
    if d == 2 or d == 3 or d == 4:
        dy = -1
    elif d == 8 or d == 7 or d == 6:
        dy = 1

    order.append([dx, dy, s])
#
# print(board)
# print(order)


# N, M = 5, 4
# board = [[0, 0, 1, 0, 2], [2, 3, 2, 1, 0], [4, 3, 2, 9, 0], [1, 0, 2, 9, 0], [8, 8, 2, 1, 0]]
# order = [[-1, 0, 3], [0, -1, 4], [-1, 1, 1], [1, -1, 8]]


# 1. 모든 구름 이동
# 2. 물동이 +1
# 3. 증발
# 4. 양동이 대각선 물동이 개수만큼 증가
# 5. 구름 증발 제외 구름 생성


cloud = [[0, N-1], [1, N-1], [0, N-2], [1, N-2]]


def move_cloud(orderr):
    global cloud

    for ii in range(len(cloud)):
        cloud[ii][0] += (orderr[0] * orderr[2])
        cloud[ii][1] += (orderr[1] * orderr[2])

        cloud[ii][0] %= N
        cloud[ii][1] %= N


def water_copy():
    global cloud, board

    for cllx, clly in cloud:

        tot = 0
        if clly < N-1 and cllx < N-1 and board[clly+1][cllx+1] != 0:
            tot += 1
        if clly > 0 and cllx > 0 and board[clly-1][cllx-1] != 0:
            tot += 1
        if clly > 0 and cllx < N-1 and board[clly-1][cllx+1] != 0:
            tot += 1
        if cllx > 0 and clly < N-1 and board[clly+1][cllx-1] != 0:
            tot += 1

        board[clly][cllx] += tot



def create_cloud():
    global board, cloud

    prev_cloud = len(cloud)

    for x, y in cloud:
        board[y][x] *= -1

    for x in range(N):
        for y in range(N):
            if board[y][x] >= 2:
                board[y][x] -= 2
                cloud.append([x, y])

    for _ in range(prev_cloud):
        tx, ty = cloud.pop(0)
        board[ty][tx] *= -1


for ord in order:
    # 1. 모든 구름 이동
    move_cloud(ord)


    # 2. 물동이 +1
    for clx, cly in cloud:
        board[cly][clx] += 1

    # 4. 양동이 대각선 물동이 개수만큼 증가
    water_copy()


    # 5. 구름 증발 제외 구름 생성
    # 3. 기존 구름 증발
    create_cloud()


    # for i in board:
    #     print(i)
    # print(cloud)


# 점수 구하기
score = 0
for i in range(N):
    for j in range(N):
        score += board[i][j]

print(score)









