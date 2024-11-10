# 도영이가 만든 맛있는 음식
from itertools import combinations
import sys

# 선택된 재료 집합에서 맛 차이의 최소값 반환
def cook(recipe):
    s, b = 1, 0
    for m1, m2 in recipe:
        s *= m1
        b += m2
    return abs(s - b)
    
# 재료 집합 선택
def choice(material):
    ret = float('inf')
    # 요소 개수가 1인 것부터
    for i in range(1, len(material) + 1):
        for recipe in combinations(material, i):
            ret = min(ret, cook(recipe))
    return ret

n = int(input())
material = []

# 데이터 입력
for _ in range(n):
    t1, t2 = map(int, input().split())
    material.append((t1, t2))

print(choice(material))