def buscaEmLargura(graph, vertex):
    acquaintances = [False] * graph.qtdVertices()
    distances = [9999999.9] * graph.qtdVertices()
    predecessor = [None] * graph.qtdVertices()
    acquaintances[vertex-1] = True
    distances[vertex-1] = 0
    f = []
    f.append(vertex)
    listN = {0: [vertex]}

    while len(f) != 0:
        aux = f.pop(0)
        for i in graph.vizinhos(aux):
            if acquaintances[i-1] == False:
                acquaintances[i-1] = True
                distances[i-1] = distances[aux-1] + 1
                predecessor[i-1] = aux
                f.append(i)
                neighborsOfTheLevel = listN.get(distances[i-1], [])
                neighborsOfTheLevel.append(i)
                listN.update({distances[i-1]: neighborsOfTheLevel})
    
    print(listN)    

