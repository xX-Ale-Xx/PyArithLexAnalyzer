import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
from Analizador import intruccion, getErrores, operar_
from GenerarJSON import generarJSON
from PIL import Image

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto")
        self.root.iconbitmap('vision.ico')

        self.line_number_bar = tk.Text(root, width=4, padx=4, takefocus=0, border=0, background='#B2AEAD', state='disabled')
        self.line_number_bar.pack(side=tk.LEFT, fill=tk.Y)

        self.text_widget = ScrolledText(self.root, wrap=tk.WORD)
        self.text_widget.pack(expand=True, fill='both')

        self.text_widget.bind('<Key>', self.update_line_numbers)
        self.text_widget.bind('<MouseWheel>', self.update_line_numbers)
        self.current_line = 1

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Guardar", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.root.quit)
        self.menu_bar.add_command(label="Analizar", command=self.analizar)
        self.menu_bar.add_command(label="Errores", command=self.Errores)
        self.menu_bar.add_command(label="Graficar", command=self.gh)

    def open_file(self):

        file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                #self.data = content
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)
            self.update_line_numbers()
        self.data = self.text_widget.get(1.0, tk.END)



    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
        if file_path:
            content = self.text_widget.get(1.0, tk.END)
            with open(file_path, 'w') as file:
                file.write(content)
            messagebox.showinfo("Guardado", "Archivo guardado exitosamente.")

    def update_line_numbers(self, event=None):
        line_count = self.text_widget.get('1.0', tk.END).count('\n')
        if line_count != self.current_line:
            self.line_number_bar.config(state=tk.NORMAL)
            self.line_number_bar.delete(1.0, tk.END)
            for line in range(1, line_count + 1):
                self.line_number_bar.insert(tk.END, f"{line}\n")
            self.line_number_bar.config(state=tk.DISABLED)
            self.current_line = line_count

    def analizar(self):
        try:
            instrucciones = intruccion(self.data)
            respuestas_Operaciones = operar_()

            Resultados = ''
            Operacion = 1

            configuracion = 1
            salto = "\n"

            for respuesta in respuestas_Operaciones:

                if isinstance(respuesta.operar(None), int) or isinstance(respuesta.operar(None), float) == True:
                    Resultados += str(f"Operacion {Operacion} --> {respuesta.tipo.operar(None)} = {respuesta.operar(None)}\n")
                    print(respuesta.operar(None))
                    Operacion += 1



            messagebox.showinfo("Analisis Exitoso", Resultados)
        except ValueError:
            print(ValueError)
            messagebox.showinfo("Error", "No se ha ingresado ningun archivo")

    def Errores(self):
        lista_errores = getErrores()
        generar = generarJSON()
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos JSON", "*.json")])
        if file_path:
            generar.generar_archivo(file_path,lista_errores)
            messagebox.showinfo("Guardado", "Archivo guardado exitosamente.")
        else:
            messagebox.showinfo("ERROR", "El Archivo no se pudo generar")
        for error in lista_errores:
            cont = 1
            er = error.operar(cont)
            cont += 1
            print(er)

    def gh(self):
        try:
            operar_().clear()

            intrucciones = intruccion(self.data)
            respuestas_Operaciones = operar_()

            contenido = "digraph G {\n\n"
            r = open("Operaciones.dot", "w", encoding="utf-8")
            contenido += str(Graphviz(respuestas_Operaciones))
            contenido += '\n}'

            r.write(contenido)
            r.close()

            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Archivos png", "*.png")])
            if file_path:
                with open("Operaciones.dot", "w") as archivo:
                    archivo.write(contenido)
                os.system(f"dot -Tpng Operaciones.dot -o {file_path}")
                print("¡Gráfica generada en Operaciones.png!")
                try:
                    img = Image.open(file_path)
                    img.show()  # Mostrar la imagen
                    print(f"¡Gráfica generada y abierta en {file_path}!")
                except Exception as e:
                    print(f"Error al abrir la imagen: {str(e)}")
            else:
                messagebox.showinfo("ERROR", "El Archivo no se pudo generar")


        except Exception as e:
            messagebox.showinfo("Se produjo un error: ", str(e))
            messagebox.showinfo("Mensaje", f"Error al generar el archivo de salida, Verificar el Archivo de entrada.")
        else:
            messagebox.showinfo("Mensaje", "Grafica generada con exito")
            respuestas_Operaciones.clear()
            intrucciones.clear()


