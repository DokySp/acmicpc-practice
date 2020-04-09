import sys
# https://www.acmicpc.net/source/12521062
# https://withcoding.com/79 (range 함수 사용법) : range(시작, 끝, 인터벌)
# https://dodo4513.github.io/2017/07/02/python_algorithm/ (파이썬 반복문)
# https://www.acmicpc.net/board/view/855 (sys.stdin)

# sys.stdin.readline
reader = sys.stdin
ts = list(map(int,reader.readline().split()))

a = list(map(int,reader.read().split()))

for T in range(0, ts[0]*2, 2):
	# a = input().split(' ')
	# res = res + str(a[0] + a[1]) + "\n"
	print( a[T]+a[T+1] )

