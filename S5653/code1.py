
import sys
sys.stdin = open("sample.txt", "r")


T = int(input())

for ttttt in range(T):

    N, M, K = input().split()
    N = int(N)
    M = int(M)
    K = int(K)

    board = []

    for i in range(N):
        tmp = []
        inp = input().split()

        # 빈칸 -> -1
        # 생명력 -> 0~9 수정 (0도 카운트 해야 함!!)
        # 생명력 -> 상태 / 본래 생명력 / 현재 생명력
        for j in inp:
            ttmp = int(j)
            if ttmp != 0:
                ttmp -= 1
                ttmp += ttmp * 10


                ttmp += 100
            else:
                ttmp = -1
            tmp.append(ttmp)
        board.append(tmp)


    # for kk in board:
    #     print(kk)
    # print()



    for time in range(K):

        updateq = []

        i = 0
        while i < len(board):
            j = 0
            while j < len(board[0]):

                tmp = board[i][j]
                X = (int(tmp / 10) % 10)

                # 번식
                if tmp != -1 and int(tmp / 100) == 2 and tmp % 10 == X:

                    # 좌 증폭
                    if j < 1:
                        for ii in range(len(board)):
                            board[ii].insert(0, -1)
                        j += 1
                    # 우 증폭
                    if j >= len(board[0]) - 1:
                        for ii in range(len(board)):
                            board[ii].append(-1)
                    # # 상 증폭
                    if i < 1:
                        tttmp = [-1 for _ in range(len(board[0]))]
                        board.insert(0, tttmp)
                        i += 1
                    # 하 증폭
                    if i >= len(board) - 1:
                        tttmp = [-1 for _ in range(len(board[0]))]
                        board.append(tttmp)

                    # 만약 기존에 있는 경우 pass
                    # 새로 생성된 세포가 있는 경우, X가 더 크면 덮음
                    x = 0
                    y = 0
                    for tt in range(4):

                        if tt == 0:
                            y = 1
                        elif tt == 1:
                            y = -1
                        elif tt == 2:
                            x = -1
                            y = 0
                        elif tt == 3:
                            x = 1

                        targ = board[i + x][j + y]
                        targ_x = (int(targ / 10) % 10)

                        # 생성 시, 재탐색 고려
                        # 100 구분을 못해냄... -> 1100으로 수정
                        # 1:41:01.52
                        if targ != -1 and targ_x == targ % 10 and targ_x < X:

                            if int(targ / 100) == 11:
                                # 생성 시 , 1 1 X X + 1
                                if x > 0 or y > 0:
                                    board[i + x][j + y] = 1100 + X * 10 + X + 1
                                # 생성 시 , 1 1 X X + 1
                                else:
                                    board[i + x][j + y] = 1100 + X * 10 + X
                                # updateq.append([i+x, j+y])

                        elif targ == -1:
                            # 생성 시 , 1 1 X X + 1
                            if x > 0 or y > 0:
                                board[i + x][j + y] = 1100 + X * 10 + X + 1
                            # 생성 시 , 1 1 X X + 1
                            else:
                                board[i + x][j + y] = 1100 + X * 10 + X
                            # updateq.append([i + x, j + y])

                # 2. 1X0
                #   2-1. 2XX로 변경
                #   2-2. 동서남북 확장
                #   2-3. 경계인 경우, board 확장
                # 3. 2X0 -> 300으로 변경
                # 1. 모든 세포들 생명력 -1

                if tmp != -1 and int(tmp / 100) == 1 and tmp % 10 == 0:
                    # 비활성 -> 활성

                    board[i][j] = 200 + X * 10 + X
                elif tmp != -1 and int(tmp / 100) == 2 and tmp % 10 == 0:
                    # 활성 -> 사망
                    board[i][j] = 300
                elif tmp == 300:
                    pass
                elif tmp != -1:
                    board[i][j] -= 1

                j += 1
            i += 1



        # 11XX인 세포들 앞에 1 제거

        # print(updateq)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if int(board[i][j] / 100) == 11:
                    board[i][j] -= 1000



        # for kk in board:
        #     for kkk in kk:
        #         print("%3d" % kkk, end=", ")
        #     print()
        # print()


    score = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            res = int(board[i][j] / 100)

            if res == 1 or res == 2:
                score += 1

    print("#" + str(ttttt+1), score, len(board), len(board[0]))






# sum = 0
# for i in range(300):
#     for k in range(422500):
#         sum += 1
# print(sum)
# 10초 정도 걸림.... 조금 위험할 듯
