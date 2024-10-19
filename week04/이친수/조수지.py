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