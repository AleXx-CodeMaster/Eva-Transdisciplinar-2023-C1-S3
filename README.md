1.      MRUA-SIMULATOR (Eva-Transdiciplinario-2023-CI-S3)
Descripción: El movimiento rectilíneo uniforme acelerado (MRUA) es un tipo de movimiento en el que un objeto se desplaza a lo largo de una línea recta con una aceleración constante. En este tipo de movimiento, la velocidad del objeto cambia de manera uniforme a medida que pasa el tiempo.

En el **MRUA**, el objeto experimenta una **aceleración constante**, lo que significa que la magnitud de su velocidad cambia de manera uniforme en intervalos de tiempo iguales. La aceleración puede ser **positiva o negativa**, dependiendo de la dirección en la que se aplique.

Durante el MRUA, se pueden observar las siguientes características:

**Posición inicial**: Es la posición del objeto en el inicio del movimiento. Se representa usualmente con la letra "x₀".

**Velocidad**: Es la magnitud de la rapidez con la que el objeto se desplaza. Se representa con la letra "V". En el MRUA, la velocidad cambia de manera constante, incrementándose o disminuyendo según la dirección de la aceleración. la velocidad se divide en tres variables las cuales son: 

** "Vo" **: velocidad inicial del movimiento, esta es en linea recta aplicandose en el MRUA, esta puede ser tanto negativa como positiva puesto que depende de la aceleracion y en si su sentido u orientacion.

** "Vf" **: velocidad final, este es el resultado luego de experimentar una aceleracion que puede ser negativa o positiva, en pocas palabras es el resultante de la velocidad al sufrir un cambio provocado por una fuerza externa (aceleracion).

** "VF**2" **: velocidad final al cuadrado, tal como dice el nombre es solo la velocidad final pero elevada 2, esta misma sirve para calcular velocidad final teniendo alguna incognita o bien para comparar magnitudes de velocidad.
    
**Aceleración**: Es la tasa de cambio de la velocidad. Se representa con la letra "a". Si la aceleración es positiva, el objeto aumentará su velocidad en el tiempo, mientras que si es negativa, disminuirá su velocidad. la aceleración misma posee un limite el cual se dicta al momento de ejercer una fuerza sobre un objeto, pero si no existe una fuerza externa que se aplique sobre un objeto este estará en reposo y no tendra cambio en aceleración, ni en velocidad.
    
**Tiempo**: Es el intervalo de tiempo transcurrido desde el inicio del movimiento. Se representa con la letra "t".
    
 **Desplazamiento**: Es la variación en la posición del objeto durante un determinado intervalo de tiempo. Se representa con la letra "Δx" o simplemente "x". En el MRUA, el desplazamiento puede ser positivo o negativo, dependiendo de la dirección del movimiento.

En este trabajo planeamos simular un auto en el cual su trayectoria sea una aceleración constante en una linea recta, en donde se experimentará el MRUA con una aceleración constante positiva. En este caso, la velocidad del automóvil aumenta gradualmente, la idea principal es que el usuario pueda ingresar valores los cuales iran alterando su velocidad, su desplazamiento, la posición y la aceleración de manera gradual, todo esto siguiendo las reglas del Fenómeno Físico Mencionado.

3.      Evento Físico a simular: MOVIMIENTO RECTILINEO UNIFORME ACELERADO

**A.      Breve historia asociada**:

El concepto del movimiento rectilíneo uniforme acelerado (MRUA) se deriva de la comprensión de la cinemática y las leyes del movimiento formuladas por Isaac Newton.

En el siglo XVII, Isaac Newton desarrolló las leyes del movimiento que establecen las relaciones fundamentales entre la fuerza, la masa y la aceleración de un objeto. Sus leyes sentaron las bases para la comprensión de los diferentes tipos de movimientos.

El MRUA es una variante específica del movimiento en línea recta, en la cual un objeto experimenta una aceleración constante. La aceleración representa el cambio en la velocidad de un objeto a lo largo del tiempo. En el caso del MRUA, la aceleración se mantiene constante, lo que significa que la velocidad del objeto aumenta o disminuye de manera uniforme en cada unidad de tiempo.

El estudio y la descripción matemática del MRUA se basan en la segunda ley del movimiento de Newton, que establece que la fuerza neta aplicada sobre un objeto es igual al producto de su masa y su aceleración. Esta relación se expresa en la fórmula:

