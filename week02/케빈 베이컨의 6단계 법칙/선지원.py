import sys
from collections import deque

#bfs 코드
def kevin_bacon(start):
  queue = deque([start])

  #각 node까지의 거리를 담음
  depth = [0] * (N+1)

  while queue:
    V = queue.popleft()
    for next_friend in link[V]:
      if not visited[next_friend]:
        visited[next_friend] = 1
        queue.append(next_friend)
        #다음 노드 까지의 거리 = 바로 전 노드 까지의 거리 + 1
        depth[next_friend] = depth[V] + 1

  return sum(depth)


#입력
N, M = map(int, sys.stdin.readline().strip().split())

link = [[] for _ in range(N+1)]

for _ in range(M):
  A, B = map(int, sys.stdin.readline().strip().split())
  link[A].append(B)
  link[B].append(A)


ans = float('inf') #케빈 베이컨의 값을 담는거
result = 0 #가장 작은 케빈 베이컨 값을 가진 친구를 저장
for i in range(1, N+1):
  visited = [0] * (N+1)
  visited[i] = 1
  temp = kevin_bacon(i)
  if temp < ans:
    result = i
    ans = temp

print(result)