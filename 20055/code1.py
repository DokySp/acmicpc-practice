
import sys
sys.stdin = open("sample.txt", "r")

T = int(input())

def rotate_belt():
    global belt, robots, end_point
    belt.insert(0, belt.pop())

    # 로봇 내림
    robots[end_point - 1] = False
    robots.insert(0, robots.pop())


for ttttt in range(T):

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
        # 2-1. 뒤쪽 로봇부터
        for k in range(N-1, -1, -1):


            if robots[k]:
                
                # 로봇 앞에 안막힌 곳
                robot_togo = k
                for rr in range(k+1, N):
                    if robots[rr]:
                        break
                    else:
                        robot_togo += 1

                # 벨트 내구도 갈 수 있는 곳
                belt_togo = k
                for bb in range(k+1, N):
                    if belt[bb] <= 0:
                        break
                    else:
                        belt_togo += 1

                # 최대 가능 거리
                res_togo = min(robot_togo, belt_togo)

                # 이동
                # 만약 벨트 끝인 경우, 삭제 (손상시키고!!)
                # 이동하는 벨트 데미지
                # 그자리인 경우 스킵


                if res_togo >= N - 1:
                    robots[k] = False
                    for mm in range(k + 1, res_togo + 1):
                        belt[mm] -= 1
                elif res_togo == k:
                    pass
                else:
                    robots[k] = False
                    for mm in range(k + 1, res_togo + 1):
                        belt[mm] -= 1
                    robots[res_togo] = True





                # print("robot_togo", robot_togo, "belt_togo", belt_togo)


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

