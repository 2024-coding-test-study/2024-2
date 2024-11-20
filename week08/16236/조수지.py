from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

space = [list(map(int, input().split())) for _ in range(n)]

# 자신보다 작은 물고기만 먹을 수 있다
# 자신보다 같은 크기의 물고기가 있는 칸은 지나갈 수 있다
# 먹을 수 있는 물고기가 없다면 엄마를 부른다

baby_size = 2 # 아기 상어의 크기
baby_eat = 0 # 아기 상어가 먹은 물고기 수
time = 0 # 지난 시간

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 가장 가까운 물고기 찾기 위해 bfs를 사용
def bfs(baby_x, baby_y, baby_size) :
    visited = [[False] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    eats = []

    q = deque()
    q.append((baby_x, baby_y))
    visited[baby_x][baby_y] = True

    while q :
        x, y = q.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나지 않고, 아직 방문하지 않았다면
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] :
                if space[nx][ny] <= baby_size : # 현재 아기 상어의 크기보다 작거나 같다면
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1

                    # 현재 상어의 크기보다 작고 0이 아니라면 먹을 수 있는 물고기!
                    if space[nx][ny] < baby_size and space[nx][ny] != 0 :
                        eats.append((nx, ny, distance[nx][ny]))

    # 가장 가까운 순서대로 정렬
    return sorted(eats, key=lambda x : (x[2], x[0], x[1]))

# 아기 상어의 처음 위치 찾기
for i in range(n) :
    for j in range(n) :
        if space[i][j] == 9 :
            baby_x, baby_y = i, j
            space[i][j] = 0

while True :
    baby = bfs(baby_x, baby_y, baby_size)

    # 더 이상 갈 곳이 없다면 멈춤
    if not baby :
        break

    # 가장 가까운 먹을 수 있는 물고기에 대해서
    nx, ny, d = baby[0]
    time += d
    baby_eat += 1

    # 지금 몸집과 같은 수의 물고기를 먹었다면
    if baby_size == baby_eat :
        baby_size += 1
        baby_eat = 0

    # 먹은 물고기 자리를 0으로 바꿔줌
    space[baby_x][baby_y]= 0
    # 아기 상어 위치 갱신
    baby_x, baby_y = nx, ny

print(time)