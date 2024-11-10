# 과자 나눠주기
m, n = map(int, input().split())
snack = list(map(int, input().split()))
snack.sort()

def exceptbs():
    if sum(snack) >= m:
        return 1
    return 0

def bs(s, e):
    while s <= e:
        mid = (s + e) // 2 # 자를 길이
        if mid == 0:
            return exceptbs()
        total = sum([s // mid for s in snack]) # 몫
        if m <= total: # 몫이 인원 수보다 많은 경우
            ret = mid
            s = mid + 1
        else:           # 몫이 인원 수 보다 적은 경우
            e = mid - 1
    return ret

print(bs(0, snack[-1]))