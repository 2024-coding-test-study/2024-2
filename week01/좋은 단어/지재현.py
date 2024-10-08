import sys
input = sys.stdin.readline

N = int(input())
word_count = 0 # 좋은 단어 개수
for _ in range(N):
    word = input().rstrip()
    stack = [] # 스택 생성
    for i in range(len(word)): # AB로 이루어진 단어의 길이만큼 반복
        stack.append(word[i]) # 스택에 단어를 추가
        if len(stack) >= 2: # 스택에 단어가 2개 이상이면 선 긋기
            if stack[-1] == stack[-2]: # 스택에 마지막 단어와 그 전 단어가 같으면 선 긋기
                stack.pop() # pop으로 스택 제거
                stack.pop()
    if not stack: # 스택이 아직 비어있지 않으면
        word_count += 1 # 단어 개수 증가

print(word_count)