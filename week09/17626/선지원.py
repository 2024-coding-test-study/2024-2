#pypy의 경우 정답
import sys
input = sys.stdin.readline

def solution():
  dp = [i for i in range(N+1)]

  for i in range(1, N+1):
    for j in range(1, i):
      if j*j > i:
        break
      dp[i] = min(dp[i], dp[i-(j*j)] + 1)
  return dp[N]


N = int(input())
print(solution())

"""gpt돌림
import sys
input = sys.stdin.readline

def solution(n):
  # 제곱수인 경우 1 반환
  if int(n ** 0.5) ** 2 == n:
    return 1

  # 두 제곱수의 합으로 표현되는 경우 체크
  for i in range(1, int(n ** 0.5) + 1):
    if int((n - i*i) ** 0.5) ** 2 == n - i*i:
      return 2

  # 세 제곱수의 합으로 표현되는 경우 체크
  for i in range(1, int(n ** 0.5) + 1):
    for j in range(1, int((n - i*i) ** 0.5) + 1):
      if int((n - i*i - j*j) ** 0.5) ** 2 == n - i*i - j*j:
        return 3

  # 나머지는 모두 4
  return 4

n = int(input())
print(solution(n))
"""