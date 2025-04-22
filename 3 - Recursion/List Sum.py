def sum(list):
    if len(list) == 0:
        return 0
    
    else:
        return list.pop() + sum(list)

list = [2, 6, 4]
print(sum(list))