def Graphviz(respuestas_Operaciones):
    Titulo = ""
    colorNodo = ""
    fuenteNodo = ""
    formaNodo = ""
    try:
        print('---------------------------------------------')
        for respuesta in respuestas_Operaciones:
            if isinstance(respuesta.operar(None), int) or isinstance(respuesta.operar(None), float) == True:
                pass
            else:
                temporal = str(respuesta.texto.operar(None)).lower()
                print(respuesta.texto.operar(None))
                print(respuesta.ejecutarT())
                if respuesta.ejecutarT() == "texto":  # Podemos recibir cualquier texto
                    Titulo = str(respuesta.texto.operar(None))
                if respuesta.ejecutarT() == "color-fondo-nodo":  # Vericar el color del nodo a asignar
                    if temporal == ("amarillo" or "yellow"):
                        temporal = "yellow"
                        colorNodo = temporal
                    elif temporal == ("verde" or "green"):
                        temporal = "green"
                        colorNodo = temporal
                    elif temporal == ("azul" or "blue"):
                        temporal = "blue"
                        colorNodo = temporal
                    elif temporal == ("rojo" or "red"):
                        temporal = "red"
                        colorNodo = temporal
                    elif temporal == ("morado" or "purple"):
                        temporal = "purple"
                        colorNodo = temporal
                print(colorNodo)
                if respuesta.ejecutarT() == "color-fuente-nodo":  # Vericar la fuente del nodo a asignar

                    if temporal == ("amarillo" or "yellow"):
                        temporal = "yellow"
                        fuenteNodo = temporal
                    elif temporal == ("verde" or "green"):
                        temporal = "green"
                        fuenteNodo = temporal
                    elif temporal == ("azul" or "blue"):
                        temporal = "blue"
                        fuenteNodo = temporal
                    elif temporal == ("rojo" or "red"):
                        temporal = "red"
                        fuenteNodo = temporal
                    elif temporal == ("morado" or "purple"):
                        temporal = "purple"
                        fuenteNodo = temporal
                    elif temporal == ("negro" or "black"):
                        temporal = "black"
                        fuenteNodo = temporal

                if respuesta.ejecutarT() == "forma-nodo":  # Vericar el formato de nodo a asignar
                    if temporal == ("circulo" or "circle"):
                        temporal = "circle"
                        formaNodo = temporal
                    elif temporal == ("cuadrado" or "square"):
                        temporal = "square"
                        formaNodo = temporal
                    elif temporal == ("triangulo" or "triangle"):
                        temporal = "triangle"
                        formaNodo = temporal
                    elif temporal == ("rectangulo" or "box"):
                        temporal = "box"
                        formaNodo = temporal
                    elif temporal == ("elipse" or "ellipse"):
                        temporal = "ellipse"
                        formaNodo = temporal

        temporal = ''
        CnumIzquierdo = 0
        CnumDerecho = 0
        Crespuesta = 0
        Ctotal = 0

        text = ""
        text += f"\tnode [shape={formaNodo}]\n"
        # text += f"\tnode [shape=box];\n"

        text += f"\tnodo0 [label = \"{Titulo}\"]\n"
        text += f"\tnodo0" + "[" + f"fontcolor = {fuenteNodo}" + "]\n"
        # text += f"\tnodo0 [label = \"CambiarPorTexto\"]\n"    # ESTE DEJAR

        for respuesta in respuestas_Operaciones:
            CnumIzquierdo += 1
            CnumDerecho += 1
            Crespuesta += 1
            Ctotal += 1

            if isinstance(respuesta.operar(None), int) or isinstance(respuesta.operar(None), float) == True:

                text += f"\tnodoRespuesta{Crespuesta}" + "[" + f"style = filled" + f",fillcolor = {colorNodo}" + f",fontcolor = {fuenteNodo}" + "]\n"
                text += f"\tnodoIzqu{CnumIzquierdo}" + "[" + f"style = filled" + f",fillcolor = {colorNodo}" + f",fontcolor = {fuenteNodo}" + "]\n"
                text += f"\tnodoDere{CnumDerecho}" + "[" + f"style = filled" + f",fillcolor = {colorNodo}" + f",fontcolor = {fuenteNodo}" + "]\n"
                text += f"\tnodoT{Ctotal}" + "[" + f"style = filled" + f",fillcolor = {colorNodo}" + f",fontcolor = {fuenteNodo}" + "]\n"

                text += f"\tnodoRespuesta{Crespuesta}" + f"[label = \"{str(respuesta.tipo.operar(None))}: " + "\"]\n"
                text += f"\tnodoIzqu{CnumIzquierdo}" + "[label = \"Valor1: " + f" {str(respuesta.left.operar(None))} " + "\"]\n"
                text += f"\tnodoDere{CnumDerecho}" + "[label = \"Valor2: " + f" {str(respuesta.right.operar(None))} " + "\"]\n"

                text += f"\tnodoRespuesta{Crespuesta} -> nodoIzqu{CnumIzquierdo}\n"
                if CnumDerecho:
                  text += f"\tnodoRespuesta{Crespuesta} -> nodoDere{CnumDerecho}\n"

                text += f"\tnodoT{Ctotal}" + f"[label = \"{respuesta.operar(None)}" + "\"]\n"
                text += f"\tnodoT{Ctotal} -> nodoRespuesta{Crespuesta}\n"

            else:
                pass

        return text
    except Exception as e:
        messagebox.showinfo("Se produjo un error: ", str(e))
        messagebox.showinfo("Mensaje", "Error en los comandos de Graphviz")


if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()