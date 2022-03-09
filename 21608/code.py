
stdNum = []
stdArr = []
classroom = []
available = []


# 입력
N = int(input())

for i in range(N*N):
    stdN, l1, l2, l3, l4 = input().split(" ")
    stdNum.append(int(stdN))
    stdArr.append([int(l1), int(l2), int(l3), int(l4)])

# N = 3
# stdNum = [4, 3, 9, 8, 7, 1, 6, 5, 2]
# stdArr = [[2, 5, 1, 7], [1, 9, 4, 5], [8, 1, 2, 3], [1, 9, 3, 4], [2, 3, 4, 8], [9, 2, 5, 7], [5, 2, 3, 4], [1, 9, 2, 8], [9, 3, 1, 4]]

# 완전탐색 오류 반례
# N = 3
# stdNum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# stdArr = [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9, 1], [8, 9, 1, 2], [9, 1, 2, 3], [1, 2, 3, 4]]


# 2차원 배열 생성
for i in range(N):
    classroom.append([])
    available.append([])
    for j in range(N):
        classroom[i].append(0)
        available[i].append(0)


# 이웃 누구 있는지 추출
def get_neighbors_arr(x, y):

    returnArr = []
    zero_count = 0

    if x-1 >= 0:
        returnArr.append(classroom[x-1][y])
        if classroom[x-1][y] == 0:
            zero_count += 1
    else:
        returnArr.append(0)

    if x+1 < N:
        returnArr.append(classroom[x+1][y])
        if classroom[x+1][y] == 0:
            zero_count += 1
    else:
        returnArr.append(0)

    if y-1 >= 0:
        returnArr.append(classroom[x][y-1])
        if classroom[x][y-1] == 0:
            zero_count += 1
    else:
        returnArr.append(0)

    if y+1 < N:
        returnArr.append(classroom[x][y+1])
        if classroom[x][y+1] == 0:
            zero_count += 1
    else:
        returnArr.append(0)

    return returnArr, zero_count


# 완전탐색인데 불필요한 범위를 제한해서 문제를 틀림..
# def check_available(x, y):
#     available[x][y] = 0
#
#     if y - 1 >= 0 and classroom[x][y - 1] == 0:
#         available[x][y - 1] = 1
#
#     if y + 1 < N and classroom[x][y + 1] == 0:
#         available[x][y + 1] = 1
#
#     if x + 1 < N and classroom[x + 1][y] == 0:
#         available[x + 1][y] = 1
#
#     if x - 1 >= 0 and classroom[x - 1][y] == 0:
#         available[x - 1][y] = 1


# code
for i in range(N*N):

    # 첫 번째 사람은 무조건 1,1에 배치
    if i == 0:
        classroom[1][1] = stdNum[i]
        continue

    # 1. 인접 칸에 좋아하는 친구 찾기
    friend_count_max = -1

    resultX = []
    resultY = []
    resultFriend = []

    # 탐색 가능한 영역 확인
    for m in range(N):
        for n in range(N):
            # 완전탐색인데 불필요한 범위를 제한해서 문제를 틀림..
            # if available[m][n] == 1:
            if classroom[m][n] == 0:

                compArr, zero_count = get_neighbors_arr(m, n)

                friend_count = 0

                for comp in compArr:
                    if stdArr[i].count(comp) > 0:
                        friend_count += 1

                resultX.append(m)
                resultY.append(n)
                resultFriend.append(friend_count)

    # 자리 배치 전 선택
    mv = -1
    zero_max = -1

    zero_list = []

    # for k in resultFriend:
    #     if mv < k:
    #         mv = k
    mv = max(resultFriend)
    

    for idx in range(len(resultFriend)):
        _, zero_count = get_neighbors_arr(resultX[idx], resultY[idx])
        zero_list.append(zero_count)

    for idx in range(len(resultFriend)):
        if resultFriend[idx] == mv:
            if zero_max < zero_list[idx]:
                zero_max = zero_list[idx]



    for idx in range(len(resultFriend)):
        if resultFriend[idx] == mv and zero_list[idx] == zero_max:
            maxX = resultX[idx]
            maxY = resultY[idx]
            break

    # 자리 등록
    classroom[maxX][maxY] = stdNum[i]


# 점수계산
total_score = 0

for m in range(N):
    for n in range(N):

        friend_count = 0
        compArr, _ = get_neighbors_arr(m, n)

        for comp in compArr:
            if stdArr[  stdNum.index(classroom[m][n])  ].count(comp) > 0:
                friend_count += 1

        score = 0

        for i in range(friend_count):
            score *= 10
            if i == 0: score = 1
        total_score += score


# 결과 출력
# print(classroom)
print(total_score)
