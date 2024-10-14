n = int(input())

# dp = [[] for _ in range(n + 1)]
# dp[0].append(0b1)
# for i in range(n):
#     for j in dp[i]:
#         dp[i + 1].append(j << 1)
#         if not j & 1:
#             dp[i + 1].append((j << 1) + 1)
# print(len(dp[n - 1]))

# prev_dp = [0b1]
# for i in range(n):
#     curr_dp = []
#     for j in prev_dp:
#         curr_dp.append(j << 1)
#         if not j & 1:
#             curr_dp.append((j << 1) + 1)
#     prev_dp = curr_dp
# print(len(prev_dp))


dp = [[0, 0] for _ in range(n + 1)]

dp[1][1] = 1
dp[1][0] = 0

for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1]  # 마지막 자리가 0인 경우, 그 앞은 0 또는 1일 수 있음
    dp[i][1] = dp[i - 1][0]  # 마지막 자리가 1인 경우, 그 앞은 무조건 0이어야 함

# n자리 이친수의 총 개수는 마지막 자리가 0인 경우와 1인 경우의 합
result = dp[n][0] + dp[n][1]
print(result)
