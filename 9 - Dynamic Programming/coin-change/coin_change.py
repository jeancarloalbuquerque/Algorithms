def coinChange(coins, amount):
    dp = [float('inf') for _ in range(amount + 1)]
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] +1)

    print(dp)
    return dp[amount]

coins = {1, 5, 10, 25, 50}
amount = 99

result = coinChange(coins, amount)

print(f'You will need {result} coin{'s' if result > 1 else ''} to pay $ {amount}')