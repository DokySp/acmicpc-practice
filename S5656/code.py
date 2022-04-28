# import sys
# sys.stdin = open("sample.txt", "r")

import copy

T = int(input())

def blow_blocks(iboard, iii, j):

    global W, H

    tar = iboard[iii][j]
    iboard[iii][j] = 0

    for r in range(1, tar):
        if iii + r < H:
            blow_blocks(iboard, iii + r, j)
        if iii - r >= 0:
            blow_blocks(iboard, iii - r, j)
        if j + r < W:
            blow_blocks(iboard, iii, j + r)
        if j - r >= 0:
            blow_blocks(iboard, iii, j - r)
    return



def throw_marble(iboard, w):

    global H

    for ii in range(H):
        if iboard[ii][w] != 0:
            blow_blocks(iboard, ii, w)
            break

    return iboard



def gravity(iboard):

    global W, H

    for w in range(W):
        tmp = []
        for k in range(H):
            tmp.append(iboard[k][w])

        blank = tmp.count(0)

        for _ in range(blank):
            tmp.remove(0)

        for _ in range(blank):
            tmp.insert(0, 0)

        for k in range(H-1, -1, -1):
            iboard[k][w] = tmp[k]

    return iboard



def dfs(tboard, targetw, depth):

    global W, H, min

    if(depth == 0):

        zcount = 0
        for ss in tboard:
            for sss in ss:
                if sss == 0:
                    zcount += 1
        tmin = W * H - zcount

        if min > tmin:
            min = tmin

        return

    ttboard = copy.deepcopy(tboard)

    # 1. 구슬 던짐 & 터짐
    ttboard = throw_marble(ttboard, targetw)
    # 3. 중력
    ttboard = gravity(ttboard)

    # dfs
    for kkk in range(W):
        dfs(ttboard, kkk, depth - 1)



for ttttt in range(T):

    N, W, H = input().split()
    N = int(N)
    W = int(W)
    H = int(H)

    min = W * H

    board = []

    for i in range(H):
        tmp = []
        inp = input().split()

        for k in inp:
            tmp.append(int(k))
        board.append(tmp)


    for kk in range(W):
        dfs(board, kk, N)


    # for bb in board:
    #     print(bb)
    # print()

    # for i in range(7):
    #     # 1. 구슬 던짐 & 터짐 # 3. 중력
    #     board = throw_marble(board, 3)
    #     board = gravity(board)
    #     for bb in board:
    #         print(bb)
    #     print()

    print("#" + str(ttttt+1), min)
