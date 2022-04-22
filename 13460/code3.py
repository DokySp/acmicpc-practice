class Item:

    blank = 0
    wall = 10
    hole = 5
    red = 1
    blue = 2


class Direction:
    left = 0
    right = 1
    up = 2
    down = 3

    leftd = [-1, 0]
    rightd = [1, 0]
    upd = [0, -1]
    downd = [0, 1]


class Ball:
    x = -1
    y = -1
    color = -1


red = Ball()
blue = Ball()


N, M = input().split(" ")

N = int(N)
M = int(M)

board = []

for i in range(N):
    tmp = []
    inp = input()
    for j in range(M):

        if inp[j] == ".":
            tmp.append(Item.blank)
        elif inp[j] == "#":
            tmp.append(Item.wall)
        elif inp[j] == "O":
            tmp.append(Item.hole)
        elif inp[j] == "R":
            # tmp.append(Item.red)
            tmp.append(Item.blank)
            red.x, red.y, red.color = j, i, Item.red
        elif inp[j] == "B":
            # tmp.append(Item.blue)
            tmp.append(Item.blank)
            blue.x, blue.y, blue.color = j, i, Item.blue

    board.append(tmp)


# N, M = 7, 7
# board = [
#     [10, 10, 10, 10, 10, 10, 10],
#     [10, 0, 0, 0, 0, 0, 10],
#     [10, 0, 10, 10, 10, 10, 10],
#     [10, 0, 0, 0, 0, 0, 10],
#     [10, 10, 10, 10, 10, 0, 10],
#     [10, 5, 0, 0, 0, 0, 10],
#     [10, 10, 10, 10, 10, 10, 10],
# ]

# red.x, red.y, red.color = 4, 1, Item.red
# blue.x, blue.y, blue.color = 5, 1, Item.blue


# N, M = 3, 10
# board = [
#     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
#     [10, 0, 5, 0, 0, 0, 0, 0, 0, 10],
#     [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
# ]
# red.x, red.y, red.color = 1, 1, Item.red
# blue.x, blue.y, blue.color = 8, 1, Item.blue

# print(N, M)
# print(board)
# print(red.x, red.y)
# print(blue.x, blue.y)


def move_ball(dir: Direction, ired: Ball, iblue: Ball):

    cred, cblue = Ball(), Ball()
    cred.x, cred.y, cred.color = ired.x, ired.y, ired.color
    cblue.x, cblue.y, cblue.color = iblue.x, iblue.y, iblue.color

    # 1. 공의 위치 확인 -> 누가 먼저 굴러갈지 결정

    ball_queue = []
    dx, dy = 0, 0

    if cred.y == cblue.y and dir == Direction.left:
        dx, dy = Direction.leftd
        if cred.x < cblue.x:
            ball_queue = [cred, cblue]
        else:
            ball_queue = [cblue, cred]
    elif cred.y == cblue.y and dir == Direction.right:
        dx, dy = Direction.rightd
        if cred.x > cblue.x:
            ball_queue = [cred, cblue]
        else:
            ball_queue = [cblue, cred]
    elif cred.x == cblue.x and dir == Direction.up:
        dx, dy = Direction.upd
        if cred.y < cblue.y:
            ball_queue = [cred, cblue]
        else:
            ball_queue = [cblue, cred]
    elif cred.x == cblue.x and dir == Direction.down:
        dx, dy = Direction.downd
        if cred.y > cblue.y:
            ball_queue = [cred, cblue]
        else:
            ball_queue = [cblue, cred]

    # 위의 경우에 해당하지 않을 경우!
    if len(ball_queue) == 0:
        ball_queue = [cred, cblue]
        if dir == Direction.left:
            dx, dy = Direction.leftd
        elif dir == Direction.right:
            dx, dy = Direction.rightd
        elif dir == Direction.up:
            dx, dy = Direction.upd
        elif dir == Direction.down:
            dx, dy = Direction.downd

    # 공 굴리기
    # 만약 빠진 경우 플래그 온
    is_red_hole = False
    is_first = True
    tmp_wall = Ball()

    for cball in ball_queue:

        while not (cball.x + dx >= 0 or cball.x + dx < M) or (
            cball.y + dy >= 0 or cball.y + dy < N
        ):
            cball.x += dx
            cball.y += dy

            if board[cball.y][cball.x] == Item.wall:
                # 벽이면 되돌린 후, 첫 공인 경우 임시벽 배치 / 리턴
                cball.x -= dx
                cball.y -= dy

                if is_first:
                    tmp_wall.x = cball.x
                    tmp_wall.y = cball.y
                    board[tmp_wall.y][tmp_wall.x] = Item.wall

                is_first = False
                break
            elif board[cball.y][cball.x] == Item.hole:

                # 구멍인 경우, 무슨 공인지 체크하고
                # 파란 공 -> return
                # 빨간 공 -> is_red_hole 체크
                # is_red_hole 인데 파란공 -> return

                if cball.color == Item.red:
                    is_red_hole = True
                    is_first = False
                    break
                elif cball.color == Item.blue:
                    # 가벽 치우기
                    board[tmp_wall.y][tmp_wall.x] = Item.blank
                    # 끝 여부, 성공 여부, 빨공, 파공

                    return True, False, cred, cblue

    # 가벽 치우기
    board[tmp_wall.y][tmp_wall.x] = Item.blank

    # 끝 여부, 성공 여부, 빨공, 파공
    if is_red_hole:
        return True, True, cred, cblue
    return False, False, cred, cblue


# BFS
# 1. 두 공의 위치를 보드에서 지우고, 따로 저장한다
# 2. 이전과 동일하지 않은 각 방향별로 BFS 진행한다.


def bfs():

    prev_queue = [(red, blue, -1)]

    for depth in range(1, 11):

        pq_len = len(prev_queue)

        for _ in range(pq_len):
            cb_red, cb_blue, prev_dir = prev_queue.pop(0)

            if cb_red == -1:
                continue

            # 각 방향으로 던짐
            if prev_dir != Direction.up:
                isend, res, nred, nblue = move_ball(Direction.up, cb_red, cb_blue)

                if isend == True and res == True:
                    return depth
                elif isend == True and res == False:
                    prev_queue.append((-1, -1, -1))
                else:
                    prev_queue.append((nred, nblue, Direction.up))

            if prev_dir != Direction.down:
                isend, res, nred, nblue = move_ball(Direction.down, cb_red, cb_blue)

                if isend == True and res == True:
                    return depth
                elif isend == True and res == False:
                    prev_queue.append((-1, -1, -1))
                else:
                    prev_queue.append((nred, nblue, Direction.down))

            if prev_dir != Direction.left:
                isend, res, nred, nblue = move_ball(Direction.left, cb_red, cb_blue)

                if isend == True and res == True:
                    return depth
                elif isend == True and res == False:
                    prev_queue.append((-1, -1, -1))
                else:
                    prev_queue.append((nred, nblue, Direction.left))

            if prev_dir != Direction.right:
                isend, res, nred, nblue = move_ball(Direction.right, cb_red, cb_blue)

                if isend == True and res == True:
                    return depth
                elif isend == True and res == False:
                    prev_queue.append((-1, -1, -1))
                else:
                    prev_queue.append((nred, nblue, Direction.right))

    return -1


print(bfs())
