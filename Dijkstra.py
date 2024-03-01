def dijkstra(graph, s):
    d = [99999999.9]*graph.qtdVertices()
    y = [0]*graph.qtdVertices()
    z = [False]*graph.qtdVertices()
    d[s-1] = 0

    while False in z:
        distancesFalses = [9999999999.9]*graph.qtdVertices()
        
        for i,f in enumerate(z):
            if not f:
                distancesFalses[i] = d[i]
        
        u = distancesFalses.index(min(distancesFalses)) + 1
        z[u-1] = True

        for v in graph.vizinhos(u):
            if not z[v-1]:
                if d[v-1] > d[u-1] + graph.peso(u,v):
                    d[v-1] = d[u-1] + graph.peso(u,v)
                    y[v-1] = u

    for predecessor in range(len(y)):
        path = []
        aux = predecessor
        
        while y[aux] != 0:
            path.append(aux+1)
            aux= y[aux] - 1
        
        path.reverse()
        path.insert(0, s)
        
        print(predecessor+1, ":", *path, ";", "d =", d[predecessor], sep=" ")