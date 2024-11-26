import sys
input = sys.stdin.readline

n = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

MIN = prices[0] # 거쳐간 도시 중 가장 저렴한 기름 저장할 변수. 첫번째 기름 가격으로 초기화
min_price = [prices[0]]

for i in range(1, n - 1) :
    if MIN > prices[i] :
        MIN = prices[i]
        min_price.append(MIN)
    else :
        min_price.append(MIN)

SUM = 0

for i in range(n - 1) :
    SUM += min_price[i] * roads[i]

print(SUM)