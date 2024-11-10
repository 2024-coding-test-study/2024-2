import sys
input = sys.stdin.readline

m, n = map(int, input().split()) # 조카의 수, 과자의 수
snack_len = list(map(int, input().split()))

l, r = 1, max(snack_len) # 과자의 길이는 양의 정수여야 하므로 1과 가장 긴 과자로 초기화
result = 0

while l <= r : # l이 r보다 작거나 같을 동안 반복
    mid = (l + r) // 2 # l와 r의 중간값인 정수 구해주기. 즉, mid는 최대 과자 길이

    # 과자들을 mid로 나눈 몫을 cnt에 저장
    cnt = sum(snack // mid for snack in snack_len)

    if cnt >= m : # m명의 조카들에게 mid 크기로 나눠줄 수 있으면
        result = mid
        l = mid + 1 # 더 크게 나눠줄 수 있나 확인

    else : # mid 크기로 나눠줄 수 없다면
        r = mid - 1 # 더 작은 크기로 나눠줄 수 있나 확인

print(result) # 최대로 나눠줄 수 있는 과자 길이 출력