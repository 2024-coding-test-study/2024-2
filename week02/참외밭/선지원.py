import sys

def solution(K):
  max_length = 0
  max_height = 0
  small_length = 0
  small_height = 0

  for i in range(6):
    if point[i][0] == 1 or point[i][0] == 2:
      max_length = max(max_length, point[i][1])
    elif point[i][0] == 3 or point[i][0] == 4:
      max_height = max(max_height, point[i][1])

  for i in range(6):
    next = (i + 1) % 6
    two_next = (i + 2) % 6
    previous = (i - 1) % 6
    if (point[i][0] == 1 or point[i][0] == 2) and ((point[next][0] == 3 and point[previous][0] == 3) or (point[next][0] == 4 and point[previous][0] == 4)):
      small_length = point[i][1]
      small_height = point[next][1] if point[two_next][0] == point[i][0] else point[previous][1]

  result = ((max_length * max_height) - (small_length * small_height)) * K
  print(result)



K = int(sys.stdin.readline())
point = []

for _ in range(6):
  direction, length = map(int, sys.stdin.readline().strip().split())
  point.append((direction, length))

solution(K)

