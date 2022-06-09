class grafos:
    vertices = []
    aristas = []
    CantVertices = 0

    def __init__(self):
        self.CantVertices = 0

    def agregarvertice(self, vertic):
        if not (self.existevertice(vertic)):
            self.vertices.append(vertic)
            self.CantVertices += 1
            matriz = []
            for i in range(self.CantVertices):
                matriz.append([0] * self.CantVertices)

            for i in range(self.CantVertices-1):
                for j in range(self.CantVertices-1):
                    matriz[i][j] = self.aristas[i][j]
            self.aristas = matriz

    def ververtices(self):
        if self.CantVertices > 0:
            for i in range(self.vertices.__len__()):
                print(self.vertices[i], end=",")
            print("\n")

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



miGrafo = grafos()
miGrafo.agregarvertice(3)
miGrafo.agregarvertice(2)
miGrafo.agregarvertice(1)
miGrafo.agregarvertice(5)
miGrafo.agregarvertice(4)
miGrafo.agregararistas(3, 2)
miGrafo.agregararistas(3, 4)
miGrafo.agregararistas(2, 1)
miGrafo.agregararistas(2, 3)
miGrafo.agregararistas(2, 4)
miGrafo.agregararistas(2, 5)
miGrafo.agregararistas(1, 2)
miGrafo.agregararistas(1, 5)
miGrafo.agregararistas(4, 2)
miGrafo.agregararistas(4, 3)
miGrafo.agregararistas(4, 5)
miGrafo.agregararistas(5, 1)
miGrafo.agregararistas(5, 2)
miGrafo.agregararistas(5, 4)
miGrafo.ververtices()
miGrafo.veraristas()

# print(miGrafo.existevertice(3))


