def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    print("Dynmic Programming Matrix")
    for row in dp:
        print(row)

    return dp[n][capacity]

value = [2,3,1,4]
weight = [3,4,6,5]
capacity = 8

max_pf = knapsack(value, weight, capacity)
print("\nMaximum Profit:", max_pf)