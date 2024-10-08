import sys

# 1 -> N 까지 증가시켜 가며 dp에 담음
def make_one(n):
  # [0]에는 횟수 [1]에는 부모의 값을 담음
  dp = [[0, 0] for _ in range(n+1)]

  for i in range(2, n+1):
    #초기값은 n-1값에서 1 증가한 값
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = i-1

    #2로 나누어 떨어진다면 n//2 한 값에서 +1
    if i % 2 == 0:
      if dp[i][0] > dp[i // 2][0] + 1:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = i // 2
    #3으로 나누어 떨어진다면 n//3 한 값에서 +1
    if i % 3 == 0:
      if dp[i][0] > dp[i // 3][0] + 1:
        dp[i][0] = dp[i // 3][0] + 1
        dp[i][1] = i // 3

  return dp


N = int(sys.stdin.readline())
dp = make_one(N)

print(dp[N][0])

parent = N
while parent > 0:
  print(parent, end = " ")
  parent = dp[parent][1]
