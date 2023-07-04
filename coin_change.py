def coinChange(coins: list, amount: int) -> int:
    dp = {0: 0}

    def dfs(coin_total):
        print("processing coin_total: ", coin_total)
        if coin_total in dp:
            return
        if coin_total in coins:
            print("whole coin_total added: ", coin_total)
            dp[coin_total] = 1
            return
        min_coins = float("inf")
        for coin in coins:
            remainder = coin_total - coin
            if remainder < 0:
                continue
            total_coin = 1 + dp[remainder]
            min_coins = min(total_coin, min_coins)
        print("processed coin_total added: ", coin_total, " with: ", min_coins)
        dp[coin_total] = min_coins

    for i in range(amount + 1):
        dfs(i)

    return -1 if dp[amount] == float("inf") else dp[amount]


print(coinChange([474, 83, 404, 3], 264))
