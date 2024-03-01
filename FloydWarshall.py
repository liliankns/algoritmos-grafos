def floydWarshall(graph):
    d = [0]*(graph.qtdVertices()+1)
    a = [[0 for i in range(graph.qtdVertices())] for j in range(graph.qtdVertices())]
    d.insert(0,a)
    for i in range(graph.qtdVertices()):
        for j in range(graph.qtdVertices()):
            if i == j:
                d[0][i][j] = 0
            else:
                if i != j and graph.haAresta(i+1,j+1):
                    d[0][i][j] = graph.peso(i+1,j+1)
                else:
                    d[0][i][j] = 9999999.9
    for k in graph.vertices.keys():
        d.insert(k, [[0 for i in range(graph.qtdVertices())] for j in range(graph.qtdVertices())])
        for u in graph.vertices.keys():
            for v in graph.vertices.keys():
                d[k][u-1][v-1] = min(d[k-1][u-1][v-1], d[k-1][u-1][k-1] + d[k-1][k-1][v-1])

    for v,i in enumerate(d[graph.qtdVertices()]):
        print(v+1, ":", *i)