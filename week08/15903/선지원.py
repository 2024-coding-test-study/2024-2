import sys
import heapq
input = sys.stdin.readline

def solution():
  for _ in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)
    SUM = x + y

    heapq.heappush(cards, SUM)
    heapq.heappush(cards, SUM)
  return sum(cards)

n, m = map(int, input().strip().split())
cards = list(map(int, input().strip().split()))

heapq.heapify(cards)
print(solution())