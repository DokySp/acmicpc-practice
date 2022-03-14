
# 리스트 초기화
operand = []
operator = []
comb = []

# 입력
N = int(input())
formula = input()

# TC
# N = 9
# formula = "3+8*7-9*2"


# 연산자 클래스 등록
class Operator:
    plus = 1
    minus = 2
    mul = 3


# 입력값 처리
for i in range(0, N):
    if formula[i] == "+":
        operator.append(Operator.plus)
    elif formula[i] == "-":
        operator.append(Operator.minus)
    elif formula[i] == "*":
        operator.append(Operator.mul)
    else:
        operand.append(int(formula[i]))


# 괄호 조합 찾는 재귀함수
def search(prev, dimension):
    lastIdx = prev.pop()
    prev.append(lastIdx)

    if dimension == 0:
        st = lastIdx + 2
        for k in range(st, len(operand)-1):
            comb.append(prev + [k])  # 외우기
    else:
        st = lastIdx + 2
        comb.append(prev)
        for k in range(st, len(operand)-1):
            search(prev + [k], dimension-1)


# 괄호조합 찾기
for i in range(0, len(operand)-1):
    search([i], int(len(operand)/2))


# 괄호 없을 경우 추가
comb.append([])

# 최댓값 저장
max = 0;
is_first = True


# 괄호 조합 연산
for target in comb:

    rOperator = operator + []
    rOperand = operand + []
    comb_list = (target + [])

    # 괄호 먼저 연산
    for idx in comb_list:
        if rOperator[idx] == Operator.plus:
            rOperand[idx] = rOperand[idx] + rOperand[idx+1]
        elif rOperator[idx] == Operator.minus:
            rOperand[idx] = rOperand[idx] - rOperand[idx+1]
        elif rOperator[idx] == Operator.mul:
            rOperand[idx] = rOperand[idx] * rOperand[idx+1]
        rOperand.pop(idx + 1)
        rOperand.insert(idx+1, "X")
        rOperator.pop(idx)
        rOperator.insert(idx, "X")

    # X 제거
    for i in comb_list:
        rOperand.remove("X")
        rOperator.remove("X")

    # 나머지 연산
    for idx in range(0, len(rOperator)):

        if rOperator[idx] == Operator.plus:
            rOperand[1] = rOperand[0] + rOperand[1]
        elif rOperator[idx] == Operator.minus:
            rOperand[1] = rOperand[0] - rOperand[1]
        elif rOperator[idx] == Operator.mul:
            rOperand[1] = rOperand[0] * rOperand[1]
        rOperand.pop(0)

    # 최댓값 검사
    if is_first:
        max = rOperand[0]
        is_first = False

    if max < rOperand[0]:
        max = rOperand[0]


# 결과 출력
print(max)
