from Abstract import Expression

class Lexema(Expression):

    def __init__(self, lexema,  fila, columna):
        self.lexema = lexema

        super().__init__(fila, columna)

    def operar(self, arbol):   #! Retorna mi Lexema
        return self.lexema

    def isTrigonometria(self):
        return self.lexema.capitalize() == 'Coseno' or self.lexema.capitalize() == 'Seno' or self.lexema.capitalize() == 'Tangente'

    def getFila(self):              #! Retorna la fila
        return super().getFila()

    def getColumna(self):           #! Retorna la columna
        return super().getColumna()