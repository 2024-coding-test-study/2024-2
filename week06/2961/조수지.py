from itertools import combinations # 조합 찾기 위해 import함
import sys
input = sys.stdin.readline

n = int(input())

ingredients = []

for _ in range(n) :
    sour, bitter = map(int, input().split())

    ingredients.append((sour, bitter))

MIN = float('inf') # 충분히 큰 값으로 초기화

for i in range(1, n + 1) : # 1~n개의 재료들에 대해서
    for combi in combinations(ingredients, i) : # i개의 조합 경우의 수만큼 반복
        sour, bitter = 1, 0 # 곱해줄거니까 1로, 덧셈이니 0으로 초기화

        for s, b in combi :
            sour *= s
            bitter += b

            MIN = min(MIN, abs(sour - bitter))

print(MIN)