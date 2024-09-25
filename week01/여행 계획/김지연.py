n, m = map(int, input().split())
city = []
for _ in range(n):
  city.append(list(map(int, input().split())))

plan = list(map(int, input().split()))

#여행지 수 만킄 초기화
parent = [0] * (n+1)
for i in range(1, n+1):
  parent[i] = i


def find_parent(parent, x):
  if parent[x] != x: #x의 부모가 자가 자신이 아니라면 즉, 루트가 아니라면
    parent[x] = find_parent(parent, parent[x])
  return parent[x]
def union_parent(parent, a, b): #합치기 연산 -> 부모 리스트 업데이트 (a와 b의 부모를 찾아서 수가 더 작은 노드가 부모가 되도록함
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

#최대가 500이라 시간초과 안남 (n^2이여도)
for i in range(n):
  for j in range(n):
    if city[i][j] == 1: #이어져있으면 union 연산, 부모리스트 업데이트
      union_parent(parent, i+1, j+1)

possible = True
#여행계획이 2, 3, 4, 3 이라면 이 노드들의 부모가 같은지 확인하면됨
for i in range(m-1):
  if parent[plan[i]] != parent[plan[i+1]]:
    print("NO")
    possible = False
    break
if possible:
  print("YES")