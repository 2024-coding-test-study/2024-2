import heapq
m, n = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort() #과자 길이 정렬 후 이분 탐색 
copy_lst = [0] * n
for i in range(len(lst)):
    copy_lst[i] = lst[i]

#주어진 과자 길이 모두 더한 후 조카 수로 나눠서 최대 길이 구하기
answer = sum(lst) // m

#이분 탐색
def binary_search(start, end, target):
    while start <= end:
        
        mid = (start + end) // 2
        
        if lst[mid] >= target: #최대로 나눠줄 수 있는 막대 과자 길이(target) 보다 길거나 같으면 리턴
            lst[mid] = lst[mid] - target
            return mid
        elif lst[mid] < target:
            start = mid + 1
    return False
        
while answer != 0: #과자를 나눠줄 수 없을 때까지 반복
    #막대길이(answer)를 m명에게 나눠줄 수 있는지 확인
    mid = 0
    for i in range(m):
        mid = binary_search(mid, n-1, answer) #m개의 막대길이 (answer)를 lst에서 이분 탐색
        lst.sort()
    if mid == False:
        for i in range(len(lst)):
            lst[i] = copy_lst[i]
        answer -= 1
    else:
        break
print(answer)


