# ret = []
# def _dp(N, depth):
#     ret.append(N)
#     if N == 1:
#         return
#     dp = [[0, 0] for i in range(N + 1)]
    
#     for i in range(2, N + 1):

#         dp[i][0] = dp[i - 1][0] + 1
#         dp[i][1] = i - 1

#         if i % 2 == 0:
#             dp[i][0] = min(dp[i][0], dp[i // 2][0] + 1)
#             dp[i][1] = dp[i][1] if dp[i][0] < dp[i // 2][0] + 1 else i // 2
            
#         if i % 3 == 0:
#             dp[i][0] = min(dp[i][0], dp[i // 3][0] + 1)
#             dp[i][1] = dp[i][1] if dp[i][0] < dp[i // 3][0] + 1 else i // 3
#     if depth == 0:
#         print(dp[-1][0])
#     _dp(dp[-1][1], depth + 1)

# N = int(input())
# _dp(N, 0)
# print(" ".join(map(str, ret)))


def _dp(N):
    dp = [[0, 0] for _ in range(N + 1)]
    
    for i in range(2, N + 1):
        dp[i][0] = dp[i - 1][0] + 1
        dp[i][1] = i - 1
        
        if i % 2 == 0:
            if dp[i][0] > dp[i // 2][0] + 1:
                dp[i][0] = dp[i // 2][0] + 1
                dp[i][1] = i // 2
        
        if i % 3 == 0:
            if dp[i][0] > dp[i // 3][0] + 1:
                dp[i][0] = dp[i // 3][0] + 1
                dp[i][1] = i // 3
    return dp

def trace_path(dp, N):
    ret = []
    while N > 0:
        ret.append(N)
        N = dp[N][1]
    return ret

N = int(input())
dp = _dp(N)
print(dp[N][0])
ret = trace_path(dp, N)
print(" ".join(map(str, ret)))