**Fuerza neta = masa × aceleración**

A partir de esta relación, podemos deducir que si la fuerza neta aplicada a un objeto es constante y no hay fuerzas adicionales que actúen sobre él, el objeto experimentará una aceleración constante. Esta aceleración constante resulta en un MRUA.

El MRUA se ha estudiado y aplicado en numerosas áreas de la física y la ingeniería, como la descripción del movimiento de objetos en caída libre, el movimiento de proyectiles y el análisis de vehículos y maquinaria en movimiento.

En resumen, el concepto del movimiento rectilíneo uniforme acelerado surgió de la formulación de las leyes del movimiento por Isaac Newton y la comprensión de cómo una fuerza neta constante produce una aceleración constante en un objeto en movimiento rectilíneo.

**B.      Matemática empleada**:
Todas las ecuaciones que describen el Movimiento Rectilíneo Uniforme Acelerado (MRUA):

1. Ecuación de la velocidad:
   **v = v₀ + a * t**

   Donde:
   - v es la velocidad en un momento dado.
   - v₀ es la velocidad inicial.
   - a es la aceleración constante.
   - t es el tiempo transcurrido desde el inicio del movimiento.

2. Ecuación del desplazamiento:
   **x = x₀ + v₀ * t + 0.5 * a * t²**

   Donde:
   - x es el desplazamiento en un momento dado.
   - x₀ es la posición inicial.
   - v₀ es la velocidad inicial.
   - a es la aceleración constante.
   - t es el tiempo transcurrido desde el inicio del movimiento.

3. Ecuación de la velocidad al cuadrado:
   **v² = v₀² + 2 * a * Δx**

   Donde:
   - v es la velocidad en un momento dado.
   - v₀ es la velocidad inicial.
   - a es la aceleración constante.
   - Δx es el cambio en el desplazamiento desde el inicio del movimiento.

4. Ecuación de la posición en función del tiempo:
   **x = x₀ + v₀ * t + 0.5 * a * t²**

   Esta es la misma ecuación del desplazamiento, pero se puede utilizar para encontrar la posición en función del tiempo.

5. Ecuación de la aceleración en función del cambio de velocidad y tiempo:
   **a = (v - v₀) / t**

   Donde:
   - a es la aceleración media en un intervalo de tiempo.
   - v es la velocidad final.
   - v₀ es la velocidad inicial.
   - t es el tiempo transcurrido.

Estas ecuaciones son fundamentales para describir el MRUA y permiten calcular diferentes variables del movimiento, como la velocidad, el desplazamiento, la posición y la aceleración, en función de los valores iniciales y el tiempo transcurrido.

**C.      **Como se resuelve****:

Para resolver las ecuaciones del Movimiento Rectilíneo Uniforme Acelerado (MRUA), se deben seguir los siguientes pasos:

**1. Identificar las variables conocidas**: Determina qué variables se conocen en el problema y cuáles se desconocen. Las variables pueden ser la velocidad final (v), velocidad inicial (v₀), aceleración (a), tiempo transcurrido (t), posición inicial (x₀) o desplazamiento (x).

**2. Seleccionar la ecuación adecuada**: Elije la ecuación que contenga las variables conocidas y la variable desconocida que deseas calcular.

**3. Despejar la variable desconocida**: Reorganiza la ecuación para aislar la variable desconocida en un lado de la ecuación. Esto implica realizar operaciones algebraicas para dejar la variable deseada sola en un lado de la ecuación y las variables conocidas en el otro lado.

**4. Sustituir los valores conocidos**: Una vez que hayas despejado la variable desconocida, sustituye los valores conocidos en la ecuación.

**5. Realizar los cálculos**: Realiza las operaciones matemáticas necesarias para calcular el valor de la variable desconocida.

**6. Verificar unidades**: Asegúrate de que todas las unidades estén correctamente expresadas y, si es necesario, realiza conversiones de unidades antes de realizar los cálculos.

**7. Interpretar el resultado**: Analiza el valor obtenido y considera su significado en el contexto del problema. Asegúrate de proporcionar la respuesta con la unidad correcta y el sentido adecuado según el contexto.

**8. Repetir el proceso si es necesario**: Si el problema requiere calcular más de una variable desconocida, repite los pasos anteriores utilizando las ecuaciones adecuadas hasta que todas las incógnitas sean resueltas.

