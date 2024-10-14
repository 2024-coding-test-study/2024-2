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
