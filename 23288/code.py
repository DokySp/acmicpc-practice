import copy

N, M, K = input().split(" ")
N, M, K = int(N), int(M), int(K)

board = []
mem = []

for i in range(N):
    tmp = []
    tmpp = []
    inp = input().split(" ")

    for t in inp:
        tmp.append(int(t))
        tmpp.append(0)

    board.append(tmp)
    mem.append(tmpp)


# N, M, K = 4, 5, 3
# board = [[4, 1, 2, 3, 3], [6, 1, 1, 3, 3], [5, 6, 1, 3, 2], [5, 5, 6, 5, 5]]
# mem = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


class Dice:
    dx = 0
    dy = 0
    px = 0
    py = 0


tmpmem = copy.deepcopy(mem)

# n, n+2번째를 바꿔줌!
dicx = [1, 3, 6, 4]
dicy = [1, 5, 6, 2]

dice = Dice()
direction = 0


def sync_x4y():
    dicx[dice.dx] = dicy[dice.dy]
    dicx[(dice.dx + 2) % 4] = dicy[(dice.dy + 2) % 4]


def sync_y4x():
    dicy[dice.dy] = dicx[dice.dx]
    dicy[(dice.dy + 2) % 4] = dicx[(dice.dx + 2) % 4]


def move_dice():

    global direction

    # 위
    if direction == 3:
        if dice.py == 0:  # 튕겨서 아래
            direction = (direction + 2) % 4
            dice.py = 1
            dice.dy = (dice.dy - 1) % 4
            sync_x4y()

        else:
            dice.py -= 1
            dice.dy = (dice.dy + 1) % 4
            sync_x4y()

    # 아래
    elif direction == 1:
        if dice.py == N - 1:  # 튕겨서 위

            # 방향이 바뀐다는 조건!!!
            direction = (direction + 2) % 4

            dice.py = N - 2
            dice.dy = (dice.dy + 1) % 4
            sync_x4y()

        else:
            dice.py += 1
            dice.dy = (dice.dy - 1) % 4
            sync_x4y()

    # 왼쪽
    elif direction == 2:
        if dice.px == 0:  # 튕겨서 오른쪽
            direction = (direction + 2) % 4
            dice.px = 1
            dice.dx = (dice.dx - 1) % 4
            sync_y4x()
        else:
            dice.px -= 1
            dice.dx = (dice.dx + 1) % 4
            sync_y4x()

    # 오른쪽
    elif direction == 0:
        if dice.px == M - 1:  # 튕겨서 왼쪽
            direction = (direction + 2) % 4
            dice.px = M - 2
            dice.dx = (dice.dx + 1) % 4
            sync_y4x()

        else:
            dice.px += 1
            dice.dx = (dice.dx - 1) % 4
            sync_y4x()


total = 0


def dfs(px: int, py: int, target: int):

    global total

    # 1. 만약 자기 위치 mem True 이면
    #     1-1. return

    # 2. 자기 위치 mem 기록

    # 3. 만약 자기 위치가 타겟 숫자면
    #     3-1. sum++
    #     3-2. 동서남북 dfs

    # 4. 아니면 return

    if mem[py][px]:
        return

    mem[py][px] = True

    if board[py][px] == target:
        total += 1

        if px <= M - 2:
            dfs(px + 1, py, target)
        if px >= 1:
            dfs(px - 1, py, target)
        if py <= N - 2:
            dfs(px, py + 1, target)
        if py >= 1:
            dfs(px, py - 1, target)

        return
    else:
        return


def calc_score():

    global total
    global mem

    # B 계산
    B = board[dice.py][dice.px]
    C = 0

    # print("바닥:", B)
    dfs(dice.px, dice.py, B)
    C = total
    total = 0
    mem = copy.deepcopy(tmpmem)
    # print("C:", C)

    # C 계산 (DFS)
    # if 0 < dice.py and dice.py < N - 1:
    #     C += 2
    # else:
    #     C += 1
    # if 0 < dice.px and dice.px < M - 1:
    #     C += 2
    # else:
    #     C += 1

    return B * C


def change_direction(is_cw):
    global direction

    if is_cw:
        direction = (direction + 1) % 4

    else:
        direction = (direction - 1) % 4


def calc_direction():

    A = dicx[(dice.dx + 2) % 4]
    B = board[dice.py][dice.px]

    if A > B:
        change_direction(True)
    elif A < B:
        change_direction(False)


score = 0

for i in range(K):

    # 1. 이동방향 구름
    move_dice()

    # 2. 도착 판 점수 계산
    score += calc_score()

    calc_direction()

    # print("==========")


print(score)
