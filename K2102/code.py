import copy


class Dirr:
    up = 0
    right = 1
    down = 2
    left = 3


board = []


def dfs(i, j, dirr, depth, memtable):

    global board

    # 특별한 경우가 아니라면 메모이제이션 하기!!
    memt = copy.deepcopy(memtable)

    # print(i, j, depth, board[i][j])

    memt[i][j] = True

    if depth != 0 and board[i][j] == "P":
        return 1

    if depth >= 2 and board[i][j] != "P":
        return 0

    if board[i][j] == "X":
        return 0

    sum = 0

    # 실수로 elif로 돌림...
    if i >= 1 and dirr != Dirr.down and not memt[i - 1][j]:
        sum += dfs(i - 1, j, Dirr.up, depth + 1, memt)

    if i <= 3 and dirr != Dirr.up and not memt[i + 1][j]:
        sum += dfs(i + 1, j, Dirr.down, depth + 1, memt)

    if j <= 3 and dirr != Dirr.left and not memt[i][j + 1]:
        sum += dfs(i, j + 1, Dirr.right, depth + 1, memt)

    if j >= 1 and dirr != Dirr.right and not memt[i][j - 1]:
        sum += dfs(i, j - 1, Dirr.left, depth + 1, memt)

    return sum


def solution(places):
    global board

    # DFS로 거리 2 이내 사람이 있는지 확인 (넘으면 Fail)
    # 중간에 벽 있으면 Fail

    answer = []

    for p in places:
        board = p
        result = 0
        for i in range(5):
            for j in range(5):

                # print(board[i][j], i, j)

                if board[i][j] == "P":
                    memtable = [[False for _ in range(5)] for _ in range(5)]
                    result += dfs(i, j, Dirr.up, 0, memtable)
                    result += dfs(i, j, Dirr.down, 0, memtable)
                    result += dfs(i, j, Dirr.left, 0, memtable)
                    result += dfs(i, j, Dirr.right, 0, memtable)

                # print(result)
                # print("================")

        if result != 0:
            answer.append(0)
        else:
            answer.append(1)
        # print(answer)
        # print("================================================================")

    return answer


print(
    solution(
        [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
            ["OOOXX", "XOOOX", "PPPXX", "OXOOX", "OOOOO"],
        ]
    )
)
