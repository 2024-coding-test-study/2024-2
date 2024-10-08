# 46m

# 그냥 input()하면 시간초과
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 표 크기, 횟수
table = [[0]  for _ in range(n + 1)]

for i in range(1, n + 1) :
  table[i].extend(map(int, input().split()))
  
# 누적합 표
accum_table = [[0] * (n + 1) for _ in range(n + 1)]

for i in range (1, n + 1) :
  for j in range (1, n + 1) :
    accum_table[i][j] = table[i][j] + accum_table[i - 1][j] + accum_table[i][j - 1] - accum_table[i - 1][j - 1]
    
for _ in range(m) :
  x1, y1, x2, y2 = map(int, input().split())
  
  # x2y2 직사각형에서 x1-1y2 직사각형과 x2y1-1 직사각형을 빼고 겹치는 부분은 두 번 뺏으므로 한 번 더해줌
  sum = accum_table[x2][y2] - accum_table[x1 - 1][y2] - accum_table[x2][y1 - 1] + accum_table[x1 - 1][y1 - 1]
  
  print(sum)


# 첫번째 시도. 시간 초과
'''for _ in range(m) :
  x1, y1, x2, y2 = map(int, input().split())
  sum = 0
  
  for a in range(x1, x2 + 1) :
    for b in range(y1, y2 + 1) :
      sum += table[a][b]
      
  print(sum)'''