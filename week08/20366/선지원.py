import sys
input = sys.stdin.readline

def solution():
  result = float('inf')

  #첫 번쨰 눈사람
  for start in range(N-1):
    for end in range(N-1, start, -1):
      #두개의 눈사람을 만들 수 없으면
      if end - start + 1 < 4:
        continue

      first_snowman = snowballs[start] + snowballs[end]

      #두번째 눈사람
      second_start = start + 1
      second_end = end - 1
      while second_start < second_end:
        second_snowman = snowballs[second_start] + snowballs[second_end]
        diff = first_snowman - second_snowman
        result = min(result, abs(diff))
        if diff < 0:
          second_end -= 1
        else:
          second_start += 1

  return result





N = int(input())
snowballs = list(map(int, input().strip().split()))
snowballs.sort()
print(solution())