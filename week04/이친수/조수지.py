# 1h

import sys
input = sys.stdin.readline

n = int(input()) # n자리 이진수

if n == 1 or n == 2 :
  print(1)
  
else :

  pinary = [0] * (n + 1) 

  pinary[1], pinary[2] = 1, 1 # 1) 1, 2) 10

  # n-1자리의 이친수에 0을, n-2자리의 이친수에 01을 붙이면 n자리 이친수가 됨
  for i in range(3, n + 1) :
    pinary[i] = pinary[i - 1] + pinary[i - 2]
  
  print(pinary[n])


# 힙을 사용한 코드... 시간 초과
'''import heapq
import sys
input = sys.stdin.readline

n = int(input()) # n자리 이진수

if n == 1 or n == 2 : # 1) 1, 2) 10
  print(1)

else :
  pinary = [] # 이친수 저장할 배열
  cnt = 0 # 이친수 개수
  
  heapq.heappush(pinary, '1') # 이친수는 1로 시작하므로 넣어줌
  
  while pinary :
    now = heapq.heappop(pinary)
    
    if len(now) == n : #
      cnt += 1
    
    else :
      if now[-1] == '0' :
        heapq.heappush(pinary, now + '0')
        heapq.heappush(pinary, now + '1')
      
      # 1이 등장하면 그 다음은 '무조건' 0이 되어야 함    
      elif now[-1] == '1' :
        heapq.heappush(pinary, now + '0')
  
  print(cnt)'''