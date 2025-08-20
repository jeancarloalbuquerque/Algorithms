def quicksort(list):

    if len(list) < 2:
        return list
    
    else:
        pivot = list[0]
        list.pop(0)
        left = []
        right = []

        for item in list:
            if item < pivot:
                left.append(item)
            else:
                right.append(item)
        
        return quicksort(left) + [pivot] + quicksort(right)

list = [5, 7, 2, 3, 0, 1, 9, 4, 6, 8]

print(quicksort(list))