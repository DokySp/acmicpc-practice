
import sys
sys.stdin = open("sample.txt", "r")

def rotate_belt():
    global belt, robots, end_point
    belt.insert(0, belt.pop())

    # 로봇 내림
    robots[end_point - 1] = False
    robots.insert(0, robots.pop())


N, K = input().split(" ")
N = int(N)
K = int(K)

belt = []

start_point = 0
end_point = N

inp = input().split(" ")
for i in inp:
    belt.append(int(i))
robots = [False for _ in range(N*2)]


# 1. 벨트 움직임
# 2. 로봇 이동
# 3. 로봇 올림

count = 1
while True:
# for i in range(10):

    # 1. 벨트 + 로봇 움직임
    rotate_belt()



    # 2. 로봇 이동
    # !!! 로봇은 한 칸만 이동한다..!
    # 2-1. 뒤쪽 로봇부터

    # !!! 마지막칸 뒤로 전부 무조건 내림 !
    # !!! 마지막 칸은 미리 내리면 의도대로 나오지 않음 !!
    # robots[N-1] = False
    for nn in range(N-1, 2*N):
        robots[nn] = False

    for k in range(N-1, 0, -1):

        if robots[k]:
            # 다음 칸이 내구도 있으면서 다른 로봇 없는지 검사
            if not robots[k+1] and belt[k+1] > 0:
                # 이동
                robots[k+1] = True
                robots[k] = False
                belt[k+1] -= 1

    # 3. 로봇 올림
    if belt[start_point] > 0:
        robots[start_point] = True
        belt[start_point] -= 1

    # print(robots)
    # print(belt)
    #
    # print("res: ", belt.count(0), "count: ", count)
    # print()

    if belt.count(0) >= K:
        break
    count += 1


print(count)
