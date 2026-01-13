from KnapsackSolver import Knapsack

# w = 4
# items = ['Violão', 'Rádio', 'Notebook']
# values = [1500, 3000, 2000]
# weights = [1, 4, 3]

items = {
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
w = 4

knapsack = Knapsack(items)
knapsack.solve(w)