def count(list):
    if len(list) == 0:
        return 0
    else:
        list.pop()
        return 1 + count(list)

list = [1, 2, 3, 4, 5, 6, 7, 8]
print(count(list))