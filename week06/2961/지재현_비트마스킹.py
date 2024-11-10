# 도영이가 만든 맛있는 음식
import sys

# 선택된 재료 집합에서 맛 차이의 최소값 반환
def cook(recipe):
    if not recipe: # 공집합인 경우
        return float('inf')
    s, b = 1, 0
    for m1, m2 in recipe:
        s *= m1
        b += m2
    return abs(s - b)
    
# 재료 집합 선택
def choice(material):
    ret = float('inf')
    recipes = []
    for bitmask in range(1 << n): # 00 01 10 11
        recipes.append(list([material[i] for i in range(n) if bitmask & (1 << i)]))
    for recipe in recipes:
        ret = min(ret, cook(recipe))
    return ret

n = int(input())
material = []

# 데이터 입력
for _ in range(n):
    t1, t2 = map(int, input().split())
    material.append((t1, t2))

print(choice(material))