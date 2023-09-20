from Abstract import Expression


class Texto(Expression):

    def __init__(self, texto, tipo, fila, columna):
        self.texto = texto
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        pass

    def ejecutarT(self):

        if self.texto != None:
            tipo = self.tipo

        if tipo == "texto":
            return tipo

        elif tipo == "fondo":
            return tipo

        elif tipo == "fuente":
            return tipo

        elif tipo == "forma":
            return tipo

        else:
            None

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()