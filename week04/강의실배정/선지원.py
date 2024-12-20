import heapq
import sys

n = int(sys.stdin.readline())

time = []

for i in range(n):
  start, end = map(int, sys.stdin.readline().split())
  time.append([start, end])

time.sort(key=lambda x: x[0])

room = []
heapq.heappush(room, time[0][1])

for i in range(1, n):
  if time[i][0] < room[0]: # 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠르면
    heapq.heappush(room, time[i][1]) # 새로운 회의실 개설
  else: # 현재 회의실에 이어서 회의 개최 가능
    heapq.heappop(room) # 새로운 회의로 시간 변경을 위해 pop후 새 시간 push
    heapq.heappush(room, time[i][1])

print(len(room))