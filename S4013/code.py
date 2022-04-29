import sys
sys.stdin = open("sample.txt", "r")

T = int(input())

class Magnet:
    S = 1
    N = 0

class Dirr:
    cw = 1
    ccw = -1


def rotate(tar, dirr):
    global gear

    if dirr == Dirr.cw:
        gear[tar].insert(0, gear[tar].pop())
    else:
        gear[tar].append(gear[tar].pop(0))


for ttttt in range(T):

    N = int(input())

    gear = []
    order = []

    for i in range(4):
        inp = input().split(" ")
        tmp = []
        for k in inp:
            tmp.append(int(k))
        gear.append(tmp)

    for i in range(N):
        inp = input().split(" ")
        order.append([int(inp[0]) - 1, int(inp[1])])


    for idx in range(len(order)):

        gearn, dirr = order[idx]

        # 기어 돌림
        # 돌리기 전, 양끝 정보 저장
        left = gear[gearn][6]
        right = gear[gearn][2]
        rotate(gearn, dirr)


        idx = 0
        gn = gearn - 1
        dr = dirr
        while True:
            if gn >= 0 and left != gear[gn][2]:
                dr *= -1
                left = gear[gn][6]
                rotate(gn, dr)
                gn -= 1
            else:
                break
        idx = 0
        gn = gearn + 1
        dr = dirr
        while True:
            if gn < 4 and right != gear[gn][6]:
                dr *= -1
                right = gear[gn][2]
                rotate(gn, dr)
                gn += 1
            else:
                break

    score = (gear[0][0] * 1) + (gear[1][0] * 2) + (gear[2][0] * 4) + (gear[3][0] * 8)

    print("#" + str(ttttt + 1), score)
