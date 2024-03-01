from Grafo import Grafo
import BuscaEmLargura
import CicloEuleriano
import Dijkstra
import FloydWarshall

def main():
    grafo = Grafo("ContemCicloEuleriano.net")
    
    print("\n--------------Busca em Largura-----------------")
    BuscaEmLargura.buscaEmLargura(grafo, 1)
    print("-----------------------------------------------\n\n")
    
    print("--------------Ciclo Euleriano------------------")
    CicloEuleriano.hierholzer(grafo)
    print("-----------------------------------------------\n\n")

    print("--------------Dijkstra-------------------------")
    Dijkstra.dijkstra(grafo, 1)
    print("-----------------------------------------------\n\n")

    print("--------------FloydWarshall--------------------")
    FloydWarshall.floydWarshall(grafo)
    print("-----------------------------------------------\n\n")
    
if __name__ == '__main__':
    main()
