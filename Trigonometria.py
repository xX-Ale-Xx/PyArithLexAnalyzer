from Abstract import Expression
import math
class Trigonometria(Expression):

    def __init__(self, dato, tipo, fila, columna):
        self.dato = dato
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        value = ''

        if self.dato != None:
            value = self.dato.operar(arbol)

        if self.tipo.operar(arbol).capitalize() == 'Coseno':
            return math.cos(value)
        else:
            return None

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()

