from Abstract import Expression
import math
class Aritmetica(Expression):
    def __init__(self, left, right, tipo, fila, columna):
        self.left = left
        self.right = right
        self.dato = None
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        leftValue = ''
        rightValue = ''

        if self.left != None:
            leftValue = self.left.operar(arbol)
        if self.right != None:
            rightValue = self.right.operar(arbol)

        if self.tipo.operar(arbol).capitalize() == 'Suma':
            return round(leftValue + rightValue,2)
        elif self.tipo.operar(arbol).capitalize() == 'Resta':
            return round(leftValue - rightValue,2)
        elif self.tipo.operar(arbol).capitalize() == 'Multiplicacion':
            return round(leftValue * rightValue,2)
        elif self.tipo.operar(arbol).capitalize() == 'Division':
            return round(leftValue / rightValue,2)
        elif self.tipo.operar(arbol).capitalize() == 'Potencia':
            return round(leftValue ** rightValue,2)
        elif self.tipo.operar(arbol).capitalize() == 'Mod':
            return round(leftValue % rightValue, 2)
        else:
            return None

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()

