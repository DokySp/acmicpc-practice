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
end_lev = 10


def dfs(depth, curr_board, direction):

    if depth >= end_lev:
        return 100000

    curr_board2 = copy.deepcopy(curr_board)

    if depth != 0:
        is_goal_, is_fail_, curr_board2 = move_balls(curr_board2, direction)

        if is_goal_ and not is_fail_:
            return depth

        elif is_goal_ and is_fail_:
            return 100000



    res1 = dfs(depth + 1, curr_board2, Direction.up)
    res2 = dfs(depth + 1, curr_board2, Direction.down)
    res3 = dfs(depth + 1, curr_board2, Direction.right)
    res4 = dfs(depth + 1, curr_board2, Direction.left)

    res = [res1, res2, res3, res4]
    return min(res)



def move_balls(curr_board, direction):

    curr_board2 = copy.deepcopy(curr_board)


    first_move = St.red
    is_aligned = True

    # 각 공 위치 찾기

    red_loc_x, red_loc_y = find_ball_loc(curr_board2, St.red)
    blue_loc_x, blue_loc_y = find_ball_loc(curr_board2, St.blue)




    # 가능 방향에 상대 공이 경로가 겹친 경우, first_move 수정
    if (direction == Direction.up or direction == Direction.down) and red_loc_x == blue_loc_x:
        if direction == Direction.down:
            if red_loc_y > blue_loc_y:
                first_move = St.red
            else:
                first_move = St.blue
        else:
            if red_loc_y < blue_loc_y:
                first_move = St.red
            else:
                first_move = St.blue
    elif (direction == Direction.right or direction == Direction.left) and red_loc_y == blue_loc_y:
        if direction == Direction.right:
            if red_loc_x > blue_loc_x:
                first_move = St.red
            else:
                first_move = St.blue
        else:
            if red_loc_x < blue_loc_x:
                first_move = St.red
            else:
                first_move = St.blue
    else:
        is_aligned = False


    # 공 이동, 보드 반영

    curr_x = -1
    curr_y = -1

    for i in range(2):
        if first_move == St.red:
            curr_x = red_loc_x
            curr_y = red_loc_y
        else:
            curr_x = blue_loc_x
            curr_y = blue_loc_y

        # 원래 공 위치 삭제
        curr_board2[curr_y][curr_x] = St.blank

        if direction == Direction.up:
            curr_y -= 1
            while curr_board2[curr_y][curr_x] == St.blank or curr_board2[curr_y][curr_x] == St.hole:
                if is_goal(curr_board2[curr_y][curr_x], first_move):
                    # 공이 겹친 경우, 뒤따라 같이 들어갈 수 있음
                    if is_aligned:
                        return True, True, curr_board2
                    else:
                        return True, False, curr_board2
                if is_fail(curr_board2[curr_y][curr_x], first_move):
                    return True, True, curr_board2
                curr_y -= 1
            curr_y += 1

        elif direction == Direction.down:
            curr_y += 1
            while curr_board2[curr_y][curr_x] == St.blank or curr_board2[curr_y][curr_x] == St.hole:
                if is_goal(curr_board2[curr_y][curr_x], first_move):
                    # 공이 겹친 경우, 뒤따라 같이 들어갈 수 있음
                    if is_aligned:
                        return True, True, curr_board2
                    else:
                        return True, False, curr_board2
                if is_fail(curr_board2[curr_y][curr_x], first_move):
                    return True, True, curr_board2
                curr_y += 1
            curr_y -= 1

        elif direction == Direction.right:
            curr_x += 1
            while curr_board2[curr_y][curr_x] == St.blank or curr_board2[curr_y][curr_x] == St.hole:
                if is_goal(curr_board2[curr_y][curr_x], first_move):
                    # 공이 겹친 경우, 뒤따라 같이 들어갈 수 있음
                    if is_aligned:
                        return True, True, curr_board2
                    else:
                        return True, False, curr_board2
                if is_fail(curr_board2[curr_y][curr_x], first_move):
                    return True, True, curr_board2
                curr_x += 1
            curr_x -= 1

        elif direction == Direction.left:
            curr_x -= 1
            while curr_board2[curr_y][curr_x] == St.blank or curr_board2[curr_y][curr_x] == St.hole:
                if is_goal(curr_board2[curr_y][curr_x], first_move):
                    # 공이 겹친 경우, 뒤따라 같이 들어갈 수 있음
                    if is_aligned:
                        return True, True, curr_board2
                    else:
                        return True, False, curr_board2
                if is_fail(curr_board2[curr_y][curr_x], first_move):
                    return True, True, curr_board2
                curr_x -= 1
            curr_x += 1

        # 공 위치 업데이트
        curr_board2[curr_y][curr_x] = first_move

        # 공 전환
        if first_move == St.red:
            first_move = St.blue
        else:
            first_move = St.red

    # 리턴
    # is_goal, is_fail, board
    return False, False, curr_board2



def is_goal(target, ball_color):
    return target == St.hole and ball_color == St.red

def is_fail(target, ball_color):
    return target == St.hole and ball_color == St.blue


def find_ball_loc(curr_board, target):
    for i in range(len(curr_board)):
        loc_y = curr_board[i].count(target)

        if loc_y != 0:
            loc_y = i
            loc_x = curr_board[i].index(target)
            break
    return loc_x, loc_y


val = dfs(0, board, 0)
if val >= 100:
    print(-1)
else:
    print(val)