import sys
import heapq
input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a > b:
    parent[a] = b
  else:
    parent[b] = a

N = int(input())

edges = []
parent = [i for i in range(N+1)]

for u in range(1, N+1):
  costs = list(map(int, input().strip().split()))
  for v in range(1, N+1):
    edges.append((costs[v-1], u, v))
edges.sort()

result = 0
for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)
