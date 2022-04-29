import math
import sys
sys.stdin = open("sample.txt", "r")


class Dirr:
    up = 1
    right = 2
    down = 3
    left = 4



T = int(input())


for ttttt in range(T):


    M, A = input().split()
    M = int(M)
    A = int(A)

    pmove = []
    ploc = [[0, 0], [9, 9]]

    aploc = []
    aprange = []
    appower = []


    for k in range(2):
        atmp = input().split()
        ttt = []
        for i in atmp:
            ttt.append(int(i))
        # 마지막 이동하고나서 점수 안구함...
        ttt.append(0)
        pmove.append(ttt)

    for i in range(A):
        atmp = input().split()
        # 반대...!
        aploc.append([int(atmp[1]) - 1, int(atmp[0]) - 1])
        aprange.append(int(atmp[2]))
        appower.append(int(atmp[3]))



    # 1. 도달 기지국 검색
    # 2. 기지국 배정 (겹치는 거 없앰)
    # 3. 점수 계산
    # 4. A, B 움직임

    score = 0

    for idx in range(len(pmove[0])):
        # print("#", idx)
        # print(ploc)
        # print(pmove[0][idx], pmove[1][idx])

        # 1. 도달 기지국 검색
        reachedq = []

        pn = 0
        for p in ploc:
            for app in range(len(aploc)):
                dist = int(math.fabs(aploc[app][0] - p[0])) + int(math.fabs(aploc[app][1] - p[1]))
                # print(dist, " / ", aploc[app][0], p[0], aploc[app][1], p[1])
                if dist <= aprange[app]:
                    reachedq.append([pn, app, appower[app]])
            pn += 1

        # 2. 기지국 배정 (겹치는 거 없앰)
        # 2-1. 파워 순으로 정렬
        # 2-2. 제일 높은 파워 순으로 배정
        # 겹치는 구역이 제일 적은 놈부터 높은거 배정
        # 같이 같은 기지국 쓰는 경우, 반으로 나눠가짐!

        score1 = 0
        score2 = 0

        rq1 = []
        rq2 = []
        score1 = 0
        targa1 = 0
        targp1 = 0
        score2 = 0
        targa2 = 0
        targp2 = 0

        if len(reachedq) != 0:

            # 그냥 둘 다 계산해서 큰거로 가져가야할듯
            reachedq.sort(key=lambda x: x[2], reverse=True)
            # if dup[0] > dup[1]:
            reachedq.sort(key=lambda x: x[0], reverse=True)
            rq1 = [i for i in reachedq]
            score1 += rq1[0][2]
            targp1 = rq1[0][0]
            targa1 = rq1[0][1]
            # print(rq1)

            reachedq.sort(key=lambda x: x[0], reverse=False)
            rq2 = [i for i in reachedq]

            score2 += rq2[0][2]
            targp2 = rq2[0][0]
            targa2 = rq2[0][1]

            # print(rq2)

            # print(reachedq[0][2], end=" / ")

        # else:
            # print(0, end=" / ")


        # 3. 점수 계산
        ppp = 0
        while ppp < len(rq1):
            if targp1 == rq1[ppp][0] or targa1 == rq1[ppp][1]:
                rq1.pop(ppp)
            else:
                ppp += 1
        if len(rq1) != 0:
            score1 += rq1[0][2]

        ppp = 0
        while ppp < len(rq2):
            if targp2 == rq2[ppp][0] or targa2 == rq2[ppp][1]:
                rq2.pop(ppp)
            else:
                ppp += 1
        if len(rq2) != 0:
            score2 += rq2[0][2]

        if len(reachedq) != 0:
            score += max(score1, score2)
            # print(score1, score2)


        # 4. A, B 움직임
        for p in range(2):
            if pmove[p][idx] == Dirr.left:
                ploc[p][1] -= 1
            elif pmove[p][idx] == Dirr.right:
                ploc[p][1] += 1
            elif pmove[p][idx] == Dirr.down:
                ploc[p][0] += 1
            elif pmove[p][idx] == Dirr.up:
                ploc[p][0] -= 1

        # print(score)
        # print()

    print("#" + str(ttttt+1), score)

