#MST
#우선순위큐?
import heapq
#(가중치, 노드)
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
q = [] #우선순위큐
visited = [False] * (v+1)
visited[0] = True
for i in range(e):
    v1, v2, cost = map(int, input().split())
    graph[v1].append((cost, v2))
    graph[v2].append((cost, v1))


#이런식으로 풀면도지않을까..?
answer = 0
# heapq.heappush(q, graph[1]) #node 1부터 시작
for cost, node in graph[1]:
    heapq.heappush(q,(node, cost))
visited[1] = True
while False in visited: 
    total_cost = 0
    print(q)
    cost, node = heapq.heappop(q)
    for cost, v in graph[node]: #node에 연결된 다른 노드 순차적으로 탐색
        if total_cost:
            visited[v] = True
            print(v, cost)
            answer += cost
            for cost, node in graph[v]:
                heapq.heappush(q,(node, cost))
print(answer)