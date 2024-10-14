import sys

"""
1 -> 1
2 -> 10
3 -> 100, 101
4 -> 1000, 1001, 1010
5 -> 10000, 10001, 10010, 10100, 10101
1, 1, 2, 3, 5, 8
피보나치의 형태로 증가하는 것을 확인 할 수 있음
"""

def pinary_number(N):
  dp = [0] * (N+1)
  dp[1] = 1
  if N >= 2 :
    dp[2] = 1
  for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]
  return dp[N]


N = int(sys.stdin.readline())
print(pinary_number(N))