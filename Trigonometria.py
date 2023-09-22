from Abstract import Expression
import math
class Trigonometria(Expression):

    def __init__(self, dato, tipo, fila, columna):
        self.dato = dato
        self.tipo = tipo
        self.left = None
        self.right = None
        super().__init__(fila, columna)

    def operar(self, arbol):
        value = ''

        if self.dato != None:
            value = self.dato.operar(arbol)

        if self.tipo.operar(arbol).capitalize() == 'Coseno':

            return round(math.cos(value),2)
        elif self.tipo.operar(arbol).capitalize() == 'Seno':

            return round(math.sin(value),2)
        elif self.tipo.operar(arbol).capitalize() == 'Tangente':

            return round(math.tan(value),2)
        elif self.tipo.operar(arbol).capitalize() == 'Raiz':
            return round(math.sqrt(value),2)
        elif self.tipo.operar(arbol).capitalize() == 'Inverso':
            return round((1/value),2)
        else:
            return None

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()


