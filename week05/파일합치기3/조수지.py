import heapq
import sys
input = sys.stdin.readline

t = int(input()) # 테스트 데이터 수

for i in range(t) :
    k = int(input())  # 장의 수
    files = list(map(int, input().split()))
    heapq.heapify(files) # 안쓰면 틀림
    total = 0 # 최소 비용 저장할 변수

    while len(files) > 1 : # 파일이 한 개 남을 때 까지 반복
        a = heapq.heappop(files)
        b = heapq.heappop(files)

        c = a + b

        heapq.heappush(files, c)

        total += c

    print(total)