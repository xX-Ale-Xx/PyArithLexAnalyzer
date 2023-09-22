**Manual Técnico**

**Analizador Léxico** 

Nombre: Javier Alejandro Avila Flores

Carnet: 202200392

**Descripción**

El proyecto consiste en un programa que lee código fuente en formato JSON, identifica un lenguaje dado, detecta errores léxicos y ejecuta las instrucciones correspondientes. El programa también genera un archivo de errores en formato JSON.

**Funcionalidad**

El programa se desarrolla en Python utilizando la librería Tkinter para la interfaz gráfica de usuario. El programa reconoce y ejecuta una serie de instrucciones, implementando el análisis léxico correspondiente.

**Características**

- **Carga de código**: El código se carga en un área de texto donde se puede modificar. Se puede guardar el archivo con el mismo nombre o con un nombre diferente.
- **Análisis**: Al analizar el código, se muestran los diagramas del árbol creado de acuerdo con la operación, considerando siempre la jerarquía operacional.
- **Errores**: Los errores encontrados se muestran en un archivo JSON, indicando qué provocó el error.
- **Reporte**: Se generan los diagramas de las operaciones previamente analizadas.

**Menú**

El menú del programa consta de las siguientes opciones:

- **Archivo**: Permite abrir un archivo para editarlo, guardar el archivo que se está editando con el nombre actual o con otro nombre, y cerrar la aplicación.
- **Analizar**: Analiza el texto y muestra los elementos reconocidos.
- **Errores**: Muestra los errores en formato JSON.
- **Reporte**: Genera los diagramas de las operaciones previamente analizadas.


**Clases y Módulos:**

Clase TextEditorApp:

Atributos:

No se especifican atributos en el código.

Métodos:

- \_\_init\_\_(self, root): Inicializa la clase y crea la aplicación principal del editor de texto.
- load\_file(self): Abre un archivo de texto existente.
- save\_file(self): Guarda el contenido actual en un archivo de texto.
- save\_file\_as(self): Guarda el contenido actual en un nuevo archivo de texto.
- cut\_text(self): Corta el texto seleccionado.
- copy\_text(self): Copia el texto seleccionado.
- paste\_text(self): Pega el texto copiado o cortado.
- undo\_action(self): Deshace la acción anterior.
- redo\_action(self): Rehace la acción deshecha anteriormente.
- find\_text(self): Abre una ventana para buscar texto en el documento.
- replace\_text(self): Abre una ventana para reemplazar texto en el documento.
- Graphviz(self, respuestas\_Operaciones): Genera un diagrama Graphviz según las respuestas de operaciones.
- create\_menu(self): Crea el menú principal de la aplicación.

Clase generarJSON:

Atributos:

No se especifican atributos en el código.

Métodos:

- generar\_archivo(self, direccion, lista\_errores): Genera un archivo JSON a partir de una lista de errores.
- agregarError(self, error, n): Agrega un error a la estructura JSON.

Clase Analizador:

Atributos:

- reserved: Un diccionario que almacena palabras reservadas y sus correspondientes nombres de token.
- lexemas: Una lista de nombres de tokens.
- n\_linea: Un contador de número de línea.
- n\_columna: Un contador de número de columna.
- lista\_lexemas: Una lista que almacena instancias de la clase Lexema.
- instrucciones: Una lista que almacena instrucciones generadas.
- lista\_errores: Una lista que almacena instancias de la clase Errores.

Métodos:

- instruccion(self, cadena): Analiza una cadena de entrada y genera una lista de lexemas.
- armar\_lexema(self, cadena): Convierte una cadena en un lexema.
- armar\_numero(self, cadena): Convierte una cadena en un número.
- operar(self): Analiza la lista de lexemas y genera instrucciones.
- operar\_(): Realiza la operación principal de análisis y generación de instrucciones.
- getErrores(self): Retorna la lista de errores encontrados durante el análisis.

Clase Expression (Clase Abstracta):

Atributos:

- fila: Almacena la fila de inicio de la expresión.
- columna: Almacena la columna de inicio de la expresión.

Métodos:

- operar(self, arbol): Método abstracto que debe ser implementado por las clases hijas.
- getFila(self): Retorna la fila de inicio.
- getColumna(self): Retorna la columna de inicio.

Clase Lexema:

Atributos:

- lexema: Almacena el lexema como una cadena de caracteres.

Métodos:

- operar(self, arbol): Retorna el lexema.
- isTrigonometria(self): Verifica si el lexema es una función trigonométrica.
- getFila(self): Retorna la fila de inicio.
- getColumna(self): Retorna la columna de inicio.

Clase Numero:

Atributos:

- valor: Almacena el valor numérico.

Métodos:

- operar(self, arbol): Retorna el valor numérico.
- getFila(self): Retorna la fila de inicio.
- getColumna(self): Retorna la columna de inicio.

Clase Aritmetica

Atributos:

- left: Representa la parte izquierda de la operación.
- right: Representa la parte derecha de la operación.
- tipo: Representa el tipo de operación aritmética.

Métodos:

- operar(self, arbol): Realiza la operación aritmética especificada y retorna el resultado.
- getFila(self): Retorna la fila de inicio.
- getColumna(self): Retorna la columna de inicio.

Clase Errores:

Atributos:

- lexema: Almacena el lexema que causó el error.

Métodos:

- operar(self, no): Retorna un mensaje de error que incluye el lexema.
- err(self): Retorna el lexema que causó el error.
- getColumna(self): Retorna la columna de inicio.
- getFila(self): Retorna la fila de inicio.

Clase Texto:

Atributos:

- texto: Almacena el texto.
- tipo: Almacena el tipo de texto.

Métodos:

- operar(self, arbol): No implementado en el código proporcionado.
- ejecutarT(self): Retorna el tipo de texto (texto, fondo, fuente o forma).
- getFila(self): Retorna la fila de inicio.
- getColumna(self): Retorna la columna de inicio.

Clase Trigonometria

Atributos:

- dato: Representa el valor numérico sobre el cual se aplicará la función trigonométrica.
- tipo: Representa el tipo de función trigonométrica.

Métodos:

- operar(self, arbol): Realiza la operación trigonométrica especificada y retorna el resultado.
- getFila(self): Retorna la fila de inicio.
- getColumna(self): Retorna la columna de inicio.

Diagrama de clases:

![](Aspose.Words.68f7558d-41fb-4272-a400-1a77294035ab.001.png)
