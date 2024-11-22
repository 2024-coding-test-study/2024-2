# 시간 초과. pypy3으로 하면 맞았습니다!!가 뜨긴 함
import sys
input = sys.stdin.readline

n = int(input())
snow = list(map(int, input().split()))

snow.sort()  # 눈덩이 길이의 오름차순으로 정렬

MIN = float('inf')

for first_head in range(n - 3):
    for first_body in range(first_head + 3, n): # 왜 +3인가? -> 첫번째 눈사람 머리, 몸통 범위 안에서 두번째 눈사람을 탐색할 것이기 때문.
        first_snowman = snow[first_head] + snow[first_body]

        # first_head와 first_body 안쪽 범위에서 second를 설정한 이유?
        # -> 어차피 first는 모든 범위를 돌 것이기 때문
        # -> first의 바깥 범위까지 탐색 할 필요가 없음
        second_head, second_body = first_head + 1, first_body - 1

        while second_head < second_body:
            second_snowman = snow[second_head] + snow[second_body]
            MIN = min(MIN, abs(first_snowman - second_snowman)) # 최소 차이 갱신

            if first_snowman > second_snowman: # 첫번째 눈사람이 더 크면
                second_head += 1 # 두번째 눈사람의 머리를 더 크게 만들어 전체 크기를 키워줌
            else:
                second_body -= 1

print(MIN)