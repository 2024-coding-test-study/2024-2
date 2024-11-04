import sys

def solution():

  left = 1
  right = max(stick_snack)

  ans = 0
  while left <= right:
    mid = (left + right) // 2
    count = 0

    for i in stick_snack:
      if i >= mid:
        count += i // mid
      else:
        continue

    if count >= M:
      left = mid + 1
      ans = mid
    else:
      right = mid - 1

  return ans



M, N = map(int, sys.stdin.readline().strip().split())
stick_snack = list(map(int, sys.stdin.readline().strip().split()))
print(solution())
