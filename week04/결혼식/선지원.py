import sys
from collections import deque

def bfs(n, start):
  visited = [0] * (n+1)
  queue = deque([start])
  visited[start] = 1

  while queue:
    V = queue.popleft()
    #친구의 친구 까지만 허용하기 때문
    if visited[V] >= 3:
      continue
    for next_node in friends[V]:
      if not visited[next_node]:
        queue.append(next_node)
        visited[next_node] = visited[V] + 1

  """
  ex) [0, 1, 2, 2, 3, 0, 0]
  n-1 -> 자기 자신을 숫자 카운트에서 제외
  """
  return n - visited[2:].count(0) - 1

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
friends = [[] for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, sys.stdin.readline().strip().split())
  friends[a].append(b)
  friends[b].append(a)

print(bfs(n, 1))