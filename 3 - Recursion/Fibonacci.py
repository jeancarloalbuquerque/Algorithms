

def fibonacci(n):
    global count
    count += 1

    if n == 0 or n == 1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

# count = 0
# print(fibonacci(40), count) 

for i in range(1, 40):
    count = 0
    fibonacci(i)
    print(i, ";", count)