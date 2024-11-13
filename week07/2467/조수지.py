import sys
input = sys.stdin.readline

n = int(input()) # 전체 용액의 수
solutions = list(map(int, input().split())) # 용액의 특성값들

left, right = 0, n - 1
value = float('inf') # 두 용액의 특성값 저장할 변수. 무한대로 초기화
close_0 = [0, 0]

while left < right :
    total = solutions[left] + solutions[right]

    if value > abs(total) :
        value = abs(total) # 더 적은 특성값으로 바꾸기

        close_0[0] = solutions[left]
        close_0[1] = solutions[right]

    if total > 0 :
        right -= 1

    elif total < 0 :
        left += 1

    else : # 합이 0이면 바로 반복문을 빠져나감
        break

print(close_0[0], close_0[1])