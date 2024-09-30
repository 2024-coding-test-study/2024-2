from collections import deque

def add_graph(grahp, x , y) :
    graph[x].append(y)
    graph[y].append(x)


def BFS(grahp, start, n) :
    q = deque([start])
    distance = [-1 for _ in range(n+1)]
    distance[start] = 0
    
    while q :
        v = q.popleft()
        
        for vertax in grahp[v] :
            if distance[vertax] == -1 :
                distance[vertax] = distance[v]+1
                q.append(vertax)
                
    return sum(distance[1:])
            

n,m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
result = []

for _ in range(m) :
    x,y = map(int, input().split())
    add_graph(graph, x, y)
    
for i in range(1, n+1) :
    num = BFS(graph, i, n)
    result.append(num)

min_num = min(result)

for j in range(n) :
    if(result[j] == min_num) :
        print(j+1)
        break
    