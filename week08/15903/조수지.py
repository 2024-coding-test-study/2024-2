import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 카드 개수, 카드 합체 수

cards = list(map(int, input().split()))

heapq.heapify(cards)

for _ in range(m) :
    min1 = heapq.heappop(cards)
    min2 = heapq.heappop(cards)

    SUM = min1 + min2

    heapq.heappush(cards, SUM)
    heapq.heappush(cards, SUM)

print(sum(cards))