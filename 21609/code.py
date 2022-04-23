import copy

board = []
mem = []
zeros = []

N, M = input().split(" ")
N, M = int(N), int(M)

for i in range(N):
    tmp = []
    tmpp = []
    inp = input().split(" ")

    for j in range(N):
        tmp.append(int(inp[j]))
        tmpp.append(False)

    board.append(tmp)
    mem.append(tmpp)


# N, M = 5, 3
# # board = [[2, 2, -1, 3, 1], [3, 3, 2, 0, -1], [0, 0, -1, 1, 2], [-1, 3, 1, 3, 2], [0, 3, 2, 2, 1]]
# board = [[2, 2, -1, 3, 1], [3, 3, 2, 0, -1], [0, 0, 0, 1, 2], [-1, 3, 1, 3, 2], [0, 3, 2, 2, 1]]
# mem = [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]

# N, M = 6, 4
# board = [[2, 3, 1, 0, -1, 2], [2, -1, 4, 1, 3, 3], [3, 0, 4, 2, 2, 1], [-1, 4, -1, 2, 3, 4], [3, -1, 4, 2, 0, 3], [1, 2, 2, 2, 2, 1]]
# mem = [[False, False, False, False, False, False], [False, False, False, False, False, False], [False, False, False, False, False, False], [False, False, False, False, False, False], [False, False, False, False, False, False], [False, False, False, False, False, False]]


tmpmem = copy.deepcopy(mem)

group_q = []

score = 0


# -1: 검은색 (블록)
# 0: 무지개 (조커)
# M: 블록 색
# -10: 빈칸


# 1. 그룹핑
def find_group():

    global gsize, mem, znum, tmpmem, zeros

    zeros.clear()
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                zeros.append((i, j))

    group_q.clear()

    # 인접 블록 있으면 그룹핑 시작
    for ii in range(N):
        for j in range(N):
            if board[ii][j] == -1 or board[ii][j] == -10 or board[ii][j] == 0:
                continue

            near = 0

            if ii >= 1 and (board[ii - 1][j] == board[ii][j] or board[ii - 1][j] == 0):
                near += 1
            if j >= 1 and (board[ii][j - 1] == board[ii][j] or board[ii][j - 1] == 0):
                near += 1
            if ii < N - 1 and (
                board[ii + 1][j] == board[ii][j] or board[ii + 1][j] == 0
            ):
                near += 1
            if j < N - 1 and (
                board[ii][j + 1] == board[ii][j] or board[ii][j + 1] == 0
            ):
                near += 1

            if near > 0:
                dfs(ii, j, board[ii][j], False)

            if gsize != 0:
                group_q.append((ii, j, gsize, znum))
            gsize = 0
            znum = 0

            # 숨겨진..? 문제조건
            # 무지개 블록은 여러 그룹에 포함될 수 있음 ☆☆☆☆
            zero_init()

    mem = copy.deepcopy(tmpmem)


# 숨겨진..? 문제조건
# 무지개 블록은 여러 그룹에 포함될 수 있음 ☆☆☆☆
def zero_init():
    for t in zeros:
        mem[t[0]][t[1]] = False


gsize = 0
znum = 0


def dfs(x: int, y: int, target: int, isd: bool):

    global gsize, znum, N

    # 1. 이미 그룹이면 return
    #
    # 3-1. 자기가 0이거나 타겟 숫자면?
    #     mem true
    #     상하좌우 보냄
    # 3-2. 아니면 return

    if mem[x][y]:
        return

    if board[x][y] == target or board[x][y] == 0:

        # 블록 삭제
        if isd:
            board[x][y] = -10
        else:
            mem[x][y] = True
            gsize += 1
            if board[x][y] == 0:
                znum += 1

        if x >= 1:
            # print("111")
            dfs(x - 1, y, target, isd)
        if y >= 1:
            # print("222")
            dfs(x, y - 1, target, isd)
        if x < N - 1:
            # print("333")
            dfs(x + 1, y, target, isd)
        if y < N - 1:
            # print("444")
            dfs(x, y + 1, target, isd)
    return


def find_big_group_idx():

    maxi = -10
    maxz = -10
    maxz_idx = -1

    ia = []
    za = []

    # 우선순위 재졍렬 ☆☆
    group_q.sort(key=lambda x: x[1], reverse=True)
    group_q.sort(key=lambda x: x[0], reverse=True)

    for _, _, i, z in group_q:
        ia.append(i)
        za.append(z)
        if maxi < i:
            maxi = i

    # 없는 경우
    if len(ia) == 0:
        return -1

    # 동일 그룹 사이즈가 여러개인 경우
    elif ia.count(maxi) > 1:

        st_idx = 0
        idxs = []

        for k in range(ia.count(maxi)):
            st_idx = ia.index(maxi, st_idx, len(ia))
            idxs.append(st_idx)
            st_idx += 1

        for k in idxs:
            z = za[k]
            if maxz < z:
                maxz = z
                maxz_idx = k

    else:
        maxz_idx = ia.index(maxi)

    return maxz_idx


def gravity():

    global N

    for j in range(N):
        inp = []
        tmpp = []

        for i in range(N):
            inp.append(board[i][j])

        # -1 벽 고정
        wq = []
        wallnum = inp.count(-1)
        if wallnum != 0:
            st_idx = 0

            for k in range(wallnum):
                st_idx = inp.index(-1, st_idx, N)
                wq.append(st_idx)
                st_idx += 1

        prev_wall = 0

        for wall in wq:
            ttt = []
            for k in range(prev_wall, wall):
                ttt.append(inp[k])

            if ttt.count(-1) != 0:
                ttt.remove(-1)
            tmpp.append(ttt)
            prev_wall = wall

        ttt = []
        for k in range(prev_wall, N):
            ttt.append(inp[k])

        if ttt.count(-1) != 0:
            ttt.remove(-1)
        tmpp.append(ttt)

        # 최종 제작
        for i in range(len(tmpp)):
            tmpp[i]
            blanknum = tmpp[i].count(-10)
            if blanknum != 0:
                for k in range(blanknum):
                    tmpp[i].remove(-10)
                for k in range(blanknum):
                    tmpp[i].insert(0, -10)

        result = []
        for i in tmpp:
            for k in i:
                result.append(k)
            result.append(-1)
        result.pop(len(result) - 1)

        # 적용
        for i in range(N):
            board[i][j] = result[i]


def rotate():

    global board, N
    target1 = []
    target2 = []

    # 좌우대칭
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(board[i][N - j - 1])
        target1.append(tmp)

    # 시메트릭
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(target1[j][i])
        target2.append(tmp)

    board = copy.deepcopy(target2)


score = 0


# 아... ☆☆☆☆☆
# for i in range(0, 10)
while True:

    # for i in board:
    #     print(i)

    # 2. 가장 큰 그룹 찾기 (기준을 저장)
    find_group()
    result_idx = find_big_group_idx()
    # print(group_q)

    # print(result_idx)

    if result_idx == -1:
        print(score)
        break

    max_group = group_q[result_idx]

    # 3. 빈칸으로 바꿈 (-10) / 칸 개수^2 -> 점수
    score += max_group[2] * max_group[2]
    dfs(max_group[0], max_group[1], board[max_group[0]][max_group[1]], True)

    # 4. 중력
    gravity()

    # 5. 반시계 회전 (좌우대칭 / 시메트릭 대칭)
    rotate()

    # 6. 중력
    gravity()

    # print(score)
    # print("=========")
