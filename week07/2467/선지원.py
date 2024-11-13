import sys
input = sys.stdin.readline

def solution():
  left, right = 0, N-1
  result = [liquid[0] , liquid[-1]]

  closest_zero = float('inf')

  while right > left:
    SUM = (liquid[left] + liquid[right])
    if abs(closest_zero) >= abs(SUM):
      closest_zero = SUM
      result[0], result[1] = liquid[left], liquid[right]

    if SUM > 0:
      right -= 1
    else:
      left += 1

  return result

N = int(input())
liquid = list(map(int, input().strip().split()))
ans = solution()
print(ans[0], ans[1])