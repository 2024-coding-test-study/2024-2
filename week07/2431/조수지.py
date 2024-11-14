from collections import deque
import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split()) # 접시 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
sushi = [int(input()) for _ in range(n)]

start, end = 0, 0
most_various = 0 # k개의 연속된 초밥을 먹을 때, 최대 초밥 종류 수
continue_k = deque()

while start < n :
    continue_k.append(sushi[end])
    SET = set(continue_k) # 중복 제거

    # continue_k에 중복이 없고 k개의 초밥을 먹을 수 있으며 여기에 c가 포함 되지 않았을 때
    if len(SET) == len(continue_k) == k and c not in continue_k :
        print(k + 1)
        break

    else :
        if c not in continue_k : # c가 포함되지 않았다면
            most_various = max(most_various, len(SET) + 1)
        else :
            most_various = max(most_various, len(SET))

    if len(continue_k) >= k : # k보다 같거나 많아졌다면 다음 반복을 위해 빼줌
        start += 1
        continue_k.popleft()

    end = (end + 1) % n

else :
    print(most_various)

# 시간 초과
'''import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split()) # 접시 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호

sushi = []

for _ in range(n) :
    sushi.append(int(input()))

continue_k = [] # 서로 다른 초밥 k가 이어진 거 담을 배열

for i in range(n) :
    test_k = [sushi[i]] # 서로 다른 초밥 k가 이어지는지 확인할 배열. 일단 첫 초밥을 담아줌

    for j in range(1, k) :
        if sushi[(i+j) % n] not in test_k :
            test_k.append(sushi[(i+j) % n])  # 똑같은 초밥이 없으면 배열에 담아줌
        else :
            continue

    continue_k.append(test_k) # 서로 다른 k개의 초밥이 연속됨. 배열에 추가

check_more_k = False

for conti in continue_k :
    if c not in conti : # c가 포함되지 않은 k개의 연속 초밥이 존재한다면
        check_more_k = True
        print(k + 1) # k + 1을 출력
        break

if not check_more_k:
    print(k)'''