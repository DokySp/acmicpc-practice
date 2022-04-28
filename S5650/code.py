
import sys
sys.stdin = open("sample.txt", "r")


class Block:
    L = 1
    F = 2
    R = 3
    J = 4
    square = 5

    blackhole = -1

    # 구현 시 필요없는 부분 지우기!!
    # wormhole = 6 # 6 ~10




T = int(input())


def move_ball_from_to(i, j, holenum):
    global board, wormhole, wormholen

    fi = wormholen.index(holenum)
    si = wormholen.index(holenum, fi + 1)

    whf = wormhole[fi]
    whs = wormhole[si]

    if whf[0] == i and whf[1] == j:
        return whs
    else:
        return whf


for ttttt in range(T):

    N = int(input())

    board = []
    wormhole = []
    wormholen = []

    for i in range(N):
        inp = input().split()
        tmp = []
        j = 0
        for kk in inp:
            tt = int(kk)
            if 6 <= tt <= 10:
                wormhole.append([i, j])
                wormholen.append(tt)
            tmp.append(tt)
            j += 1

        board.append(tmp)



    # for kkk in board:
    #     print(kkk)
    # print()


    # 임의 핀볼 위치, 진행방향 선정

    max = -1

    for ii in range(N):
        for jj in range(N):

            if board[ii][jj] != 0:
                continue

            for dirr in range(4):

                score = 0

                if dirr == 0:
                    dx = 1
                    dy = 0
                elif dirr == 1:
                    dx = 0
                    dy = 1
                elif dirr == 2:
                    dx = -1
                    dy = 0
                elif dirr == 3:
                    dx = 0
                    dy = -1

                st_point = [ii, jj]
                i = st_point[0]
                j = st_point[1]

                # print(i, j, dx, dy, st_point)

                while True:
                    i += dy
                    j += dx

                    # print(i, j ,"/" ,dx, dy)

                    if i == st_point[0] and j == st_point[1]:
                        # print("turnback!!")
                        break

                    elif i >= N or j >= N or i < 0 or j < 0:
                        score += 1
                        # print("Wall")

                        if i >= N:
                            i = N
                        elif j >= N:
                            j = N
                        elif i < 0:
                            i = -1
                        elif j < 0:
                            j = -1
                        dx = -dx
                        dy = -dy

                    elif board[i][j] == Block.blackhole:
                        # print("blackhole!!")
                        break

                    elif board[i][j] == Block.L:
                        score += 1

                        # print("L")
                        if dx == 1 and dy == 0:
                            dx = -1
                        elif dx == -1 and dy == 0:
                            dx = 0
                            dy = -1
                        elif dx == 0 and dy == 1:
                            dx = 1
                            dy = 0
                        elif dx == 0 and dy == -1:
                            dx = 0
                            dy = 1

                    elif board[i][j] == Block.J:
                        score += 1

                        # print("J")
                        if dx == 1 and dy == 0:
                            dx = 0
                            dy = -1
                        elif dx == -1 and dy == 0:
                            dx = 1
                            dy = 0
                        elif dx == 0 and dy == 1:
                            dx = -1
                            dy = 0
                        elif dx == 0 and dy == -1:
                            dx = 0
                            dy = 1

                    elif board[i][j] == Block.R:
                        score += 1

                        # print("R")
                        if dx == 1 and dy == 0:
                            dx = 0
                            dy = 1
                        elif dx == -1 and dy == 0:
                            dx = 1
                            dy = 0
                        elif dx == 0 and dy == 1:
                            dx = 0
                            dy = -1
                        elif dx == 0 and dy == -1:
                            dx = -1
                            dy = 0

                    elif board[i][j] == Block.F:
                        score += 1

                        # print("F")
                        if dx == 1 and dy == 0:
                            dx = -1
                        elif dx == -1 and dy == 0:
                            dx = 0
                            dy = 1
                        elif dx == 0 and dy == 1:
                            dx = 0
                            dy = -1
                        elif dx == 0 and dy == -1:
                            dx = 1
                            dy = 0

                    elif board[i][j] == Block.square:
                        score += 1

                        # print("Sq")
                        dx = -dx
                        dy = -dy

                    # 실수....
                    # board[i][j] == Block.wormhole:
                    elif 6 <= board[i][j] <= 10:
                        # print("WH")
                        i, j = move_ball_from_to(i, j, board[i][j])


                # print("score", score)
                if score > max:
                    max = score

    print("#" + str(ttttt+1), max)
