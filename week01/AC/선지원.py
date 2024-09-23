import sys

def AC_lang(arr):
  result = []
  #direction 1 -> 정방향, -1 -> 역방향
  direction = 1
  start_point = 0
  end_point = len(arr)

  for command in p:
    if command == "R":
      direction *= -1
      start_point, end_point = end_point, start_point
    elif command == "D":
      if start_point == end_point:
        return "error"
      elif direction == 1:
        start_point += 1
      elif direction == -1:
        start_point -= 1

  #정방향 출력
  if direction == 1:
    result = arr[start_point:end_point]
  #역방향 출력
  else:
    for i in range(start_point-1, end_point-1, -1):
      result.append(arr[i])

  return "[" + ",".join(map(str, result)) + "]"



T = int(sys.stdin.readline())

for i in range(T):
  p = list(sys.stdin.readline().strip())
  n = int(sys.stdin.readline())
  X = sys.stdin.readline().strip()
  #n이 0이면 [] 출력
  if n == 0:
    X = []
  #"[", "]", "," 를 제거한 배열 생성
  else:
    X = list(map(int, X[1:len(X)-1].split(',')))

  result = AC_lang(X)
  print(result)
