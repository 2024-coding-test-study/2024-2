import sys
input = sys.stdin.readline

def solution():
  result = 0
  location = 0

  while location < N-1:
    #이동해야 하는 거리
    charge = 0
    #이동 해야 하는 node
    move = 0

    for j in range(location, N-1):
      #현재의 가격이 j 일때 보다 더 비싸면 break
      if cost[location] > cost[j]:
        break
      #현재 넣는게 싼 경우
      charge += distances[j]
      move += 1

    result += charge * cost[location]
    location += move
  return result


N = int(input())
distances = list(map(int, input().strip().split()))
cost = list(map(int, input().strip().split()))
print(solution())