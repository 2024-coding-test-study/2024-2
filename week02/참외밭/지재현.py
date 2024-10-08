# 참외밭
'''
    동(1) 서(2) 남(3) 북(4)
    1. 최대 길이가 한 번씩 등장
        4, 2 = ┓ 1 1 3 3
        3, 2 = ┏ 1 1 4 4
        4, 1 = ┛ 2 2 3 3
        3, 1 = ┗ 2 2 4 4
    2. 방향의 나열 순서? -> 무관
    3. 2번 등장하는 방향과 최대 & 최소의 연관? -> 복잡
    4. 그리는 방향 회전 -> 좌 우 끝에 한 번 등장한 값을 배치
        4 2 3 1 3 1 ┓
            -> 2 3 1 3 1 4 ┓
        1 4 1 4 2 3 ┏
            -> 3 1 4 1 4 2 ┏
        1 4 2 3 2 3 ┛
            -> 4 2 3 2 3 1 ┛
        3 1 4 2 4 2 ┗
            -> 1 4 2 4 2 3 ┗
'''
from collections import deque, Counter
import sys
input = sys.stdin.readline

n = int(input()) # 참외 개수
d = deque()

for _ in range(6):
    direct, length = map(int, input().rstrip().split())
    d.append((direct, length))

dcount = Counter([direct for direct, _ in d])
unique_values = [direct for direct, count in dcount.items() if count == 1]
while True:
    d.rotate(1)
    if (d[0][0] in unique_values and d[5][0] in unique_values):
        break

print ((d[0][1] * d[5][1] - d[2][1] * d[3][1]) * n)