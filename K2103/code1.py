def solution(n, k, cmd):

    answer = ""
    idx = k
    arr = [i for i in range(n)]

    delq = []

    for command in cmd:

        if command[0] == "U":  # 위
            shift = int(command.split()[1])
            idx -= shift

        elif command[0] == "D":  # 아래
            shift = int(command.split()[1])
            idx += shift

        elif command[0] == "C":  # 삭제
            delq.append(arr.pop(idx))
            if len(arr) == idx:
                idx -= 1

        elif command[0] == "Z":  # 복구
            targ = delq.pop()
            st_point = 0

            if targ >= len(arr) - 1:
                st_point = len(arr) - 1
            else:
                st_point = targ

            # print(arr)

            i = st_point
            # print("st_point", st_point, "targ", targ, "i", i)

            leng = len(arr)
            while i >= 0:
                if arr[i] <= targ:
                    i += 1
                    break
                i -= 1
            arr.insert(i, targ)

            if i <= idx:
                idx += 1

            # print(arr)

    ii = 0
    limit = len(arr)

    for ni in range(n):

        if ii >= limit - 1:
            if arr[limit - 1] == ni:
                answer += "O"
            else:
                answer += "X"
            continue

        if arr[ii] == ni:
            ii += 1
            answer += "O"
        else:
            answer += "X"

    return answer
