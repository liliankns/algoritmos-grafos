from collections import deque

def hierholzer(graph):
    qttEdges = graph.qtdArestas()
    visitedEdges = [False] * qttEdges
    vertex = 1
    haveEulerianCycle, cycle = buscaSubcicloEuleriano(graph, vertex, visitedEdges)

    if not haveEulerianCycle or len(list(filter(lambda x: not x, visitedEdges))) > 0:
        exists, result = False, None
    else:
        exists, result = True, cycle
    
    printaCiclo(exists, result)
    return exists, result


def buscaSubcicloEuleriano(graph, vertex, wasVisited):
    cycle = [vertex]
    finalPoint = vertex

    while True:
        indexOfUnvisitedEdgesAndLinkedToVertex = \
            deque(
                list(filter(
                     lambda i: not wasVisited[i],
                     graph.getIndexArestasVertice(vertex))))

        if len(indexOfUnvisitedEdgesAndLinkedToVertex) == 0:
            return False, "nao tem indexes nao visitados ligados ao vertex"
        else:
            indexDeArestaNaoVisitada = indexOfUnvisitedEdgesAndLinkedToVertex.popleft()
            wasVisited[indexDeArestaNaoVisitada] = True
            edge = graph.arestas[indexDeArestaNaoVisitada]

            if edge[0] == vertex:
                vertex = edge[1]
            else:
                vertex = edge[0]

            cycle.append(vertex)

        if vertex == finalPoint:
            break
    def listHaveItemInOtherList(list1, list2):
        for item in list1:
            if item in list2:
                return True
        return False
    
    while True:
        nonVisitedEdges = [i for i, x in enumerate(wasVisited) if not x]

        vertexexOfCycleWithNonVisitedEdges = deque([
            vertex for vertex in cycle if
            listHaveItemInOtherList(graph.getIndexArestasVertice(vertex), nonVisitedEdges)
        ])

        if len(vertexexOfCycleWithNonVisitedEdges) == 0:
            break

        x = vertexexOfCycleWithNonVisitedEdges.popleft()
        r, cycle2 = buscaSubcicloEuleriano(graph, x, wasVisited)

        if not r:
            return False, "nao ha subciclo euleriano a partir do vertex "

        index = cycle.index(x)
        cycle.pop(index)
        cycle[index:index] = cycle2

    return True, cycle

def printaCiclo(exists, result):
    if exists:
        print(1)
        print(str(result)[1:-1])
    else:
        print(0)
