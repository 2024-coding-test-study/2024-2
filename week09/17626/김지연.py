import math
n = int(input())
num = int(math.sqrt(n))# n의 제곱근 보다 작은 정수 저장
lst = [0] * (num + 1)
result = 5
for i in range(1, num+1):
    lst[i] = i**2
for i in range(num, 0, -1):
    cnt = 0
    now = lst[i]
    start = n
    while start > 0:
        
        start -= now #이 수 이후의 값이 들어갔을때
        now = lst[int(math.sqrt(start))]
        cnt += 1
        
    result = min(result, cnt)
    

print(result) 