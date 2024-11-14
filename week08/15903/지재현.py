# 카드 합체 놀이
import heapq

n, m = map(int, input().split())
card = list(map(int, input().split()))
heapq.heapify(card)

for _ in range(m):
    a1 = heapq.heappop(card)
    a2 = heapq.heappop(card)
    heapq.heappush(card, a1 + a2)
    heapq.heappush(card, a1 + a2)

print(sum(card))