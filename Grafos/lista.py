# lista = []
# lista.append(5)
# print(lista)

class duallist:
    one = []
    two = []

    def __int__(self, dato1, dato2):
        self.one[0] = dato1
        self.two[0] = dato2

    def imprimir(self): 
        print(self.one[0])
        print(self.two[0])


mid = duallist(6,7)
mid.imprimir()