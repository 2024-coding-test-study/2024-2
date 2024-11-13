import sys
input = sys.stdin.readline

def solution():
  result = 0

  #연속해서 먹는 경우
  eat_list = [0] * (d+1)
  #추가로 받는 초밥의 갯수 + 1
  eat_list[c] = 1

  start = 0
  end = 0

  #start가 N+k-1번 이동 하면 모든 경우의 수 고려
  for i in range(N+k-1):
    eat_list[queue[start]] += 1
    if abs(start - end) + 1 >= k:
      result = max(result, d + 1 - eat_list.count(0))
      eat_list[queue[end]] -= 1
      end = (end + 1) % N
    start = (start + 1) % N

  return result


N, d, k, c = map(int, input().strip().split())
queue = []
for _ in range(N):
  susi = int(input())
  queue.append(susi)
print(solution())