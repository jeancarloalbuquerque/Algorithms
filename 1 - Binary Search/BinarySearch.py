import time, random

def generate_random_list(size):
    list = []
    for i in range(size):
        list.append(i + 1)
    return list

def simple_search(list, search):
    for i in range(len(list)):
        if list[i] == search:
            return i

def binary_search(list, search):
    low_bound = 0
    high_bound = len(list) - 1

    while low_bound <= high_bound:
        middle = (low_bound + high_bound) // 2

        if search == list[middle]:
            return middle

        if search > list[middle]:
            low_bound = middle + 1
        else:
            high_bound = middle - 1
        
    return None



def compare_search_methods(start_size = 10, increase_factor = 2, steps = 20):
    for i in range(steps):

        start = time.time()
        # list = generate_random_list(start_size)
        end = time.time()
        # search = int((start_size / increase_factor) * 0.1)
        list_creation_time = (end - start) * 1000
        search = start_size

        start = time.time()
        result = simple_search(list, search)
        end = time.time()
        simple_search_time = (end - start) * 1000

        start = time.time()
        result = binary_search(list, search)
        end = time.time()
        binary_search_time = (end - start) * 1000

        print(f'{i + 1}; {start_size}; {list_creation_time}; {simple_search_time}; {binary_search_time}')

        start_size *= increase_factor

        list

compare_search_methods()

# start = time.time()
# time.sleep(2)
# end = time.time()

# print(end - start)
