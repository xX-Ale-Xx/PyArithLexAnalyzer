from tkinter import messagebox


class generarJSON:
    def generar_archivo(self, direccion, lista_errores):

        if lista_errores:
            contenido = '{\n'
            contenido += '\t\"errores\":[\n'
            n = 1

            for producto in lista_errores:
                contenido += self.agregarError(producto, n)
                n += 1
                if (n-1) < len(lista_errores):
                    contenido += ","
                contenido += "\n"


            contenido += '\t]\n'
            contenido += '}'

            with open(direccion, 'w') as file:
                file.write(contenido)
        else:
            messagebox.showinfo("ERROR", "El Archivo no se pudo generar")


    def agregarError(self, error, n):
        contenido = '\t\t{\n'

        contenido += '\t\t\t\"No\":' + str(n) +',\n'
        contenido += '\t\t\t\"descripcion\":{\n'
        contenido += '\t\t\t\t\"lexema\":\"' + error.err() + "\",\n"
        contenido += '\t\t\t\t\"tipo\":\"' + 'error lexico' + "\",\n"
        print(error.getColumna())
        contenido += '\t\t\t\t\"columna\":\"' + str(error.getColumna()) + "\",\n"
        contenido += '\t\t\t\t\"fila\":\"' + str(error.getFila()) + "\"\n"
        contenido += '\t\t\t}\n'

        contenido += '\t\t}'
        return contenido

