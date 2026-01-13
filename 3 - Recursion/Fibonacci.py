import time

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)



n = 38

start_time = time.time()
print(f'Fib {n}: {fibonacci(n):,}') 
end_time = time.time()

print(f'\n--- Run time: {end_time - start_time:.3f}s ---')
