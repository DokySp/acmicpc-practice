alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def solution(s):

    idx = 0
    for a in alpha:
        cnt = s.count(a)
        if cnt > 0:
            for _ in range(cnt):
                st = s.index(a)
                end = st + len(a)

                neww = s[0:st] + str(idx) + s[end : len(s)]
                s = neww
        idx += 1

    return int(s)


print(solution("onezerothreethreethree"))
solution("23four5six7")
solution("2three45sixseven")
solution("123")