Es importante recordar que las ecuaciones del MRUA **son válidas siempre y cuando la aceleración sea constante**. Si la aceleración no es constante, se requieren ecuaciones diferentes y, en algunos casos, métodos numéricos o gráficos más complejos para resolver el problema.

**D.      Aplicaciones**:

El Movimiento Rectilíneo Uniforme Acelerado (MRUA) se puede aplicar en una amplia variedad de situaciones en las que un objeto se desplaza a lo largo de una trayectoria recta y experimenta una aceleración constante. Algunos ejemplos de situaciones en las que se puede aplicar el MRUA son:

**1.  Caída libre**: Cuando un objeto cae libremente bajo la influencia de la gravedad, sufre un MRUA con una aceleración constante hacia abajo. Esto ocurre, por ejemplo, cuando dejamos caer un objeto desde cierta altura sin aplicarle ninguna fuerza adicional.
    
**2.  Lanzamiento vertical hacia arriba:** Al lanzar un objeto verticalmente hacia arriba, experimenta una aceleración constante hacia abajo debido a la gravedad. En la fase ascendente, su velocidad disminuye gradualmente hasta alcanzar el punto más alto, donde su velocidad es cero. Luego, en la fase descendente, el objeto acelera hacia abajo debido a la gravedad.
    
**3.  Frenado de un vehículo:** Cuando un automóvil se desplaza a lo largo de una carretera recta y aplica los frenos, experimenta un MRUA con una aceleración negativa (opuesta a la dirección del movimiento). La velocidad del automóvil disminuye gradualmente hasta detenerse.
    
**4.  Aceleración de un automóvil:** Cuando un automóvil se acelera en línea recta, experimenta un MRUA con una aceleración constante positiva. En este caso, la velocidad del automóvil aumenta gradualmente.
    
**5.  Ascensor en movimiento:** Cuando un ascensor sube o baja a lo largo de una guía vertical, los pasajeros en su interior experimentan un MRUA. Durante el ascenso, sienten una aceleración hacia arriba, mientras que durante el descenso, sienten una aceleración hacia abajo.
    
**6.  Proyectiles en el aire:** Cuando un objeto se lanza horizontalmente o en un ángulo, sigue una trayectoria parabólica y experimenta un MRUA en la dirección vertical. La aceleración en la dirección vertical es causada por la gravedad, que actúa hacia abajo.



5.      Programación

a.      Descripción de las herramientas utilizadas

 Lenguaje de programacion usado: "Python"
 
 Python es un lenguaje de programación interpretado, de alto nivel y de propósito general. Fue creado por Guido van Rossum y lanzado por primera vez en 1991. A lo largo de los años, Python se ha vuelto muy popular debido a su simplicidad, legibilidad de código y enfoque en la facilidad de uso.

Características clave de Python:

1. Legibilidad de código: Python se destaca por su sintaxis limpia y legible, lo que facilita la lectura y comprensión del código. Utiliza una estructura de indentación significativa en lugar de llaves o palabras clave para definir bloques de código, lo que promueve la escritura de código limpio y estructurado.

2. Fácil de aprender: Python tiene una curva de aprendizaje suave y es considerado un lenguaje ideal para principiantes. Su sintaxis clara y expresiva permite a los programadores concentrarse en la resolución de problemas en lugar de preocuparse por detalles sintácticos complejos.

3. Versatilidad: Python es un lenguaje de propósito general, lo que significa que se puede utilizar en una amplia gama de aplicaciones. Puede ser utilizado para desarrollar aplicaciones web, aplicaciones de escritorio, análisis de datos, inteligencia artificial, scripting, automatización, entre otros.

4. Bibliotecas y frameworks: Python cuenta con una amplia gama de bibliotecas y frameworks que facilitan el desarrollo de diversas aplicaciones. Algunos ejemplos populares son Django y Flask para el desarrollo web, NumPy y Pandas para el análisis de datos, TensorFlow y PyTorch para el aprendizaje automático, y muchas más.

5. Portabilidad: Python es un lenguaje multiplataforma, lo que significa que los programas escritos en Python pueden ejecutarse en diferentes sistemas operativos como Windows, macOS y Linux sin necesidad de realizar modificaciones significativas en el código.

6. Comunidad activa: Python tiene una comunidad de desarrolladores muy activa y comprometida. Esto se traduce en una amplia disponibilidad de recursos, documentación, tutoriales y una gran cantidad de bibliotecas y frameworks desarrollados por la comunidad.

