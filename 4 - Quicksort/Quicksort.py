def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]

        less = [i for i in list[1:] if i < pivot]
        greater = [i for i in list[1:] if i >= pivot]

        return quicksort(less) + [pivot] + quicksort(greater)

calls = 0

list = [5, 7, 2, 9, 6, 1, 3, 4, 0, 8]
result = quicksort(list)

print(result)