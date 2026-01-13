import time

def fibonacci(memo, n):
    if n in memo:
        return memo[n]
    
    if n <= 2:
        return 1

    memo[n] = fibonacci(memo, n-1) + fibonacci(memo, n-2)
    
    return memo[n]

memo = {}
n = 38

start_time = time.time()
result = fibonacci(memo, n)
run_time = time.time() - start_time

print(f'Fib {n}: {result:,}') 
print(f'\n--- Run time: {run_time:.3f}s ---')