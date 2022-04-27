N, M = input().split(" ")

N = int(N)
M = int(M)

board = []
order = []

for i in range(N):

    tmp = []
    inp = input().split(" ")

    for tt in inp:
        tmp.append(int(tt))

    board.append(tmp)

for i in range(M):
    d, s = input().split(" ")

    d = int(d)
    s = int(s)

    dx = 0
    dy = 0

    if d == 1:
        dy = -1
    elif d == 2:
        dy = 1
    elif d == 3:
        dx = -1
    elif d == 4:
        dx = 1

    order.append([dx, dy, s])


# print(board)
# print(order)

# N, M = 7, 1
# board = [
#     [0, 0, 0, 0, 0, 0, 0],
#     [3, 2, 1, 3, 2, 3, 0],
#     [2, 1, 2, 1, 2, 1, 0],
#     [2, 1, 1, 0, 2, 1, 1],
#     [3, 3, 2, 3, 2, 1, 2],
#     [3, 3, 3, 1, 3, 3, 2],2
#     [2, 3, 2, 2, 3, 2, 3],
# ]
# order = [[0, 1, 2]]

# N, M = 7, 4
# board = [
#     [0, 0, 0, 2, 3, 2, 3],
#     [1, 2, 3, 1, 2, 3, 1],
#     [2, 3, 1, 2, 3, 1, 2],
#     [1, 2, 3, 0, 2, 3, 1],
#     [2, 3, 1, 2, 3, 1, 2],
#     [3, 1, 2, 3, 1, 2, 3],
#     [1, 2, 3, 1, 2, 3, 1],
# ]
# order = [[0, -1, 3], [0, 1, 2], [-1, 0, 1], [1, 0, 3]]


# N, M = 7, 4
# board = [
#     [1, 1, 1, 2, 2, 2, 3],
#     [1, 2, 2, 1, 2, 2, 3],
#     [1, 3, 3, 2, 3, 1, 2],
#     [1, 2, 2, 0, 3, 2, 2],
#     [3, 1, 2, 2, 3, 2, 2],
#     [3, 1, 2, 1, 1, 2, 1],
#     [3, 1, 2, 2, 2, 1, 1],
# ]
# order = [[0, -1, 3], [0, 1, 2], [-1, 0, 1], [1, 0, 3]]


num_board = [[0 for _ in range(N)] for _ in range(N)]
one = 0
two = 0
three = 0


def get_dir(inp):
    inp %= 4
    if inp == 0:
        return -1, 0
    elif inp == 1:
        return 0, 1
    elif inp == 2:
        return 1, 0
    elif inp == 3:
        return 0, -1


# flatten
fboard = [-10]


def make_num_board():

    dx = int((N - 1) / 2)
    dy = int((N - 1) / 2)
    dir_count = 0
    idx = 1
    is_change = False
    length = 1

    while True:

        gx, gy = get_dir(dir_count)

        for _ in range(length):
            dx += gx
            dy += gy
            num_board[dy][dx] = idx

            # flatten
            fboard.append(board[dy][dx])

            idx += 1

            if idx == N * N:
                return

        if is_change:
            length += 1

        dir_count += 1
        is_change = not is_change


def add_score(marbno):

    global one, two, three

    # 이게 아니라 폭발한 구슬 계산
    # for i in range(0, N*N):
    if marbno == 1:
        one += 1
    elif marbno == 2:
        two += 1
    elif marbno == 3:
        three += 1


def pop_marble(dest, score=True):
    # 지움
    # pop할 때 순서 주의
    dest.sort(reverse=True)
    for target in dest:
        marb = fboard.pop(target)
        if score:
            add_score(marb)
    for _ in dest:
        fboard.append(0)


def destroy_marble(orderr):

    global fboard, num_board

    # 부술 인덱스 뽑음
    ox = int((N - 1) / 2)
    oy = int((N - 1) / 2)
    dest = []

    for _ in range(orderr[2]):
        ox += orderr[0]
        oy += orderr[1]

        dest.append(num_board[oy][ox])
        # dest.append([ox, oy])

    pop_marble(dest, score=False)


def find_group(limit):
    grinfo = []
    counted_group = 0

    ii = 0
    while ii < len(fboard) - 1:

        color_check = -1

        if fboard[ii] == fboard[ii + 1]:
            glen = 0
            start = -1
            end = -1

            color_check = fboard[ii]

            if color_check == 0:
                break

            start = ii
            for ik in range(ii, len(fboard)):

                if color_check == fboard[ik]:
                    glen += 1
                    continue
                else:
                    end = ik - 1
                    ii = end
                    break

            if glen >= limit:
                grinfo.append([start, end])
                counted_group += 1
            else:
                pass

        ii += 1

    return counted_group, grinfo


def exp_marble():

    dest = []
    counted_group, results = find_group(limit=4)

    for group in results:
        for tt in range(group[0], group[1] + 1):
            dest.append(tt)

    pop_marble(dest)
    return counted_group


def create_marble():

    global fboard

    newf = [-10]

    _, results = find_group(limit=2)

    gr = []
    lng = []

    for fr, bk in results:
        leng = bk - fr + 1
        gr.append(fr)
        lng.append(leng)
    i = 1

    gridx = 0
    gr.append(-10)
    # 길이 3 고려를 안함... ☆☆☆
    while i < len(fboard):

        # 매우중요!!! ☆☆☆☆☆
        # count, index 함수가 시간복잡도가 굉장히 높은듯
        # 되도록이면 쓰지 않도록 해야한다!! ☆☆☆☆☆
        if len(newf) == len(fboard):
            break
        elif fboard[i] == 0:
            newf.append(0)
        elif gr[gridx] == i:
            newf.append(lng[gridx])
            i += lng[gridx] - 1
            gridx += 1
        else:
            newf.append(1)

        newf.append(fboard[i])

        i += 1

    # 업데이트를 안함... ☆☆☆
    fboard = newf


make_num_board()


for orderr in order:

    # print("====step====")
    # print(fboard)

    # 1. 구슬 파괴
    destroy_marble(orderr)
    # print(fboard)

    # 2. 구슬 폭발 ( != 파괴)

    groupn = 1
    while groupn != 0:
        groupn = exp_marble()
    # print(fboard)

    # 3. 구슬 생성
    create_marble()
    # print(fboard)


score = 0

score = one + two * 2 + three * 3
# print(one, two, three)
# print(fboard)
print(score)
