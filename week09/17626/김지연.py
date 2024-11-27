import math
n = int(input())
num = int(math.sqrt(n))# n의 제곱근 보다 작은 정수 저장
lst = [i**2 for i in range(1, num+1)]

cnt = 0
#1,2,3,4 최소 개수 종류
if int(math.sqrt(n)) == math.sqrt(n):
    cnt = 1
else:
    for i in range(1, int(math.sqrt(n))+1):
        if int(math.sqrt(n - i**2)) == math.sqrt(n-i**2):
            cnt = 2
            break
        
    if cnt == 0:
        for i in range(1, int(math.sqrt(n)) +1):
            for j in range(1, int(math.sqrt(n - i**2)) +1):
                if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(n - i**2 - j**2):
                    cnt = 3
if cnt == 0:
    print(4)
else:
    print(cnt)
    
    