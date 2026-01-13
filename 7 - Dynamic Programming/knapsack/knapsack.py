w = 4
items = ['Violão', 'Rádio', 'Notebook']
values = [1500, 3000, 2000]
weights = [1, 4, 3]

n = len(items)

table = [[0] * (w + 1) for _ in range(n + 1)]

'''
    Solve the subproblems
'''
for item in range(1, n + 1):
    for capacity in range(1, w + 1):
        weight = weights[item - 1]

        if capacity >= weight:
            remaining_capacity = capacity - weight
            add_item = values[item - 1] + table[item - 1][remaining_capacity]

        ignore_item = table[item - 1][capacity]

        table[item][capacity] = max(ignore_item, add_item)


'''
    Backtrace to find the selected items
'''
selected = set()
item, capacity = n, w

while item > 0:
    current = table[item][capacity]
    previous = table[item - 1][capacity]

    if current == previous:
        item -= 1
        continue

    if current != previous:
        selected.add(items[item - 1])

        remaining = current - values[item - 1]

        while previous != remaining and remaining > 0:
            capacity -= 1
            previous = table[item -1][capacity]

    item -= 1

print(f'Items selected: {selected}')
print(f'Maximum value: {table[n][w]}')