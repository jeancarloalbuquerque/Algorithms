def factorial(n):
    global count
    count += 1

    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n-1)

count = 0
print(factorial(10), count)