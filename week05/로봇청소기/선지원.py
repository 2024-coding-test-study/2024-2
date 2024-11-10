import sys

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def robot_clean(r, c, d):
  result = 0

  while True:
    if graph[r][c] == 0:
      graph[r][c] = 2
      result += 1

    found_cleanable = False
    for i in range(4):
      d = (d + 3) % 4
      nx, ny = r + direction[d][0], c + direction[d][1]

      if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
        r, c = nx, ny
        found_cleanable = True
        break

    if not found_cleanable:
      back_direction = (d + 2) % 4
      r, c = r + direction[back_direction][0], c + direction[back_direction][1]

      if graph[r][c] == 1:
        break
  return result


N, M = map(int, sys.stdin.readline().strip().split())
r, c, d = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
print(robot_clean(r, c, d))