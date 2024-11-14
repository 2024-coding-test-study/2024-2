# 아기상어
import sys, time
from collections import deque
input = sys.stdin.readline

def eat(fishes, min_step):
    global start_x, start_y, step
    global sharkSize, eatCnt

    # 가장 위쪽, 왼쪽에 있는 좌표를 구함
    top_x = min(p[0] for p in fishes)
    cord = [p for p in fishes if p[0] == top_x]
    top_xy = min(cord, key=lambda p: p[1])
    # 현재 위치에서 이동
    _map[start_x][start_y] = 0
    # 좌표 수정
    start_x, start_y = top_xy[0], top_xy[1]
    # 해당 위치가 아기 상어의 위치
    _map[start_x][start_y] = 9
    # 먹은 횟수 1증가
    eatCnt += 1
    # 거리 증가
    if min_step != 1e9:
        step += min_step
    # 만약 먹은 물고기의 수가 현재 크기와 같다면
    if sharkSize == eatCnt:
        eatCnt = 0
        sharkSize += 1

# 먹을 수 있는 물고기 목적지로 이동하는 함수
def move():
    min_step = 1e9
    # 상어의 현재 위치부터 큐로 시작
    q = deque([(start_x, start_y, 0)])
    # 처음 위치를 자취에 남김
    footprint = set([(start_x, start_y)])
    # 같은 거리 물고기
    fishes = []
    while q:
        move_x, move_y, move_s = q.popleft()
        for i in range(4):
            nx = move_x + dx[i]
            ny = move_y + dy[i]
            # 발자취에 해당하지 않으며 맵 범위 안에서 해당 위치가 나보다 크지 않아야 이동가능
            if 0 <= nx < n and 0 <= ny < n and _map[nx][ny] <= sharkSize and (nx, ny) not in footprint:
                footprint.add((nx, ny))
                q.append((nx, ny, move_s + 1))
                # 이동하다가 먹을 수 있는 물고기를 발견하면
                if 0 < _map[nx][ny] < sharkSize:
                    min_step = min(min_step, move_s + 1)
                    if move_s + 1 > min_step:
                        break
                    fishes.append((nx, ny))
    if not fishes:
        return False
    eat(fishes, min_step)
    return True

# 맵 크기
n = int(input())
# 아기 상어의 위치변수
start_x, start_y = 0, 0
# 아기상어 초기 크기
sharkSize = 2
# 아기상어의 섭취 횟수
eatCnt = 0
# 아기상어의 이동 시간
step = 0
# 방향 벡터
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# 맵 생성
_map = []
# 아기 상어의 위치를 결정
for i in range(n):
    m = list(map(int, input().split()))
    if 9 in m:
        start_x = i
        start_y = m.index(9)
    _map.append(m)

while move():
    None
print(step)