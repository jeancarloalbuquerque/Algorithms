from collections import deque

class Graph:
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

    def bfSearch(self, start, end) -> bool:
        queue = deque()
        verified = set()

        # Adiciona os vizinhos de start na fila
        for n in self.getNeighbours(start):
            queue.append(n)

        while (len(queue) != 0):
            element = queue.popleft()
            
            if element not in verified: 
                if element == end:
                    return True

                for n in self.getNeighbours(element):
                    queue.append(n)

        return False
        