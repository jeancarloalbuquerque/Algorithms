from collections import deque

class WeightedGraph:
    """
        https://www.w3resource.com/c-programming-exercises/graph/c-graph-exercises-3.php
        Backtrace: https://www.baeldung.com/cs/dfs-vs-bfs-vs-dijkstra
    """

    def __init__(self, n):
        self.nodes = n
        self.matrix = None

        self.createMatrix(n)

    def createMatrix(self, n) -> None:
        self.matrix = [[None] * n for i in range(n)]
    
    def getMatrix(self) -> list:
        return self.matrix

    def displayMatrix(self) -> None:
        for i in range(self.nodes):
            for j in range(self.nodes):
                value = self.matrix[i][j] 

                if value is None:
                    value = '-'

                print(f'{value:>3}', end='')
            print('')

    def addEdge(self, start, end, value = 1) -> None:
        self.matrix[start][end] = value
    
    def removeEdge(self, start, end) -> None:
        self.matrix[start][end] = 0

    def getNeighbours(self, node) -> list:
        array = dict()
        for i in range(self.nodes):
            if self.matrix[node][i] is not None:
                array[i] = self.matrix[node][i]
        return dict(sorted(array.items(), key=lambda x:x[1])).keys()

    def dijkstra(self, start, end) -> bool:
        costs = {i: float('inf') for i in range(self.nodes)}
        costs[start] = 0

        parents = {start: None}
        
        verified = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            
            if not node in verified:
                neighbours = self.getNeighbours(node)

                for n in neighbours:
                    if not n in verified:
                        queue.append(n)

                    # Calcula o custo para chegar ao nó
                    new_cost = costs[node] + self.matrix[node][n]
                    
                    # Atualiza o custo para chegar ao nó
                    if costs[n] > new_cost:
                        costs[n] = new_cost

                        parents[n] = node
                
                verified.add(node)

        return self.backtrace(parents, start, end)
    
    def backtrace(self, parents, start, end):
        path = [end]

        while end != start:
            end = parents[end]
            path.append(end)
        
        path.reverse()

        return path
            