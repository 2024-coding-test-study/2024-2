from collections import deque

class Graph:
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.graph = [[0] * (vertex_count + 1) for _ in range(vertex_count + 1)]
        
    def add_edge(self, x, y):
        self.graph[x][y] = 1
        self.graph[y][x] = 1
        
    def bfs(self, start):
        dept = 0
        count = 0
        check = [False] * (self.vertex_count + 1)
        
        q = deque()
        q.append(start)
        check[start] = True

        while q:
            _size = len(q)

            for _ in range(_size):
                node_index = q.popleft()

                for j in range(1, self.vertex_count + 1):
                    if not check[j] and self.graph[node_index][j] == 1:
                        check[j] = True
                        q.append(j)

                        if dept == 0 or dept == 1:
                            count += 1
            
            dept += 1
            if dept == 2:
                break
        
        return count


vertex_count = int(input())
repeat_num = int(input())
graph = Graph(vertex_count)

for _ in range(repeat_num):
    x, y = map(int, input().split())
    graph.add_edge(x, y)

print(graph.bfs(1))
