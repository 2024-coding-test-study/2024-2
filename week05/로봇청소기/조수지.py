import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 세로 가로 크기
x, y, d = map(int, input().split()) # 시작 좌표, 방향

# 북서남동. 반시계 방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 문제에서는 북동남서 순이라서 바꿔줌
if d == 1 :
    d = 3
elif d == 3 :
    d = 1

room = [list(map(int, input().split())) for _ in range(n)]

clean_cnt = 0

while 1 :
    if room[x][y] == 0 :
        room[x][y] = 2 # 청소 했다는 뜻
        clean_cnt += 1

    find = False # 다음 청소할 곳을 찾았는 지 여부

    for i in range(4) : # 네 방향 확인
        d = (d + 1) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if room[nx][ny] == 0 and 0 <= nx < n and 0 <= ny < m : # 90도 돌린 칸이 청소가 안됐다면
            x = nx
            y = ny
            find = True

            break

    if not find : # 청소 안된 주변 칸을 못 찾았다면
        nx = x - dx[d]
        ny = y - dy[d]

        if room[nx][ny] != 1 and 0 <= nx < n and 0 <= ny < m: # 후진 할 칸이 벽이 아니라면 후진
            x = nx
            y = ny

        else : # 벽이라면 멈추기
            break

print(clean_cnt)