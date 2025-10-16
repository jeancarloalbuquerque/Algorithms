from Graph import Graph

grafo = Graph(4)

grafo.addEdge(0, 1)
grafo.addEdge(0, 2)
grafo.addEdge(1, 2)
grafo.addEdge(2, 3)

# grafo.displayMatrix()


print(grafo.bfSearch(0, 3))

"""
grafo.pesquisa_em_largura(0, 3)
"""