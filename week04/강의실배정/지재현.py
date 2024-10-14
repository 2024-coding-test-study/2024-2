from queue import PriorityQueue
import sys
import heapq

input = sys.stdin.readline

pq = PriorityQueue()
for _ in range(int(input())):
    s, t = map(int, input().rstrip().split())
    pq.put((s, t))

# endtime을 리스트로 초기화
endtime = []

S1, T1 = pq.get()
heapq.heappush(endtime, T1)  # 첫 번째 요소 추가

while not pq.empty():
    S2, T2 = pq.get()
    # 힙의 최상단 요소 확인
    if endtime and endtime[0] <= S2:
        heapq.heappop(endtime)  # 조건에 맞으면 제거
    heapq.heappush(endtime, T2)  # 새로운 요소 추가

print(len(endtime))
