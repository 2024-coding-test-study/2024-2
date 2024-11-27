# 주유소
import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

# 충전할 기름을 구하는 함수 => 효율적(현재 가장 싼 값)으로 갈 수 있는 지점까지의 거리
def getDestination(currentLocation):
    for arrivalLocation in range(currentLocation + 1, n):
        if arrivalLocation == n - 1:
            break
        if cost[currentLocation] > cost[arrivalLocation]:
            return arrivalLocation
    return n - 1
# 현재 위치로부터 목적지까지 갈 때 소요되는 기름
def calNeedFuel(currentLocation, destination):
    return sum(distance[currentLocation:destination]) * cost[currentLocation]

currentLocation = 0
total = 0
while currentLocation != n -1:
    destination = getDestination(currentLocation)
    total += calNeedFuel(currentLocation, destination)
    currentLocation = destination

print(total)