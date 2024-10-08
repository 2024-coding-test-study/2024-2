# 케빈 베이컨의 6단계 법칙
import sys
from collections import deque
input = sys.stdin.readline

# def showArr2D(rel, n):
#     for i in range(n):
#         for j in range(n):
#             print(rel[i][j], end=" ")
#         print()

def bfs(graph, idx):
    global n
    visited = [False] * n
    visited[idx] = True
    ret = 0
    queue = deque()
    # queue = deque([idx, 0])
    for i in range(n):
        if graph[idx][i] == 1:
            visited[i] = True
            queue.append((i, 1))
            ret += 1

    if ret == n - 1:
        return ret
    
    while queue:
        v, dist = queue.popleft()
        for j in range(n):
            if graph[v][j] == 1 and visited[j] == False:
                visited[j] = True
                queue.append((j, dist + 1))
                ret += dist + 1
    return ret

n, m = map(int, input().rstrip().split())
graph = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().rstrip().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1
# showArr2D(graph, n)

ret = []
for idx in range(n):
    ret.append(bfs(graph, idx))
print(ret.index(min(ret)) + 1)