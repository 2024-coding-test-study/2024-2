import sys
import heapq

def solution(s, e):
  distance_list = [float('inf')] * (N+1)
  distance_list[s] = 0
  queue = [(0, s)]

  while queue:
    dist, u = heapq.heappop(queue)
    if dist > distance_list[u]:
      continue
    for v, w in link[u]:
      if distance_list[v] > dist + w:
        distance_list[v] = dist + w
        heapq.heappush(queue, (dist + w, v))
  return distance_list[e]


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
link = [[] for _ in range(N+1)]

for _ in range(M):
  u, v, w = map(int, sys.stdin.readline().strip().split())
  link[u].append((v, w))

start, end = map(int, sys.stdin.readline().strip().split())

print(solution(start, end))
