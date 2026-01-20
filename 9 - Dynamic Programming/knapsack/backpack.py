def main():
    max_capacity = 4

    items_table = {
        'Violão': {
            'weight': 1,
            'value': 1500
        },
        'Rádio': {
            'weight': 4,
            'value': 3000
        },
        'Notebook': {
            'weight': 3,
            'value': 2000
        }
    }

    total_items = len(items_table)


    items = list(items_table.keys())
    # items   = [_ for _ in items_table]
    weights = [items_table[_]['weight'] for _ in items_table]
    values  = [items_table[_]['value']  for _ in items_table]


    table = [[0 for _ in range(max_capacity + 1)] for _ in range(total_items + 1)]



    for item in range(1, total_items + 1):
        for capacity in range(1, max_capacity + 1):
            without_item = table[item - 1][capacity]
            with_item = 0
            item_weight = weights[item - 1]


            if capacity >= item_weight:
                with_item = values[item - 1]

                remaining_space = capacity - item_weight
                with_item += table[item - 1][remaining_space]

            table[item][capacity] = max(without_item, with_item)
    
    print(f'Max value: {table[total_items][capacity]}')
main()