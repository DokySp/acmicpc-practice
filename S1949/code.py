
import sys
sys.stdin = open("sample.txt", "r")

import copy

T = int(input())


# 메모이제이션을 제대로 안해서 오류가 났었음!!!

# 현재 값, 좌표, k사용가능 여부, 지금까지 길이, memoization table, 디버깅용 트레이싱 문자열
def dfs(curr, i, j, is_k, len, memtable, bef):
    global board, K, maxlen
    # 주변 지형 중 자기보다 낮은 곳으로 보냄
    # 만약 지형이 같거나 높고, k 쓸 수 있으면 1~K만큼 깎은 후 진행

    # print(bef)

    # 위
    if i >= 1 and not memtable[i-1][j]:
        if board[i-1][j] < curr:
            mt = copy.deepcopy(memtable)
            mt[i-1][j] = True
            dfs(board[i-1][j], i-1, j, is_k, len + 1, mt, bef + "->" + str(board[i-1][j]))
        elif is_k:
            for kk in range(1, K+1):
                if board[i - 1][j] - kk < curr:
                    mt = copy.deepcopy(memtable)
                    mt[i - 1][j] = True
                    dfs(board[i-1][j] - kk, i-1, j, False, len + 1, mt, bef + "->" + str(board[i-1][j]) + "("+str(kk)+")")
    # 아래
    if i < N - 1 and not memtable[i+1][j]:
        if board[i+1][j] < curr:
            mt = copy.deepcopy(memtable)
            mt[i + 1][j] = True
            dfs(board[i+1][j], i+1, j, is_k, len + 1, mt, bef + "->" + str(board[i+1][j]))
        elif is_k:
            for kk in range(1, K+1):
                if board[i + 1][j] - kk < curr:
                    mt = copy.deepcopy(memtable)
                    mt[i + 1][j] = True
                    dfs(board[i+1][j] - kk, i+1, j, False, len + 1, mt, bef + "->" + str(board[i+1][j]) + "("+str(kk)+")")
    # 오른쪽
    if j < N - 1 and not memtable[i][j+1]:
        if board[i][j + 1] < curr:
            mt = copy.deepcopy(memtable)
            mt[i][j+1] = True
            dfs(board[i][j+1], i, j + 1, is_k, len + 1, mt, bef + "->" + str(board[i][j+1]))
        elif is_k:
            for kk in range(1, K + 1):
                if board[i][j + 1] - kk < curr:
                    mt = copy.deepcopy(memtable)
                    mt[i][j + 1] = True
                    dfs(board[i][j+1] - kk, i, j + 1, False, len + 1, mt, bef + "->" + str(board[i][j+1]) + "("+str(kk)+")")
    # 왼쪽
    if j >= 1 and not memtable[i][j - 1]:
        if board[i][j - 1] < curr:
            mt = copy.deepcopy(memtable)
            mt[i][j-1] = True
            dfs(board[i][j-1], i, j - 1, is_k, len + 1, mt, bef + "->" + str(board[i][j-1]))
        elif is_k:
            for kk in range(1, K + 1):
                if board[i][j-1] - kk < curr:
                    mt = copy.deepcopy(memtable)
                    mt[i][j - 1] = True
                    dfs(board[i][j-1] - kk, i, j - 1, False, len + 1, mt, bef + "->" + str(board[i][j-1]) + "("+str(kk)+")")

    if maxlen < len:
        maxlen = len

    return



def find_highest():

    global board, N

    maxx = -1

    for i in board:
        tm = max(i)
        if tm > maxx:
            maxx = tm
    res = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == maxx:
                res.append([i, j])
    return res


for ttttt in range(T):

    N, K = input().split()

    N = int(N)
    K = int(K)

    board = []

    for i in range(N):
        inp = input().split()
        tmp = []
        for t in inp:
            tmp.append(int(t))
        board.append(tmp)

    startq = []

    # 1. 가장 높은 봉우리 위치 찾기
    # 2. 낮은 방향으로 탐색 (DFS)
    # 3. 만약 지형이 같거나 높다면 1~K만큼 깎은 후 진행


    # 1. 가장 높은 봉우리 위치 찾기
    startq = find_highest()
    maxlen = 0

    # 2. 낮은 방향으로 탐색 (DFS)
    for ii, jj in startq:
        memtable = [[False for _ in range(N)] for _ in range(N)]
        memtable[ii][jj] = True
        dfs(board[ii][jj], ii, jj, is_k=True, len=1, memtable=memtable, bef=str(board[ii][jj]))

    print("#" + str(ttttt+1), maxlen)
