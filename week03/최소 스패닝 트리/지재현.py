# import sys

# def find(parent, x):
#     if parent[x] != x:
#         parent[x] = find(parent, parent[x])
#     return parent[x]

# def union(parent, rank, x, y):
#     root_x = find(parent, x)
#     root_y = find(parent, y)

#     if root_x != root_y:
#         if rank[root_x] > rank[root_y]:
#             parent[root_y] = root_x
#         elif rank[root_x] < rank[root_y]:
#             parent[root_x] = root_y
#         else:
#             parent[root_y] = root_x
#             rank[root_x] += 1

# def has_cycle(graph):
#     v = len(graph)
#     parent = [i for i in range(v)]
#     rank = [0] * v

#     for u in range(v):
#         for v in range(u + 1, len(graph)):  # 인접 행렬의 비대칭을 고려하여 (u, v) 쌍을 확인
#             if graph[u][v] == 1:  # 엣지가 존재하면
#                 if find(parent, u) == find(parent, v):
#                     return True  # 사이클 발견
#                 union(parent, rank, u, v)

#     return False  # 사이클이 없음

# input = sys.stdin.readline
# v, e = map(int, input().rstrip().split())
# graph = []

# for _ in range(e):
#     a, b, c = map(int, input().rstrip().split())
#     graph.append((a - 1, b - 1, c))

# graph.sort(reverse=True, key=lambda x: x[2])
# total = 0
# _map = [[0 for _ in range(v)] for _ in range(v)]

# for _ in range(v - 1):
#     node = graph.pop()
#     _map[node[0]][node[1]] = 1
#     _map[node[1]][node[0]] = 1
#     if has_cycle(_map):
#         _map[node[0]][node[1]] = 0
#         _map[node[1]][node[0]] = 0
#     else:
#         total += node[-1]

# print(total)


import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

def has_cycle(parent, rank, u, v):
    # 현재 노드 u와 v의 루트를 찾아서 사이클 검사를 진행
    if find(parent, u) == find(parent, v):
        return True  # 사이클 발견
    union(parent, rank, u, v)
    return False  # 사이클이 없음

input = sys.stdin.readline
v, e = map(int, input().rstrip().split())
edges = []

for _ in range(e):
    a, b, c = map(int, input().rstrip().split())
    edges.append((a - 1, b - 1, c))

# 가중치를 기준으로 내림차순 정렬
edges.sort(reverse=True, key=lambda x: x[2])
total = 0
parent = [i for i in range(v)]
rank = [0] * v

for a, b, c in edges:
    if not has_cycle(parent, rank, a, b):
        total += c

print(total)
