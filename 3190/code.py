
N = int(input())
board = []

# # 테스트용 배열출력
# def print_board():
#     for i in board:
#         print(i)

# 보드 생성
for i in range(N):
    btmp = []
    for i in range(N):
        btmp.append(0)
    board.append(btmp)

# 시과 배치
k = int(input())
for i in range(k):
    x, y = input().split(" ")
    board[int(x)-1][int(y)-1] = 2

control = []

# 아동경로 설정
L = int(input())
for i in range(L):
    sec, direction = input().split(" ")
    control.append({"sec": int(sec), "direction": direction})

loc = {
    "x": 0,
    "y": 0,
    "direction": 2 # LTRB 순 0123
}

# 초기설정
snake_stack = [[0,0]]
board[0][0] = 1


for i in range(10000):

    # 방향전환
    if len(control) != 0 and i == control[0]['sec']:
        res = control.pop(0)
        if res['direction'] == "L":
            loc['direction'] -= 1

            if loc['direction'] < 0:
                loc['direction'] = 3

        else:
            loc['direction'] += 1

            if loc['direction'] > 3:
                loc['direction'] = 0


    # 뱀 머리 위치 설정
    if loc['direction'] == 0:
        snake_stack.append([loc['x'], loc['y']-1])
        loc['y'] -= 1
    elif loc['direction'] == 2:
        snake_stack.append([loc['x'], loc['y']+1])
        loc['y'] += 1
    elif loc['direction'] == 3:
        snake_stack.append([loc['x']+1, loc['y']])
        loc['x'] += 1
    elif loc['direction'] == 1:
        snake_stack.append([loc['x']-1, loc['y']])
        loc['x'] -= 1

    # 종료조건
    if loc['x'] < 0 or loc['x'] >= N or loc['y'] < 0 or loc['y'] >= N or board[loc['x']][loc['y']] == 1:
        # print(loc)
        # print(board[loc['x']][loc['y']])
        # print("-==-=-==-=-")
        # print("End")
        print(i+1)
        break

    # 뱀 꼬리 자르기
    if board[loc['x']][loc['y']] != 2:
        res = snake_stack.pop(0)
        board[res[0]][res[1]] = 0

    # 뱀 위치 저장
    for k in snake_stack:
        board[k[0]][k[1]] = 1

    # print_board()
    # print()
