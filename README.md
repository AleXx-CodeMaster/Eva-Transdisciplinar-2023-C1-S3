1.      MRUA-SIMULATOR (Eva-Transdiciplinario-2023-CI-S3)
Descripción: El movimiento rectilíneo uniforme acelerado (MRUA) es un tipo de movimiento en el que un objeto se desplaza a lo largo de una línea recta con una aceleración constante. En este tipo de movimiento, la velocidad del objeto cambia de manera uniforme a medida que pasa el tiempo.


En el **MRUA**, el objeto experimenta una **aceleración constante**, lo que significa que la magnitud de su velocidad cambia de manera uniforme en intervalos de tiempo iguales. La aceleración puede ser **positiva o negativa**, dependiendo de la dirección en la que se aplique.

Durante el MRUA, se pueden observar las siguientes características:

**Posición inicial**: Es la posición del objeto en el inicio del movimiento. Se representa usualmente con la letra "x₀".

**Velocidad inicial**: Es la velocidad del objeto en el instante inicial. Se representa con la letra "v₀".
    
**Aceleración**: Es la tasa de cambio de la velocidad. Se representa con la letra "a". Si la aceleración es positiva, el objeto aumentará su velocidad en el tiempo, mientras que si es negativa, disminuirá su velocidad.
    
**Velocidad**: Es la magnitud de la rapidez con la que el objeto se desplaza. Se representa con la letra "v". En el MRUA, la velocidad cambia de manera constante, incrementándose o disminuyendo según la dirección de la aceleración.
    
**Tiempo**: Es el intervalo de tiempo transcurrido desde el inicio del movimiento. Se representa con la letra "t".
    
 **Desplazamiento**: Es la variación en la posición del objeto durante un determinado intervalo de tiempo. Se representa con la letra "Δx" o simplemente "x". En el MRUA, el desplazamiento puede ser positivo o negativo, dependiendo de la dirección del movimiento.

En este trabajo vamos a simular un auto que se mueve por una carrera en donde acelera en línea recta, en donde experimenta MRUA con una aceleración constante positiva. En este caso, la velocidad del automóvil aumenta gradualmente, la idea principal es que el usuario pueda ingresarle valores para ir alterando su velocidad y alterar lo que es el desplazamiento, la posición y la aceleración manera gradual, todo esto siguiendo las reglas del Fenómeno Físico Mencionado.

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
b.      Guia  de  instalación
c.      Guia  de  uso  (Hacer  uso  de  imágenes  o  un  video  tutorial  para  su  uso)
d.      Enlace  a  vídeo  con  la  explicación  del  código  desarrollado.
8.      Conclusiones

