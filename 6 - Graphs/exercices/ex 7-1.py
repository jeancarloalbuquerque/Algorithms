INF = float("inf")

grafo = {}
grafo["Inicio"] = {'A': 5, 'B': 2}
grafo["A"] = {'C': 4, 'D': 2}
grafo["B"] = {'A': 8, 'D': 7}
grafo["C"] = {'D': 6, 'Fim': 3}
grafo["D"] = {'Fim': 1}
grafo["Fim"] = {}

custos = {'A': 5, 'B':2, 'C': INF, 'D': INF, 'Fim': INF}

pais = {'A': 'Inicio', 'B': 'Inicio', 'C': None, 'D': None, 'Fim': None}

processados = set()

def menor_custo(graph):
    menor_custo = float("inf")
    no_menor_custo = None

    for no in graph:
        custo = custos[no]
        if custo < menor_custo and no not in processados:
            menor_custo = custo
            no_menor_custo = no
    
    return no_menor_custo

no = menor_custo(custos)

while no is not None:
    custo = custos[no]
    vizinhos = grafo[no]

    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = no
    
    processados.add(no)
    no = menor_custo(custos)

print(pais)