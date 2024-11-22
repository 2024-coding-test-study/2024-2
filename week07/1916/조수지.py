import heapq
import sys
input = sys.stdin.readline

def dijkstra(start_city) :
    q = []

    heapq.heappush(q, (0, start_city))
    distance[start_city] = 0

    while q :
        cost, now_city = heapq.heappop(q) # 가장 적은 비용 버스를 꺼내줌

        if distance[now_city] < cost : # 기존에 있는 비용이 더 적으면 continue
            continue

        for i in bus[now_city] : # now_city에서 출발하는 버스들에 대하여
            if cost + i[1] < distance[i[0]] :
                distance[i[0]] = cost + i[1]

                heapq.heappush(q, (cost + i[1], i[0]))

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

bus = [[] for _ in range(n + 1)]

for _ in range(m) :
    start, arrive, cost = map(int, input().split())

    bus[start].append((arrive, cost))

start_city, arrive_city = map(int, input().split())

distance = [int(1e9)] * (n + 1)

dijkstra(start_city)

print(distance[arrive_city])