import sys

def binsearch(len_cookie, max_length, person):
    low = 1
    high = max_length
    answer = 0

    # 사람 수가 과자 수보다 많으면 0 반환
    if len(len_cookie) < person:
        return 0

    while low <= high:
        mid = (high + low) // 2
        cnt = 0

        #과자 배열을 나눔
        for length in len_cookie:
            cnt += length // mid

        if cnt >= person: 
            answer = mid 
            low = mid + 1
        else:  
            high = mid - 1

    return answer


input = sys.stdin.readline

person, cookie = map(int, input().split())
len_cookie = [int(i) for i in input().split()]

len_cookie.sort()

result = binsearch(len_cookie, len_cookie[-1], person)
print(result)