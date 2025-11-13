from WeightedGraph import WeightedGraph

grafo = WeightedGraph(6)

grafo.addEdge(0, 1, 5)
grafo.addEdge(0, 2, 0)

grafo.addEdge(1, 3, 15)
grafo.addEdge(1, 4, 20)
# grafo.addEdge(1, 2, -100)

grafo.addEdge(2, 3, 30)
grafo.addEdge(2, 4, 35)

grafo.addEdge(3, 5, 20)
grafo.addEdge(4, 5, 10)

# grafo.displayMatrix()

print(grafo.dijkstra(0, 5))

"""
grafo.pesquisa_em_largura(0, 3)
"""