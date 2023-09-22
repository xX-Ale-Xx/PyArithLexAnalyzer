



##**Manual de usuario**

####**Analizador Léxico** 
![](Aspose.Words.69513629-615b-4419-ba06-8c541b792e78.001.png)











Nombre: Javier Alejandro Avila Flores

Carnet: 202200392





Introducción:

Este manual de usuario tiene como objetivo proporcionarte la información necesaria para utilizar el Analizador Léxico en Python desarrollado para identificar lenguajes de programación, detectar errores léxicos y ejecutar instrucciones correspondientes. Este programa toma como entrada código fuente en formato JSON y lleva a cabo un análisis exhaustivo de su estructura y contenido.

Descripción:

El Analizador Léxico es capaz de leer código fuente en formato JSON y determinar el lenguaje de programación contenido en el archivo. Además, identifica y notifica los errores léxicos que puedan estar presentes en el código. El programa ejecuta las instrucciones especificadas en el código, generando resultados y representando visualmente la jerarquía operacional de cada instrucción en un archivo gráfico.

Los errores léxicos detectados durante el proceso de análisis se registran en un archivo JSON, proporcionando información detallada sobre la naturaleza y ubicación de los errores.











Funcionalidad:

Este proyecto se ha implementado en Python haciendo uso de la librería Tkinter para proporcionar una interfaz de usuario intuitiva. El Analizador Léxico es capaz de reconocer diferentes instrucciones y ejecutarlas según su estructura y lenguaje asociado. La aplicación muestra resúmenes de errores detectados y resultados de las operaciones realizadas en cada función.

Un aspecto destacado de esta aplicación es la representación gráfica de la jerarquía operacional de las instrucciones en forma de árbol de operaciones, incluyendo los resultados en cada nodo correspondiente. Esto se logra mediante la librería Graphviz.

Además, la aplicación permite cargar, modificar y guardar archivos de código fuente en un área de texto. Puedes guardar archivos con el mismo nombre o con uno diferente. Al analizar el código, se generan automáticamente diagramas de árbol y se registran los errores en un archivo JSON.

En resumen, el Analizador Léxico en Python ofrece una solución completa para analizar y comprender código fuente en formato JSON, brindando resultados claros y visuales, así como un registro detallado de errores léxicos.

Uso básico:

Al abrir el programa se mostrará la siguiente ventana:

![](Aspose.Words.69513629-615b-4419-ba06-8c541b792e78.002.png)

En la cual estarán las siguientes opciones:

![](Aspose.Words.69513629-615b-4419-ba06-8c541b792e78.003.png)

Archivo:

`    `• Abrir: Permite abrir un archivo para poder seguir editándolo en la

`      `Aplicación

`      `![](Aspose.Words.69513629-615b-4419-ba06-8c541b792e78.004.png)

`      `![](Aspose.Words.69513629-615b-4419-ba06-8c541b792e78.005.png)



`    `• Guardar: Permite guardar el archivo que está siendo editado con el

`      `nombre actual.

`    `• Guardar como: Permite guardar el archivo que está siento editado con

`      `otro nombre.

`      `![](Aspose.Words.69513629-615b-4419-ba06-8c541b792e78.006.png)

`    `• Salir: Con esta opción se cerrará la aplicación.

`     `![](Aspose.Words.69513629-615b-4419-ba06-8c541b792e78.007.png)

![](Aspose.Words.69513629-615b-4419-ba06-8c541b792e78.008.png)

Analizar: Analizará el texto y mostrará los elementos reconocidos.

![](Aspose.Words.69513629-615b-4419-ba06-8c541b792e78.009.png)

Errores: Muestra los errores con el formato JSON.

![](Aspose.Words.69513629-615b-4419-ba06-8c541b792e78.010.png)

Reporte: Generar los diagramas de las operaciones previamente analizadas

![](Aspose.Words.69513629-615b-4419-ba06-8c541b792e78.011.png)

Ver manuales: Nos enviara al repositorio de GitHub donde podremos ver los manuales de usuario y manuales técnicos.



