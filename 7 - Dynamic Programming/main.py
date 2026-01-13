from KnapsackSolver import Knapsack

# w = 4
# items = ['Violão', 'Rádio', 'Notebook']
# values = [1500, 3000, 2000]
# weights = [1, 4, 3]

w = 7
items = [1, 2, 3, 4, 5]
values = [50, 40, 70, 80, 10]
weights = [3, 2, 4, 5, 1]

knapsack = Knapsack(items, weights, values)
knapsack.solve(w)