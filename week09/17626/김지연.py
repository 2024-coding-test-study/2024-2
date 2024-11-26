import math
n = int(input())
num = int(math.sqrt(n))# n의 제곱근 보다 작은 정수 저장
lst = [i**2 for i in range(1, num+1)]

#1,2,3,4 최소 개수 종류
find = False
if n in lst:
    find = True
    print(1)
else:
    #최소 개수가 2개인 경우라면
    for i in lst:
        for j in lst:
            if i + j == n:
                find = True
                print(2)
                break
            if find:
                break
        if find:
            break
                
    #최소 개수가 3개라면
    for i in lst:
        for j in lst:
            for k in lst:
                if i + j + k == n:
                    find = True
                    print(3)
                    break
            if find:
                break
        if find:
            break
 
if not find:
    print(4)