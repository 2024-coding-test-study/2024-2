import sys
sys.setrecursionlimit(100000)

#재귀적으로 x node의 루트 노드를 찾는 과정
def get_parent(parent, x):
  if parent[x] != x:
    parent[x] = get_parent(parent, parent[x])
  return parent[x]

#작은 값을 부모로 넣어줌
def union_parent(parent, a, b):
  a = get_parent(parent, a)
  b = get_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


#부모가 같은지 확인
def find_parent(parent, a, b):
  a = get_parent(parent, a)
  b = get_parent(parent, b)
  if a == b:
    return 1
  return 0


N = int(sys.stdin.readline())
points = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
parent = [i for i in range(N+1)]
edges = []
result = 0

#x, y, z 축별로 각 각 정렬
for i in range(3):
  #enumerrate 각 점에 index를 부여하는 함수 [(0, [x0, y0, z0]), (1, [x1, y1, z1]), ...]
  temp = sorted(enumerate(points), key=lambda x: x[1][i])
  for j in range(N-1):
    cost = abs(temp[j][1][i] - temp[j+1][1][i])
    edges.append((cost, temp[j][0], temp[j+1][0]))
edges.sort()

for edge in edges:
  cost, a, b = edge
  if not find_parent(parent, a, b):
    union_parent(parent, a, b)
    result += cost
print(result)
