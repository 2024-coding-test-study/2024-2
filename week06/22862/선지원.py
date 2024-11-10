import sys

def solution(K):
  end = 0
  ans = 0
  count_odd = 0

  for start in range(N):

    #홀수의 숫자를 셈
    if S[start] % 2 != 0:
      count_odd += 1

    #홀수의 숫자가 K보다 커지면 end를 올려가면서 연속되는 짝수의 최대수열을 구함
    while count_odd > K:
      if S[end] % 2 != 0:
        count_odd -= 1
      end += 1
    ans = max(ans, start - end + 1 - count_odd)

  return ans


N, K = map(int, sys.stdin.readline().strip().split())
S = list(map(int, sys.stdin.readline().strip().split()))
print(solution(K))