En general, Python se destaca por su enfoque en la legibilidad, simplicidad y productividad. Es ampliamente utilizado en diferentes industrias y áreas, desde desarrollo web y científico hasta inteligencia artificial y automatización, lo que lo convierte en uno de los lenguajes de programación más populares y relevantes en la actualidad.


-LIBRERIAS

 Tkinter:
   - Tkinter es una biblioteca estándar de Python que se utiliza para crear interfaces gráficas de usuario (GUI, por sus siglas en inglés).
   - Proporciona un conjunto de widgets y herramientas para construir ventanas, botones, etiquetas, campos de entrada, menús y más elementos interactivos en una interfaz gráfica.
   - Tkinter se basa en la biblioteca Tcl/Tk, que es una herramienta popular para crear GUIs. Proporciona una capa de interfaz de Python para interactuar con Tcl/Tk.
   - Con Tkinter, puedes crear aplicaciones de escritorio con una interfaz gráfica intuitiva y visualmente atractiva.
   - Tkinter se utiliza ampliamente debido a su facilidad de uso y su integración nativa con Python.
   - Puedes utilizar Tkinter para desarrollar aplicaciones simples o complejas, desde herramientas utilitarias hasta aplicaciones empresariales.

 PIL (Python Imaging Library):
   - PIL (Python Imaging Library) es una biblioteca de procesamiento de imágenes de código abierto para Python.
   - Proporciona una amplia gama de funciones y herramientas para abrir, manipular, mejorar y guardar imágenes en varios formatos.
   - PIL permite realizar operaciones básicas en imágenes, como recortar, redimensionar, rotar, ajustar el brillo y el contraste, cambiar el formato de archivo, entre otras.
   - También ofrece funcionalidades avanzadas, como el filtrado de imágenes, la composición de imágenes, la manipulación de píxeles y la generación de gráficos simples.
   - PIL es ampliamente utilizada en aplicaciones que requieren manipulación de imágenes, como procesamiento de imágenes médicas, visión por computadora, generación de gráficos y diseño web.
   - Sin embargo, ten en cuenta que PIL no se ha actualizado desde 2011. Ha sido reemplazada por Pillow, que es una bifurcación de PIL que proporciona mejoras y mantenimiento continuo. Pillow es compatible con la mayoría 
    de las funciones de PIL y se recomienda su uso en lugar de PIL.

En resumen, tkinter es una biblioteca para crear interfaces gráficas de usuario en Python, mientras que PIL (o su bifurcación Pillow) es una biblioteca para el procesamiento y manipulación de imágenes en Python. Ambas bibliotecas son muy útiles en diferentes contextos de desarrollo de aplicaciones.

b.      Guia  de  instalación:

1. Instalación de Python:
   - Ve al sitio web oficial de Python en https://www.python.org/downloads/ y descarga la última versión estable de Python.
   - Ejecuta el archivo de instalación descargado y marca la casilla "Add Python to PATH" durante el proceso de instalación.
   - Sigue las instrucciones en pantalla y completa la instalación.

2. Verificación de la instalación de Python:
   - Abre una ventana de comandos (CMD).
   - Escribe el siguiente comando y presiona Enter:
     ```
     python --version
     ```
   - Debería mostrarte la versión de Python instalada, lo que confirma que la instalación fue exitosa.

3. Instalación de Tkinter:
   - Tkinter generalmente ya está incluido en las instalaciones estándar de Python, por lo que no requiere una instalación adicional.

4. Instalación de PIL (Python Imaging Library):
   - Abre una ventana de comandos (CMD).
   - Escribe el siguiente comando y presiona Enter:
     ```
     pip install pillow
     ```
   - Esto instalará la biblioteca PIL a través del paquete Pillow, que es una bifurcación activa y compatible de PIL.

5. Verificación de la instalación de PIL:
   - Abre el intérprete de Python ejecutando el comando `python` en una ventana de comandos (CMD).
   - Importa el módulo PIL ejecutando el siguiente comando en el intérprete:
     ```
     import PIL
     ```
   - Si no aparece ningún error, significa que la instalación de PIL fue exitosa.

Video del proyecto final 
link(ahora publico): https://drive.google.com/file/d/1_o-x6SvExeZy-RurAGac4mDtvSoB1lwq/view?usp=sharing
