# 행성이 이어진 edge가 주어져 있지 않기에 edge를 임의로 구해주는 것이 관건인 문제

import sys
input = sys.stdin.readline

# 부모 찾는 함수. 부모의 부모가 바뀌어도 업데이트 해 줌.
def find(parent, x) : 
  if parent[x] != x :
    parent[x] = find(parent, parent[x])
    
  return parent[x]

# 합치는 함수. a와 rootA를 자꾸 헷갈린다...
def union(parent, rank, a, b) :
  rootA = find(parent, a)
  rootB = find(parent, b)
  
  if rootA != rootB : # 부모가 다를 때
    if rank[rootA] > rank[rootB] : # a 조상의 깊이가 더 깊다면
      parent[rootB] = rootA # b의 부모를 rootA로. 깊은 a에 b를 붙이는게 더 낫기 때문
      
    elif rank[rootA] < rank[rootB] : # b 조상의 깊이가 더 깊다면
      parent[rootA] = rootB # a의 부모를 rootB로
    
    else : # 깊이가 똑같다면
      parent[rootB] = rootA # b의 부모를 rootA로
      rank[rootA] += 1 # rootA에 깊이를 하나 더해줌

n = int(input()) # 행성 개수

planets = []
edges = []

for i in range(n) :
  x, y, z = map(int, input().split())
  
  planets.append((x, y, z, i)) # 행성의 인덱스 추가해서 튜플로!
  
for i in range(3) : 
  planets.sort(key=lambda x: x[i]) # x, y, z 각각으로 정렬
  
  for j in range(1, n) :
    dist = abs(planets[j - 1][i] - planets[j][i]) # 인덱스 번호가 가까운 행성끼리 거리 구해주기
    edges.append((dist, planets[j - 1][3], planets[j][3])) # (거리, j-1번째 행성, j번째 행성) 튜플 추가

edges.sort() # 거리의 오름차순으로 정렬

parent = [i for i in range(n)] # 초기에는 자기 자신이 부모
rank = [0] * n # 깊이 저장 배열

result = 0

for edge in edges :
  cost, a, b = edge
  
  if find(parent, a) != find(parent, b) : # 부모가 다르면 
    union(parent, rank, a, b) # 합쳐줌
    result += cost
  
print(result)