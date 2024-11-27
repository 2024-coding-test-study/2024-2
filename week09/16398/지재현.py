# 행성 연결
import sys

def find_root(parent, x):
    if parent[x] != x:
        parent[x] = find_root(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_root(parent, a)
    b = find_root(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v = int(input())
parent = [0] * (v + 1)
result = 0
for i in range(1, v + 1):
    parent[i] = i

graph = []
for _ in range(v):
    graph.append(list(map(int, input().split())))

edges = []
for i in range(v):
    for j in range(v):
        if i != j:
            edges.append((graph[i][j], i, j))

edges.sort()        
for edge in edges:
    cost, a, b = edge
    if find_root(parent, a) != find_root(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)