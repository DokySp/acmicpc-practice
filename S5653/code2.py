
import sys
sys.stdin = open("sample.txt", "r")


T = int(input())



def printb():
    global board
    for kk in board:
        for kkk in kk:
            print("%5d" % kkk, end=" ")
        print()
    print()

for ttttt in range(T):

    N, M, K = input().split()
    N = int(N)
    M = int(M)
    K = int(K)

    board = []

    for i in range(N):
        tmp = []
        inp = input().split()

        # 빈칸 -> 0
        # 생명력 -> 0~9 수정 (0도 카운트 해야 함!!)
        # 생명력 -> 상태(1, 2, 3, 4) / 본래 생명력(2) / 현재 생명력(2)
        # 상태: 2: 비활성 / 1: 임시 비활성(덮어쓰기 가능) / 3: 활성 / 4: 사망
        for j in inp:
            ttmp = int(j)
            if ttmp != 0:
                # 생명력
                ttmp += ttmp * 100
                # 상태
                ttmp += 20000
            else:
                ttmp = 0
            tmp.append(ttmp)
        board.append(tmp)

    # 상하좌우로 K개만큼 늘림 (최대 350)
    pad = 175 - int(min(N,M) / 2)



    for kk in range(len(board)):
        for kkk in range(pad):
            board[kk].append(0)
            board[kk].insert(0, 0)
    for kk in range(pad):
        # 배열복사 조심해서 쓰기.. (포인터 공유 문제)
        padarr = [0 for _ in range(pad * 2 + len(range(0)) + M)]
        board.append(padarr)
        padarr = [0 for _ in range(pad * 2 + len(range(0)) + M)]
        board.insert(0, padarr)

    newN = len(board)
    newM = len(board[0])

    # printb()



    for time in range(K):

        createq = []

        for i in range(1, newN-1):
            for j in range(1, newM-1):

                # 1. 모든 세포들 생명력 -1
                if board[i][j] != 0 and board[i][j] != 40000:
                    board[i][j] -= 1

                target = board[i][j]


                stat = int(target / 10000)
                X = int(target / 100) % 100
                currX = target % 100


                # 2. 2XX00
                #   2-1. 3XXXX로 변경
                if target != 0 and stat == 2 and currX == 0:
                    board[i][j] = 30000 + X * 100 + X
                    # print("활성!")

                # 3. 3(X)(X-1)
                #   2-2. 동서남북 확장
                #   2-3. 경계인 경우, board 확장

                elif target != 0 and stat == 3 and X == currX + 1:
                    # print("번식!")

                    x = 0
                    y = 0

                    for kkk in range(4):

                        if kkk == 0:
                            x = 1
                        elif kkk == 1:
                            x = -1
                        elif kkk == 2:
                            x = 0
                            y = 1
                        elif kkk == 3:
                            y = -1

                        ttarget = board[i + x][j + y]
                        tstat = int(ttarget / 10000)
                        tX = int(ttarget / 100) % 100

                        if tstat == 0 or (tstat == 1 and tX < X):
                            # 탐색 진행 방향인 경우 + 1
                            if x == 1 or y == 1:
                                board[i+x][j+y] = 10000 + X * 100 + X + 1
                            else:
                                board[i+x][j+y] = 10000 + X * 100 + X
                            createq.append([i+x, j+y])

                    # 생명력 1인 경우 바로 죽임
                    if X == 1:
                        board[i][j] = 40000

                # 3. 3X0 -> 400으로 변경
                elif target != 0 and stat == 3 and currX == 0:
                    board[i][j] = 40000
                    # print("사망!")

        for xx, yy in createq:
            ttstat = int(board[xx][yy] / 10000)
            if ttstat == 1:
                board[xx][yy] += 10000


        # printb()

    score = 0

    for i in range(newN):
        for j in range(newM):
            stat = int(board[i][j] / 10000)
            if stat == 2 or stat == 3:
                score += 1

    print("#" + str(ttttt+1), score)

    # printb()