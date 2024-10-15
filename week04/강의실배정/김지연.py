import heapq
n = int(input())

time = []
for _ in range(n):
    start, end = map(int, input().split())
    time.append((end, start))
time.sort(key=lambda x : x[1]) #시작 시간으로 정렬하는 이유: 이전 강의가 끝나는 시간에 맞춰서 다른 강의를 할당해 줄때 시작 시간이 빠른 순으로 할당해 줘야 최소의 강의실을 사용할 수 있음
q = []
heapq.heappush(q, time[0])
for i in range(1, n):
    prev_end, prev_start = heapq.heappop(q)
    end, start = time[i]
    if prev_end <= start: #이전 수업에 사용하던 강의실 배정
        heapq.heappush(q, (end, start))
    else: #새로운 강의실 배정
        heapq.heappush(q, (prev_end, prev_start))
        heapq.heappush(q, (end, start))


print(len(q))