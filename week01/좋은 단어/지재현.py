N = int(input())
word_count = 0
for _ in range(N):
    word = input()
    stack = []
    for i in range(len(word)):
        stack.append(word[i])
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
    if not stack:
        word_count += 1

print(word_count)