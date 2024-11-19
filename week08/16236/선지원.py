"""
import sys
from collections import deque
input = sys.stdin.readline
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution(location):
  shark_size = 2
  queue = deque([(location[0], location[1])])
  result = 0

  while queue:
    x, y = queue.popleft()
    for dx, dy in direction:
      nx, ny = x + dx, y + dy
      if nx < 0 or ny < 0 or nx >= N or y >= N:
        continue
      if MAP[nx][ny] > shark_size:
        continue




N = int(input())
MAP = [list(map(int, input().strip().split())) for _ in range(N)]
shark_location = []
for i in range(N):
  for j in range(N):
    if MAP[i][j] == 9:
      shark_location = [(i, j)]
      break

print(solution(shark_location))
"""