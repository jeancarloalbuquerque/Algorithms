def isPowerOfTwo(n):
    if n == 1:
        return True
    if n % 2 == 0:
        return isPowerOfTwo(n/2)
    return False

isPowerOfTwo(-10)


# for i in range(1, 100000000):
#     if isPowerOfTwo(i):
#         print(i)

