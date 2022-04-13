
board = []


class St:
    blank = 0
    wall = -1
    hole = 10
    red = 1
    blue = 2

class Direction:
    up = 1
    down = 2
    left = 3
    right = 4
    iter = [1,2,3,4]


inp = input().split(" ")
N, M = int(inp[0]), int(inp[1])


for n in range(N):
    tmp = []
    inp = input()

    for m in range(M):

        if inp[m] == ".":
            tmp.append(St.blank)
        elif inp[m] == "#":
            tmp.append(St.wall)
        elif inp[m] == "O":
            tmp.append(St.hole)
        elif inp[m] == "R":
            tmp.append(St.red)
        elif inp[m] == "B":
            tmp.append(St.blue)

    board.append(tmp)






# # print(board)
# board = [[-1, -1, -1, -1, -1, -1, -1], [-1, 0, 0, 0, 1, 2, -1], [-1, 0, -1, -1, -1, -1, -1], [-1, 0, 0, 0, 0, 0, -1],
#          [-1, -1, -1, -1, -1, 0, -1], [-1, 10, 0, 0, 0, 0, -1], [-1, -1, -1, -1, -1, -1, -1]]
# N, M = 7, 7





import copy

board_queue = []
prev_direction_queue = []




def bfs():
    board_queue = []

    tmp = copy.deepcopy(board)
    board_queue.append(tmp)
    prev_direction_queue.append(-1)


    # Depth 1~10
    for depth in range(0, 11):

        # print("iter: ", depth)
        # print("queue size: ", len(board_queue))
        # print("false count: ", board_queue.count(False))

        # 자식 노드 (큐에 쌓인만큼) 방향에 대해 검사, TF
        # 바뀐 보드, 끝났는지, 성공했는지

        for k in range(len(board_queue)):
            prev_dir = prev_direction_queue.pop(0)
            sample_board = board_queue.pop(0)
            if not sample_board:
                continue

            for direction in Direction.iter:
                ch_board, isdone, issuccess = move_board(sample_board, direction, prev_dir)
                if isdone and issuccess:
                    return depth
                elif not isdone and not issuccess:
                    board_queue.append(ch_board)
                    prev_direction_queue.append(direction)
                elif isdone and not issuccess:
                    board_queue.append(False)
                    prev_direction_queue.append(direction)

    return -1



def move_board(sample_board, direction, prev_direction):

    # 위로 움직였으면, 다음 턴에 아래로 움직일 필요없음 / 오른쪽으로 움직였으면 다음 턴에 왼쪽으로 갈 이유 없음
    if direction == Direction.up and prev_direction == Direction.down:
        return sample_board, True, False
    elif direction == Direction.down and prev_direction == Direction.up:
        return sample_board, True, False
    elif direction == Direction.left and prev_direction == Direction.right:
        return sample_board, True, False
    elif direction == Direction.right and prev_direction == Direction.left:
        return sample_board, True, False



    # 수평이 맞는지 먼저 확인 -> 먼저 이동할 공 설정
    first_ball = St.red
    red_x, red_y = find_ball_location(St.red, sample_board)
    blue_x, blue_y = find_ball_location(St.blue, sample_board)


    if direction == Direction.up and red_x == blue_x:
        if red_y > blue_y:
            first_ball = St.blue
    elif direction == Direction.down and red_x == blue_x:
        if blue_y > red_y:
            first_ball = St.blue
    elif direction == Direction.left and red_y == blue_y:
        if red_x > blue_x:
            first_ball = St.blue
    elif direction == Direction.right and red_y == blue_y:
        if blue_x > red_x:
            first_ball = St.blue

    # 해당 방향으로 이동 & 공이 구멍에 들어갔는지 조건 검사
        # 각각의 동작에서 공은 동시에 움직인다.
        # 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다.
        # 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다.
        # 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.
        # 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다.
        # 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.

    shift_x = 0
    shift_y = 0
    uboard = copy.deepcopy(sample_board)

    if direction == Direction.left:
        shift_x = -1
    elif direction == Direction.right:
        shift_x = 1
    elif direction == Direction.up:
        shift_y = -1
    elif direction == Direction.down:
        shift_y = 1




    # 공 2개 움직임
    for i in range(2):

        is_hole = False

        currx, curry = find_ball_location(first_ball, uboard)
        uboard[curry][currx] = St.blank

        currx += shift_x
        curry += shift_y
        while uboard[curry][currx] == St.blank or uboard[curry][currx] == St.hole:
            if uboard[curry][currx] == St.hole:
                is_hole = True
                break

            currx += shift_x
            curry += shift_y

        if not is_hole:
            uboard[curry - shift_y][currx - shift_x] = first_ball

        if first_ball == St.blue:
            first_ball = St.red
        else:
            first_ball = St.blue

    # 공이 들어간 경우
    red_x, red_y = find_ball_location(St.red, sample_board)
    blue_x, blue_y = find_ball_location(St.blue, sample_board)

    if red_x == -1 and blue_x != -1:
        return uboard, True, True
    elif red_x == -1 and blue_x == -1:
        return uboard, True, False
    elif red_x != -1 and blue_x == -1:
        return uboard, True, False

    return uboard, False, False
    # return uboard, isdone, issuccess


def find_ball_location(ball_color, sboard):
    for n in range(N):
        for m in range(M):
            if sboard[n][m] == ball_color:
                return m, n
    return -1, -1



print(bfs())
