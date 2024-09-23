import sys

def solution(N, word):
  stack = []
  for w in word:
    stack.append(w)
    if len(stack) >= 2:
      #stack에 연속된 두 값이 같으면 pop
      if stack[-1] == stack[-2]:
        stack.pop()
        stack.pop()
  return 1 if len(stack) == 0 else 0



N = int(sys.stdin.readline().strip())
answer = 0

for _ in range(N):
  word = list(sys.stdin.readline().strip())
  answer += solution(N, word)
print(answer)