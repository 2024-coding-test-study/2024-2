"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""

import sys
from collections import deque

def bfs(start, end):
  ans = "NO"
  queue = deque([start])

  while queue:
    V = queue.popleft()
    for next_node in link[V]:
      if not visited[next_node]:
        if next_node == end:
          ans = "YES"
          return ans
        queue.append(next_node)
        visited[next_node] = 1
  return ans



N, M = map(int, sys.stdin.readline().strip().split())
link = [[] for _ in range(N+1)]

for i in range(N):
  n_link = list(map(int, sys.stdin.readline().strip().split()))
  for j in range(N):
    if n_link[j] == 1:
      link[i+1].append(j+1)

#시작 node 끝 node를 2개 씩 묶어서 bfs로 탐색
trip = list(map(int, sys.stdin.readline().strip().split()))
for i in range(1, M):
  visited = [0] * (N+1)
  ans = bfs(trip[i-1], trip[i])
print(ans)