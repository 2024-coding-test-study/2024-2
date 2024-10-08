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


V, E = map(int, sys.stdin.readline().strip().split())
parent = [0] * (V+1)

edges = []
result = 0

#부모 노드를 자기 자신으로 초기화
for i in range(1, V+1):
  parent[i] = i

for _ in range(E):
  a, b, cost = map(int, sys.stdin.readline().strip().split())
  #비용 순으로 정렬하기 위해 cost를 제일 앞에 위치
  edges.append((cost, a, b))

edges.sort()

for edge in edges:
  cost, a, b = edge
  if not find_parent(parent, a, b):
    union_parent(parent, a, b)
    result += cost
print(result)