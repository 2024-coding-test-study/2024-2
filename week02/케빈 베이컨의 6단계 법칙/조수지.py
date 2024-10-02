# 1h

from collections import deque

def bfs(graph, start, n) :
  kb = [-1] * (n + 1) # 케빈 베이컨 수를 구할 배열 초기화

  q = deque()
  q.append(start)
  kb[start] = 0 # 시작 노드 방문 처리
  
  while q :
    node = q.popleft()
    
    for next in graph[node] :
      if kb[next] == -1 : # 방문하지 않았다면
        kb[next] = kb[node] + 1 # 현재 노드에 한 단계 추가한 값을 kb[next]에 저장
        
        q.append(next)
        
  total = sum(kb[1:]) # kb를 다 합해 start의 케빈 베이컨 수 구하기
  
  return total

n, m = map(int, input().split()) # 유저 수, 친구 관계 수

friends = [[] for _  in range(n + 1)]

for _ in range(m) :
  a, b = map(int, input().split()) # a와 b는 친구
  
  friends[a].append(b)
  friends[b].append(a)

min = 999999 # 최솟값 저장할 변수. 일단 큰 수로 초기화 해줬음

for i in range(1, n + 1) :
  n_kb = bfs(friends, i, n) # n의 케빈 베이컨 수 구하기
  
  if n_kb <  min :
    min = n_kb
    result = i
    
print(result) # 케빈 베이컨 수가 가장 작은 사람 출력