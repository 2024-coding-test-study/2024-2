import heapq # 최소 힙 사용하기 위함.
import sys
input = sys.stdin.readline

n = int(input())

courses = []

for i in range(n) :
  s, t = map(int, input().split())
  
  courses.append((s, t)) 
  
courses.sort() # 강의 시작 시간 기준 오름차순 정렬

rooms = [] # 강의실 현황

for course in courses :
  start, end = course
  
  # rooms가 비어있지 않고 가장 빨리 끝나는 강의실의 종료 시간보다 이후라면
  if rooms and rooms[0] <= start : # 이때, rooms[0]은 가장 이른 종료 시간. 최소 힙이기 때문
    heapq.heappop(rooms) # 가장 빨리 끝나는 강의실을 비워줌

  heapq.heappush(rooms, end) # 현재 강의실의 종료 시간 추가

print(len(rooms))





# 시간 초과 코드. 이전에 비슷한 문제의 코드 참고.
'''
n = int(input()) # 강의 수

courses = [] # 강의 리스트

for i in range(n) :
  s, t = map(int, input().split())
  
  courses.append((s, t)) 
  
courses.sort() # 강의 시작 시간 기준 오름차순 정렬

rooms = [] # 강의실 현황

for course in courses :
  ealriest_end = float('inf') # 가장 빨리 끝나는 강의의 끝나는 시간. 무한대로 초기화
  ealriest_end_room_idx = -1 # 가장 빨리 끝나는 강의실 번호. -1로 초기화
  
  for i in range(len(rooms)) :
    # 배정돼 있는 강의의 종료시간보다 배정할 강의의 시작 시간이 이후이고
    # 배정된 강의들 중 가장 빨리 끝난다면
    if course[0] >= rooms[i][1] and rooms[i][1] < ealriest_end :
      ealriest_end = rooms[i][1]
      ealriest_end_room_idx = i
    
  if ealriest_end_room_idx != -1 : # 강의가 배정될 방을 찾았다면
    rooms[ealriest_end_room_idx] = course 
    
  else : # 시간이 모두 겹친다면
    rooms.append(courses[i]) # 새로운 강의실 추가
    
print(len(rooms))'''