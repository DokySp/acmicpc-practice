

# board = [[0, 2], [3, 4], [5, 6], [7, 8]]
# controls = [4, 4, 4, 1, 3, 3, 3, 2]
#
# x = 0
# y = 0

board = []
controls = []

inp = input().split(" ")

N = int(inp[0])
M = int(inp[1])
x = int(inp[2])
y = int(inp[3])
K = int(inp[4])

for i in range(0, N):
    inp = input().split(" ")
    tmp = []
    for j in range(0, M):
        tmp.append(int(inp[j]))
    board.append(tmp)


inp = input().split(" ")

for i in range(0, K):
    controls.append(int(inp[i]))


def rotate_dice(rot):

    # 동쪽
    if rot == 1:
        tmp = dice_hor.pop()
        dice_hor.insert(0, tmp)
        dice_ver[0] = dice_hor[0]
        dice_ver[2] = dice_hor[2]

    # 서쪽
    elif rot == 2:
        tmp = dice_hor.pop(0)
        dice_hor.append(tmp)
        dice_ver[0] = dice_hor[0]
        dice_ver[2] = dice_hor[2]

    # 북쪽
    elif rot == 3:
        tmp = dice_ver.pop(0)
        dice_ver.append(tmp)
        dice_hor[0] = dice_ver[0]
        dice_hor[2] = dice_ver[2]

    # 남쪽
    elif rot == 4:
        tmp = dice_ver.pop()
        dice_ver.insert(0, tmp)
        dice_hor[0] = dice_ver[0]
        dice_hor[2] = dice_ver[2]


dice_ver = [0,0,0,0]
dice_hor = [0,0,0,0]

for ctrl in controls:

    # boundary check
    # 동쪽
    if ctrl == 1 and y >= M-1:
        continue
    # 서쪽
    elif ctrl == 2 and y <= 0:
        continue
    # 북쪽
    elif ctrl == 3 and x <= 0:
        continue
    # 남쪽
    elif ctrl == 4 and x >= N-1:
        continue


    if board[x][y] == 0:
        board[x][y] = dice_ver[0]
    else:
        dice_ver[0] = board[x][y]
        dice_hor[0] = board[x][y]
        # 뺘먹은 조건 / 나중에 찾음...
        board[x][y] = 0

    rotate_dice(ctrl)

    # 동쪽
    if ctrl == 1:
        y += 1
    # 서쪽
    elif ctrl == 2:
        y -= 1
    # 북쪽
    elif ctrl == 3:
        x -= 1
    # 남쪽
    elif ctrl == 4:
        x += 1

    print(dice_hor[2])
