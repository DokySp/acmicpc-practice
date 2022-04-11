

graph = [
    [0, 5, 4, 0, 0, 0],
    [5, 0, 2, 7, 0, 0],
    [4, 2, 0, 6, 11, 0],
    [0, 7, 6, 0, 3, 8],
    [0, 0, 11, 3, 0, 8],
    [0, 0, 0, 8, 8, 0],
]

tree = []
treelink = []


node_min_val = -20000
void_min_val = -10000

for i in range(9):

    min = 10000
    min_row = -1
    min_col = -1

    for j in range(len(graph)):
        for i in range(len(graph[j])):
            if graph[i][j] > 0 and min > graph[i][j]:
                min = graph[i][j]
                min_row = j
                min_col = i

    # 트리와 만나는 노드 확인
    col_node = -1
    row_node = -1

    for t in range(len(tree)):
        if tree[t].count(min_col) != 0:
            col_node = t

    for t in range(len(tree)):
        if tree[t].count(min_row) != 0:
            row_node = t

    # 새 트리 생성
    if(col_node == -1 and row_node == -1):
        tree.append([min_row, min_col])
    # 순환 생성, 제거
    elif(col_node == row_node):
        graph[min_row][min_col] = void_min_val
        graph[min_col][min_row] = void_min_val
    # 트리 제작
    else:
        graph[min_row][min_col] = node_min_val
        graph[min_col][min_row] = node_min_val
        # 트리 합침
        if(col_node != -1 and row_node != -1):
            treelink.append([min_row, min_col])
            new_tree = []

            for tt in tree[row_node]:
                new_tree.append(tt)
            for tt in tree[col_node]:
                new_tree.append(tt)

            # tree.pop(row_node)
            # tree.insert(row_node, [])
            # tree.pop(col_node)
            # tree.insert(col_node, [])
            # tree.append(new_tree)
            # tree.remove([])
            # tree.remove([])

        else:
            if(col_node != -1):
                tree[col_node].append(min_row)
            if(row_node != -1):
                tree[row_node].append(min_col)


# 그래프 표시
final_tree = []

for i in treelink:
    idx1 = -1
    idx2 = -1

    for t in tree:
        if t.count(i[0]) != 0:
            idx1 = t.index(i[0])
    for t in tree:
        if t.count(i[1]) != 0:
            idx2 = t.index(i[1])

    if(idx1 == -1 or idx2 == -1):
        treelink.remove(i)
        continue

    final_tree.append(tree[idx1])
    final_tree.append(tree[idx2])

    tree.pop(idx1)
    tree.insert(idx1, [])
    tree.pop(idx2)
    tree.insert(idx2, [])
    tree.remove([])
    tree.remove([])

print(treelink)
print(final_tree)
