# 50m

import sys
input = sys.stdin.readline

n = int(input())

calc = [0] * (n + 1) # 연산 수 저장할 배열
path = [[i] for i in range(n + 1)] # 1로 만드는 과정의 숫자들을 저장할 배열

path[1] = [1]
  
for i in range(2, n + 1) : # 2부터 n까지 반복
    calc[i] = calc[i - 1] + 1 # 연산에 1을 더해줌
    path[i] = [i] + path[i - 1] # 과정에 i를 더해줌
 
    if i % 2 == 0 and calc[i] > calc[i // 2] + 1 :
        calc[i] = calc[i // 2] + 1
        path[i] = [i] + path[i // 2]
    
    # n이 2와 3 둘 다로 나눠질 수 있기에 if를 사용    
    if i % 3 == 0 and calc[i] > calc[i // 3] + 1 :
        calc[i] = calc[i // 3] + 1
        path[i] = [i] + path[i // 3]
        
print(calc[n]) # n을 1로 만드는 연산의 최솟값 출력

print(" ".join(map(str, path[n]))) # 대괄호와 쉼표를 빼고 공백으로 구분하여 출력




# 시간초과 코드. 정말 단순하게 생각나는...
'''n = int(input())

calc = []
calc.append(n)

while n > 1 :
  if n % 3 == 0 :
    n = int(n // 3)
    calc.append(n)
    
  else :
    if (n - 1) % 3 == 0 :
      n -= 1
      calc.append(n)
    
    elif n % 2 == 0 :
      n = int(n // 2)
      calc.append(n)
    
print(len(calc) - 1)

for num in calc :
  print(num, end=' ')'''