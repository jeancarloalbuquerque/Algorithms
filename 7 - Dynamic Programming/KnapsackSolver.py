class Knapsack:
    def __init__(self, items, weights, values):
        # TODO: adding suport to use json-like dictionary for items

        self.items = items
        self.weights = weights
        self.values = values

        self.n = len(self.items)
    
    def createTable(self, w):
        return [[0] * (w + 1) for _ in range(self.n + 1)]
    
    def solve(self, w):
        self.table = self.createTable(w)

        for item in range(1, self.n + 1):
            for capacity in range(1, w + 1):
                without_current_item = self.table[item - 1][capacity]
                with_current_item = 0
                weight_current_item = self.weights[item - 1]

                if capacity >= weight_current_item:
                    remaining_capacity = capacity - weight_current_item
                    with_current_item = self.values[item - 1] + self.table[item - 1][remaining_capacity]

                self.table[item][capacity] = max(without_current_item, with_current_item)
        
        # TODO: implment next two methods
        print('Max value: ', self.maxValue(w))
        print('Selected items: ', self.selectedItems(w))
    
    def maxValue(self, w):
        return self.table[self.n][w]

    def selectedItems(self, w):
        selected = set()
        item, capacity = self.n, w

        while item > 0:
            current = self.table[item][capacity]
            previous = self.table[item - 1][capacity]

            if current == previous:
                item -= 1
                continue

            if current != previous:
                selected.add(self.items[item - 1])

                remaining = current - self.values[item - 1]

                while previous != remaining and remaining > 0:
                    capacity -= 1
                    previous = self.table[item -1][capacity]

            item -= 1
            
        return selected