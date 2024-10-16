import sys
input = sys.stdin.readline

def _search():
    global count
    visited[1] = True
    for i in rel[1]: # i => 상근이의 친구
        if not visited[i]:
            visited[i] = True
            count += 1
        for k in rel[i]: # k => 상근이의 친구의 친구
            if not visited[k]:
                visited[k] = True
                count += 1

n = int(input())
rel = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(int(input())):
    a, b = map(int, input().rstrip().split())
    rel[a].append(b)
    rel[b].append(a)

count = 0
_search()
print(count)