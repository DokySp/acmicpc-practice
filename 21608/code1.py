std = []
likes = []

N = int(input())

for i in range(N * N):
    inp = input().split()
    std.append(int(inp[0]))
    tmp = []
    for k in range(1, 5):
        tmp.append(int(inp[k]))
    likes.append(tmp)

# N = 3
# std = [4, 3, 9, 8, 7, 1, 6, 5, 2]
# likes = [[2, 5, 1, 7], [1, 9, 4, 5], [8, 1, 2, 3], [1, 9, 3, 4], [2, 3, 4, 8], [9, 2, 5, 7], [5, 2, 3, 4], [1, 9, 2, 8], [9, 3, 1, 4]]
# print(std)
# print(likes)

# N = 3
# std = [4, 2, 5, 1, 7, 9, 6, 8, 3]
# likes = [[2, 5, 1, 7], [1, 9, 4, 5], [8, 1, 4, 3], [2, 9, 3, 4], [2, 3, 4, 8], [8, 4, 5, 7], [5, 2, 3, 4], [4, 9, 2, 1], [9, 2, 1, 4]]

# N = 4
# std = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# likes = [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 10], [8, 9, 10, 11], [9, 10, 11, 12], [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 10], [8, 9, 10, 11]]

# 중복조건 반례 ☆☆☆
# N = 3
# std = [2, 5, 6, 1, 7, 8, 9, 3, 4]
# likes = [[9, 3, 1, 4], [1, 9, 4, 8], [5, 2, 3, 4], [9, 2, 5, 7], [2, 3, 4, 8], [1, 9, 3, 4], [8, 1, 2, 3], [1, 9, 4, 5], [2, 5, 1, 7]]


classroom = [[0 for i in range(N)] for i in range(N)]
score = 0

# 이렇게 임시방편 쓸 경우, 아무도 좋아하는 학생이 없는 경우 처리를 못함 ☆☆☆
# classroom[1][1] = std[0]

# for i in classroom:
#     print(i)


for idx in range(0, N * N):
    # for idx in range(1,5):

    nearq = []
    nearscore = []
    emptyscore = [[0 for i in range(N)] for i in range(N)]

    for i in range(N):
        for j in range(N):

            nearcount = 0
            emptycount = 0

            # 인접인 경우 & # 반칸 개수 측정
            if i >= 1:
                if likes[idx].count(classroom[i - 1][j]) != 0:
                    nearcount += 1
                if classroom[i - 1][j] == 0:
                    emptycount += 1

            if j >= 1:
                if likes[idx].count(classroom[i][j - 1]) != 0:
                    nearcount += 1
                if classroom[i][j - 1] == 0:
                    emptycount += 1

            if i < N - 1:
                if likes[idx].count(classroom[i + 1][j]) != 0:
                    nearcount += 1
                if classroom[i + 1][j] == 0:
                    emptycount += 1

            if j < N - 1:
                if likes[idx].count(classroom[i][j + 1]) != 0:
                    nearcount += 1
                if classroom[i][j + 1] == 0:
                    emptycount += 1

            # nearscore[i][j] = nearcount
            if nearcount > 0 and classroom[i][j] == 0:
                nearq.append([i, j])
                nearscore.append(nearcount)
            emptyscore[i][j] = emptycount

            # 다른 사람 있는 경우
            # if classroom[i][j] != 0:
            #     nearscore[i][j] = -10

    if len(nearscore) == 0:
        maxnear = 0
        for i in range(N):
            for j in range(N):
                if classroom[i][j] == 0:
                    nearq.append([i, j])
                    nearscore.append(0)
    else:
        maxnear = max(nearscore)

    # print(nearq)
    # print(maxnear)
    # print(nearscore)

    if nearscore.count(maxnear) > 1:

        ## 2, 3 조건이 겹칠 때 오류 해결 ☆☆☆
        kk = 0
        while True:
            if kk >= len(nearq):
                break

            if maxnear != nearscore[kk]:

                nearscore.pop(kk)
                nearq.pop(kk)
                kk -= 1
                # print(nearscore, kk)
            kk += 1

        emtpyq = []
        for x, y in nearq:
            emtpyq.append(emptyscore[x][y])

        maxz = max(emtpyq)

        x, y = nearq[emtpyq.index(maxz)]
        classroom[x][y] = std[idx]

    else:
        x, y = nearq[nearscore.index(maxnear)]
        classroom[x][y] = std[idx]

    # for i in classroom:
    #     print(i)
    # print()


# 1. 인접 친구 점수 계산
# 2. 빈칸 점수 계산
#
# 1 조건 만족하는 위치 찾기
#    1-1 여러 개 있으면 그 중 빈칸 만족하는거 찾기
#        여러개면 제일 앞 인덱스
#
# 4. 배치
# 5. 점수는 나중에 한번에 계산 ☆☆☆

for i in range(N):
    for j in range(N):

        idx = std.index(classroom[i][j])

        scount = 0

        if i >= 1:
            if likes[idx].count(classroom[i - 1][j]) != 0:
                scount += 1

        if j >= 1:
            if likes[idx].count(classroom[i][j - 1]) != 0:
                scount += 1

        if i < N - 1:
            if likes[idx].count(classroom[i + 1][j]) != 0:
                scount += 1

        if j < N - 1:
            if likes[idx].count(classroom[i][j + 1]) != 0:
                scount += 1

        tmpscore = 0
        if scount != 0:
            tmpscore += 1
            for _ in range(scount - 1):
                tmpscore *= 10
        score += tmpscore

print(score)
