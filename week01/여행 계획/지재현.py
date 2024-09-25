# 여행 계획
import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split()) # n = 여행지 수, m = 여행 계획 수
_map = [list(map(int, input().rstrip().split())) for _ in range(n)] # 여행지 연결 맵
plan = list(map(int, input().rstrip().split())) # 여행 계획
count = 0

for i in range(m - 1, 0, -1):
    for j in range(m - i - 1, -1, -1):
        if _map[plan[i] - 1][plan[j] - 1] == 1:
            count += 1
            break

print("YES") if count == m - 1 else print("NO")