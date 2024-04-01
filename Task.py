from collections import deque

class EspacioDeEstados:
    def __init__(self):
        self.grafo = {}

    def cargar_grafo_direccional(self, grafo):
        self.grafo = grafo

    def cargar_grafo_bidireccional(self, grafo):
        bidireccional = {}
        for nodo, vecinos in grafo.items():
            if nodo not in bidireccional:
                bidireccional[nodo] = []
            for vecino in vecinos:
                bidireccional.setdefault(vecino, []).append(nodo)
                bidireccional[nodo].append(vecino)
        self.grafo = bidireccional

    def bfs(self, valor_inicial, valor_final):
        visitados = set()
        cola = deque([[valor_inicial]])
        if valor_inicial == valor_final:
            return [valor_inicial]
        while cola:
            camino = cola.popleft()
            nodo = camino[-1]
            if nodo not in visitados:
                vecinos = self.grafo[nodo]
                for vecino in vecinos:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    cola.append(nuevo_camino)
                    if vecino == valor_final:
                        return nuevo_camino
                visitados.add(nodo)
        return None

    def dfs(self, valor_inicial, valor_final):
        visitados = set()
        pila = [[valor_inicial]]
        if valor_inicial == valor_final:
            return [valor_inicial]
        while pila:
            camino = pila.pop()
            nodo = camino[-1]
            if nodo not in visitados:
                vecinos = self.grafo[nodo]
                for vecino in vecinos:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    pila.append(nuevo_camino)
                    if vecino == valor_final:
                        return nuevo_camino
                visitados.add(nodo)
        return None

# Ejemplo de uso:
graph = {
    0: [1, 2],
    1: [0, 2, 5, 6],
    2: [0, 1, 3, 4],
    3: [2, 4, 6],
    4: [2, 3, 5],
    5: [1, 4],
    6: [1, 3]
}

espacio = EspacioDeEstados()
espacio.cargar_grafo_bidireccional(graph)

valor_inicial = 0
valor_final = 5

print("BFS:", espacio.bfs(valor_inicial, valor_final))
print("DFS:", espacio.dfs(valor_inicial, valor_final))
