# 회전초밥
import sys
from collections import deque
input = sys.stdin.readline

n, d, k, c = map(int, input().split())

sushi = []
for _ in range(n):
    sushi.append(int(input()))

_eat = deque(sushi[:k])
sushi = deque(sushi)
ret = len(set(_eat))

rotate = 0
while rotate != n:
    sushi.rotate(1)
    rotate += 1
    _eat.pop()
    _eat.appendleft(sushi[0])
    if c in _eat:
        ret = max(ret, len(set(_eat)))
    else:
        ret = max(ret, len(set(_eat)) + 1)

print(ret)