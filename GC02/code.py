from operator import ne
from platform import node


class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next


# 그래프 구현 (인접 리스트)

node_list = {
    0: Node(
        data=0,
        next=Node(
            data=1,
            next=Node(
                data=2,
                next=Node(
                    data=3,
                    next=None
                ),
            ),
        ),
    ),
    1: Node(
        data=1,
        next=Node(
            data=0,
            next=Node(
                data=4,
                next=None
            ),
        ),
    ),
    2: Node(
        data=2,
        next=Node(
            data=0,
            next=Node(
                data=4,
                next=Node(
                    data=5,
                    next=None
                ),
            ),
        ),
    ),
    3: Node(
        data=3,
        next=Node(
            data=0,
            next=Node(
                data=5,
                next=None
            ),
        ),
    ),
    4: Node(
        data=4,
        next=Node(
            data=1,
            next=Node(
                data=2,
                next=Node(
                    data=6,
                    next=None
                ),
            ),
        ),
    ),
    5: Node(
        data=5,
        next=Node(
            data=2,
            next=Node(
                data=3,
                next=Node(
                    data=6,
                    next=None
                ),
            ),
        ),
    ),
    6: Node(
        data=6,
        next=Node(
            data=2,
            next=Node(
                data=4,
                next=Node(
                    data=5,
                    next=None
                ),
            ),
        ),
    ),
}


mem = {
    0: False,
    1: False,
    2: False,
    3: False,
    4: False,
    5: False,
    6: False,
}


def mem_init():
    global mem
    mem = {
        0: False,
        1: False,
        2: False,
        3: False,
        4: False,
        5: False,
        6: False,
    }


# DFS
def dfs(root: Node):

    # 이미 탐색한 노드의 경우 리턴
    if mem[root.data] == True:
        return

    # 탐색
    print(root.data)
    # Memoization
    mem[root.data] = True

    next_node = root.next
    # 다음 노드로 넘김
    while True:
        dfs(node_list[next_node.data])
        # 너비로 넘김
        next_node = next_node.next

        # 너비 끝
        if next_node is None:
            break


# BFS
def bfs(root: Node):

    # 뎁스 0
    prev_nodes = [node_list[3]]
    next_nodes = []
    for p in prev_nodes:
        print(p.data)
        mem[p.data] = True

    # 각 뎁스별 탐색
    for i in range(5):

        # 같은 뎁스 모두 뽑아내서 출력 / 저장
        for n in prev_nodes:

            next_node = n

            while True:
                next_node = next_node.next

                # 말단인 경우 패스
                if next_node is None:
                    break

                # 이미 들렀으면 패스
                if mem[next_node.data] == True:
                    continue

                print(next_node.data)
                mem[next_node.data] = True
                next_nodes.append(node_list[next_node.data])

        # 출력 후, prev_node로 넘김
        prev_nodes.clear()
        for n in next_nodes:
            prev_nodes.append(n)
        next_nodes.clear()


print("DFS")
mem_init()
dfs(node_list[3])
print()

print("BFS")
mem_init()
bfs(node_list[3])
