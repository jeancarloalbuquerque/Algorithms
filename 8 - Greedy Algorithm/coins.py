coins = [50, 20, 10, 5]

target = 40
change = 0

change_coins = {}

for coin in coins: change_coins[coin] = 0

# O(target, coins)
while change < target: # O(target)
    for coin in coins: # O(coins)
        if coin <= target - change:
            change_coins[coin] += 1
            change += coin
            break

print(change_coins)
