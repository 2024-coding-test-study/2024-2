from itertools import combinations
n, k = map(int, input().split())
lst = list(map(int, input().split()))

copy = []
for i in lst:
    copy.append(i)

idx = []
#홀수가 위치한 인덱스 구하기
for i in range(n):
    if lst[i] % 2 != 0:
        idx.append(i)

comb = combinations(idx, k) #홀수가 위치한 인덱스 중에서 k개 뽑기
answer = 0

for idxs in comb:
    #홀수 요소 삭제
    for i in idxs:
        lst.pop(i)
    
    #짝수로 이루어진 연속한 부분 최대 길이 구하기
    now = 0 #현재 포인터
    length = 0
    while now <= n-k-1: #현재 포인터가 끝까지 갔을 때 정지
        if lst[now] % 2 == 0: #짝수면 길이 늘리기
            length += 1
            now += 1
        else: #홀수면 현재까지의 길이 저장후 now 위치 홀수 다음으로 이동
            answer = max(answer, length)
            now += 1

    #수열 원상복구   
    lst = []
    for i in range(n):
        lst.append(copy[i])
        
print(answer)