w = 4
items = [1, 2, 3]
value = [1500, 3000, 2000]
weight = [1, 4, 3]
n = len(items)

table = [[0] * (w + 1) for _ in range(n + 1)]

for item in range(1, n + 1):
    for capacity in range(1, w + 1):
        without_current_item = table[item - 1][capacity]
        with_current_item = 0
        weight_current_item = weight[item - 1]

        if capacity >= weight_current_item:
            remaining_capacity = capacity - weight_current_item
            without_current_item = value[item - 1] + table[item - 1][remaining_capacity]

        table[item][capacity] = max(without_current_item, with_current_item)

print(f'Max value: {table[n][w]}')
print(table)