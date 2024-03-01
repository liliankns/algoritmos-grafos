import sys
class Grafo:

    #Inicializa o grafo
    def __init__(self, arquivo):
        self.vertices = {}
        self.arestas = []
        self.leArquivo(arquivo)

    #Retorna a quantidade de vértices
    def qtdVertices(self):
        return len(self.vertices.keys())

    #Retorna a quantidade de arestas
    def qtdArestas(self):
        return len(self.arestas)

    #Retorna o grau do vértice v 
    def grau(self, vertice):
        return len(self.vertices.get(vertice).get("indexDasArestas"))

    #Retorna o rótulo do vértice v
    def rotulo(self, vertice):
        return self.vertices.get(vertice).get("rotulo")
    
    #Retorna os vizinhos do vértice v
    def vizinhos(self, vertice):
        invalid = {"rotulo", "indexDasArestas"}
        return [x for x in self.vertices.get(vertice).keys() if x not in invalid]
        
    def getIndexArestasVertice(self,vertice):
        return self.vertices.get(vertice).get("indexDasArestas")
    
    def haAresta(self, vertice, vizinho):
        if vizinho in self.vertices.get(vertice):
            return True
        return False

    def peso(self, vertice, vizinho):
        if self.haAresta(vertice, vizinho):
            return self.vertices.get(vertice).get(vizinho)
        return sys.float_info.max

    def leArquivo(self, arquivo):
        arquivo = open(arquivo, "r")
        edge = False
        for linha in arquivo:

            if "vertice" in linha:
                continue

            if "edge" in linha:
                edge = True
                continue

            if not edge:
                vertice = linha.split()[0]
                rotulo = linha.split()[1:]
                self.vertices.update({int(vertice):{"rotulo": rotulo, "indexDasArestas": []}})

            if edge:
                vertice, vizinho, peso = linha.split()
                vertice = int(vertice)
                vizinho = int(vizinho)
                peso = float(peso)
                size = len(self.arestas)
                indexesVizinho = self.vertices.get(vizinho).get("indexDasArestas")
                indexesVizinho.append(size)
                self.vertices.get(vizinho).update({vertice: peso, "indexDasArestas": indexesVizinho})
                indexesVertice = self.vertices.get(vertice).get("indexDasArestas")
                indexesVertice.append(size)
                self.vertices.get(vertice).update({vizinho: peso, "indexDasArestas": indexesVertice})
                self.arestas.append((vertice, vizinho, peso))