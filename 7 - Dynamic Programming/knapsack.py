n = 4
w = 10

value = [10, 40, 30, 50]
weight = [5, 4, 6, 3]

table = [[0] * (w + 1) for _ in range(n + 1)]

for item in range(1, n + 1):
    for capacity in range(1, w + 1):
        max_without_current_item = table[item - 1][capacity]
        max_with_current_item = 0
        weight_current_item = weight[item - 1]

        if capacity >= weight_current_item:
            remaining_capacity = capacity - weight_current_item
            max_without_current_item = value[item - 1] + table[item - 1][remaining_capacity]

        table[item][capacity] = max(max_without_current_item, max_with_current_item)

print(f'Max value: {table[n][w]}')