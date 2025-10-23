def investment(M, cost, profit):
    n = len(cost)
    dp = [[0] * (M + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for m in range(1, M + 1):
            if cost[i - 1] <= m:
                dp[i][m] = max(
                    dp[i - 1][m],
                    dp[i - 1][m - cost[i - 1]] + profit[i - 1]
                )
    return dp[n][M]
M = 10
cost = [6, 3, 4, 2]
profit = [30, 14, 16, 9]
max_profit = investment(M, cost, profit)
print("Lợi nhuận tối đa có thể đạt:", max_profit)
