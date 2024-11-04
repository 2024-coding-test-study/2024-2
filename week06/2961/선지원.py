import itertools
import sys

def solution():
  gap = float('inf')

  for select_count in range(1, N+1):
    #combination 연산을 통해 재료의 수를 1 ~ N 개 까지 경우의 수를 모두 구함
    combinations = itertools.combinations(ingredient, select_count)

    #각 콤비네이션 연산 안에서 신맛과 쓴 맛을 꺼네서 그 차이를 계산하여 작은 값을 gap에 담음
    for cb in combinations:
      total_S = 1
      total_B = 0
      for s, b in cb:
        total_S *= s
        total_B += b
      gap = min(gap, abs(total_S - total_B))

  return gap


N = int(sys.stdin.readline())
ingredient = []
for _ in range(N):
  S, B = map(int, sys.stdin.readline().strip().split())
  ingredient.append((S, B))
print(solution())