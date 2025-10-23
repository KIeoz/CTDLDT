def knapsack(W, weights, values):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]
W = 10
weights = [6, 3, 4, 2]
values = [30, 14, 16, 9]

max_value = knapsack(W, weights, values)
print("Giá trị lớn nhất có thể đạt:", max_value)

