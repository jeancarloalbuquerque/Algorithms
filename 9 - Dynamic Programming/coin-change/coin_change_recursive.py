import time

def coinChange(coins:list, target:int, memo:dict={}):
    if target in memo:
        return memo[target]
    
    if target == 0:
        return 0
    
    result = float('inf')

    for coin in coins:
        remainder = target - coin
        
        if remainder < 0: continue

        result = min(
            result, 
            coinChange(coins, remainder) + 1
        )
    
    memo[target] = result

    return memo[target]
  
coins = [1, 4, 5]
target = 150

start_time = time.time()

result = coinChange(coins, target)

run_time = time.time() - start_time

print(f'Minimum coins to target {target}: {result}') 
print(f'\n--- Run time: {run_time:.3f}s ---')