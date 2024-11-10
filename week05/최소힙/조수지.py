import heapq
import sys
input = sys.stdin.readline

n = int(input())

nums = []

for _ in range(n) :
    x = int(input())

    if x > 0 : # 자연수면 넣어주기
        heapq.heappush(nums, x)

    elif x == 0 :
        if len(nums) == 0 :
            print(0)

        else :
            print(heapq.heappop(nums))