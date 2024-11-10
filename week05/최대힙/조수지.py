import heapq
import sys

input = sys.stdin.readline

n = int(input())

nums = []

for _ in range(n):
    x = int(input())

    if x > 0:  # 자연수면 음수 형태로 넣어주기
        heapq.heappush(nums, -x)

    elif x == 0:
        if len(nums) == 0:
            print(0)

        else: # 최소 힙을 사용해서 최대 힙을 구현
            print(-heapq.heappop(nums)) # -를 붙여주면 가장 작은 수가 가장 큰 수가 됨