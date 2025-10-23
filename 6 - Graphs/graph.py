from collections import deque

class Graph:
    """
        https://www.w3resource.com/c-programming-exercises/graph/c-graph-exercises-3.php
        Backtrace: https://www.baeldung.com/cs/dfs-vs-bfs-vs-dijkstra
    """

    def __init__(self, n):
        self.nodes = n
        self.matrix = None

        self.createMatrix(n)

    def createMatrix(self, n) -> None:
        self.matrix = [[0] * n for i in range(n)]
    
    def getMatrix(self) -> list:
        return self.matrix

    def displayMatrix(self) -> None:
        for i in range(self.nodes):
            for j in range(self.nodes):
                pass
                print(f'{self.matrix[i][j]:>3}', end='')
            print('')

    def addEdge(self, start, end, value = 1) -> None:
        self.matrix[start][end] = value
        self.matrix[end][start] = value
    
    def removeEdge(self, start, end) -> None:
        self.graph[start][end] = 0

    def getNeighbours(self, node) -> list:
        array = []
        for i in range(self.nodes):
            if self.matrix[node][i] != 0:
                array.append(i)
        return array

    def bfs(self, start, end) -> bool:
        verified = set()
        queue = deque([start])
        parents = {start: None}

        while queue:
            element = queue.popleft()
            
            if element not in verified: 
                verified.add(element)

                if element == end:
                    return self.backtrace(parents, start, end)

                for neighbour in self.getNeighbours(element):
                    queue.append(neighbour)

                    if neighbour not in parents:
                        parents[neighbour] = element

        return False
    
    def backtrace(self, parents, start, end):
        path = [end]

        while end != start:
            end = parents[end]
            path.append(end)
        
        path.reverse()

        return path
            