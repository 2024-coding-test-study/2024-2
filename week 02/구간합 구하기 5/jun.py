import sys

graph_size, answer_size = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(graph_size)]
answer = [list(map(int, sys.stdin.readline().split())) for _ in range(answer_size)]

for x1, y1, x2, y2 in answer:
    print(sum(sum(i[x1 - 1 : x2]) for i in graph[y1 - 1 : y2]))