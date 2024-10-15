import heapq
n = int(input())

'''
4
1 2
1 4
2 6
4 5
'''
time = []
for _ in range(n):
    start, end = map(int, input().split())
    time.append((end, start))
time.sort()
q = []
heapq.heappush(q, time[0])
for i in range(1, n):
    print(q)
    prev_end, prev_start = heapq.heappop(q)
    end, start = time[i]
    if prev_end <= start: #이전 수업에 사용하던 강의실 배정
        heapq.heappush(q, (end, start))
    else: #새로운 강의실 배정
        heapq.heappush(q, (prev_end, prev_start))
        heapq.heappush(q, (end, start))


print(len(q))