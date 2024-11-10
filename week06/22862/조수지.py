import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 수열의 길이와 삭제 최대 횟수
s = list(map(int, input().split()))

start, end = 0, 0
even_len = 0
max_even_len = 0
cnt_odd = 0

while end < n : # 수열을 벗어나지 않을 동안 반복
    if s[end] % 2 == 0 : # 짝수면
        even_len += 1
    else :
        cnt_odd += 1

    while cnt_odd > k : # 홀수가 k보다 많아지면 홀수를 줄이기 위해 반복
        if s[start] % 2 == 0 :
            even_len -= 1
        else :
            cnt_odd -= 1

        start += 1

    max_even_len = max(max_even_len, even_len) # 더 큰 값으로 바꿔줌
    end += 1

print(max_even_len)


# 끄적끄적..
'''import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 수열의 길이와 삭제 최대 횟수
s = list(map(int, input().split()))

even_len = 0
start_even_idx = -1
end_even_idx = -1

even = [] # 짝수 부분 수열 저장할 리스트

for i in range(n) :
    if s[i] % 2 == 0 : # 짝수라면
        if even_len == 0 : # 이전 수가 홀수였다면
            even_len += 1
            start_even_idx = i

        else : # 이전 수가 짝수였다면
            even_len += 1

    else : # 홀수라면
        if even_len > 0 : # 이전 수가 짝수였다면
            end_even_idx = i - 1
            even.append((start_even_idx, end_even_idx, even_len))
            start_even_idx, end_even_idx, even_len = -1, -1, 0

even.sort(key= lambda x: (x[2], x[0])) # 짝수 부분 수열 길이로 오름차순, 같다면 시작 인덱스를 기준으로 오름차순

# 이 다음에 어떻게 해야 할 지 모르겠네...'''