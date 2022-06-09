class Grafo:
    vertices = None
    aristas = None
    CantVertices = None

    def __init__(self):
        self.vertices = []
        self.aristas = []
        self.CantVertices = 0

    def agregarvertice(self, vertic):
        if not (self.existevertice(vertic)):
            self.vertices.append(vertic)
            self.CantVertices += 1

    def ververtices(self):
        if self.CantVertices > 0:
            for i in range(self.vertices.__len__()):
                print(self.vertices[i], end=",")
            print("\n")

    def vertices(self):
        if self.CantVertices > 0:
            return self.vertices

    def posicionvertice(self, valor):
        for i in range(self.vertices.__len__()):
            if self.vertices[i] == valor:
                return i
    def existevertice(self, vertic):
        return vertic in self.vertices

    def agregararistas(self, origen, fin):
        fila = self.posicionvertice(origen)
        columna = self.posicionvertice(fin)
        self.aristas[fila][columna] = 1
        fila = self.posicionvertice(fin)
        columna = self.posicionvertice(origen)
        self.aristas[fila][columna] = 1

    def veraristas(self):
        for i in range(self.CantVertices):
            for j in range(self.CantVertices):
                print(self.aristas[i][j], end=",")
            print("\n")



miGrafo = Grafo()