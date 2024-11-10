import sys, heapq

input = sys.stdin.readline
tc = int(input())

def fileMerge(n):
    result = 0
    w = list(map(int, input().rstrip().split()))
    heapq.heapify(w)
    while len(w) > 1:
        f1, f2 = heapq.heappop(w), heapq.heappop(w)
        fileSum = f1 + f2
        result += fileSum
        heapq.heappush(w, fileSum)
    return result

result = []
for _ in range(tc):
    files = int(input())
    result.append(fileMerge(files))

for ret in result:
    print(ret)
