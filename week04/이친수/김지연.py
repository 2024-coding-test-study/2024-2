#무조건 1로 시작 
# n=k 자리 이친수는 n = k-1 자리 이친수를 그대로 활용가능함 -> 바텀업 방식 dp로 해결 가능
n = int(input())
pinary_cnt = [0] * (n+1) # i 자리 이친수의 개수 저장하는 리스트

#n=1일때 pinary_cnt[2] = 1에서 index_error발생
pinary_cnt[1] = 1
pinary_cnt[2] = 1
if n < 3:
    print(1)
else:
    for i in range(3, n+1):
        pinary_cnt[i] = pinary_cnt[i-1] + pinary_cnt[i-2]
    print(pinary_cnt[n])