from collections import deque
import sys
input = sys.stdin.readline

n = int(input()) # 동기 수
m = int(input()) # 리스트의 길이

friends = [[] for _ in range(n + 1)] # 인접리스트 형식으로 초기화

for i in range(m) :
  a, b = map(int, input().split())
  
  friends[a].append(b)
  friends[b].append(a)
  
q = deque(friends[1])

visited = [0] * (n + 1)
visited[1] = 1 # 상근이 자기 자신에는 방문했다고 치기

# 상근이의 친구들 방문
for friend in friends[1] :
  visited[friend] = 1
  
# 친구들의 친구들 방문
while q :
  now = q.popleft()
  
  for ff in friends[now] :
    if not visited[ff] :
      visited[ff] = 1
      
print(visited.count(1) - 1) # 자기자신 빼고 출력


# 알아보기 힘든 코드 ㅋㅋ..
'''import sys
input = sys.stdin.readline

n = int(input()) # 동기 수
m = int(input()) # 리스트의 길이
friends = [[] for _ in range(n + 1)]

for i in range(m) :
  a, b = map(int, input().split())
  
  friends[a].append(b)
  friends[b].append(a)
  
visited = [0] * (n + 1)
visited[1] = 1 # 상근이 자기 자신에는 방문했다고 치기

for i in range(len(friends[1])) :
  visited[friends[1][i]] = 1
  
  for j in range(len(friends[friends[1][i]])) :
    if visited[friends[friends[1][i]][j]] == 0 :
      visited[friends[friends[1][i]][j]] = 1
      
print(visited.count(1) - 1) # 자기자신 빼고 출력 '''