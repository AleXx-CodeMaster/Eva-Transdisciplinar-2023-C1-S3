#EVALUACION TRANSDISCIPLINAR 2023
#INGENIERIA CIVIL EN INFORMATICA
#FIS 1102 e INFO 1120

#---------------------------------------------------------------------
# importaciones 
#---------------------------------------------------------------------

import tkinter as tk
from PIL import Image, ImageTk

#---------------------------------------------------------------------
#Se obtienen los valores de las entradas de texto y se convierten a tipo float
#---------------------------------------------------------------------
# editado zona de calculos por claudio. 
def calcular_resultados(): 
    distancia = float(distancia_entry.get()) #devuelve el texto ingresado por el usuario en esa entrada. en tipo Float = Decimal
    velocidad_final = float(velocidad_final_entry.get())
    velocidad_inicial = float(velocidad_inicial_entry.get())
    tiempo = float(tiempo_entry.get())
    aceleracion = float(aceleracion_entry.get())

#---------------------------------------------------------------------
#Se realizan los cálculos necesarios utilizando las fórmulas del MRUA
#---------------------------------------------------------------------

    distancia_recorrida = ((velocidad_inicial+velocidad_final)/2)*tiempo

    aceleracion_final = (velocidad_final-velocidad_inicial)/tiempo

    velocidad_cambio = velocidad_final - velocidad_inicial

    distancia_sin_velocidad_final = velocidad_inicial * tiempo + ((aceleracion*(tiempo**2))/2)

    tiempo_final = (velocidad_final - velocidad_inicial) / aceleracion

    velocidad_final_cuadrado = 2*aceleracion*distancia + velocidad_inicial**2

#-------------------------------------------------------------------------
#Se actualizan las etiquetas en la interfaz con los resultados obtenidos
#-------------------------------------------------------------------------

     #nombre de la etiqueta,configuracion de propiedades del tkinter, cadena de texto formateada, unidad de medida.
    distancia_label_resultado.config(text=f"Distancia Recorrida: {distancia_recorrida:.2f} m") #texto,

    aceleracion_label_resultado.config(text=f"Aceleración Final: {aceleracion_final:.2f} m/s^2")

    velocidad_cambio_label.config(text=f"Velocidad Cambio: {velocidad_cambio:.2f} m/s")

    distancia_sin_velocidad_final_label.config(text=f"Distancia Sin Velocidad Final: {distancia_sin_velocidad_final:.2f} m")

    tiempo_final_label.config(text=f"Tiempo Final: {tiempo_final:.2f} s")
    
    velocidad_final_cuadrado_label.config(text=f"Velocidad Final al Cuadrado: {velocidad_final_cuadrado:.2f} m/s^2")

#---------------------------------------------------------------------
#Funcionalidad de movimiento de auto y fondo
#---------------------------------------------------------------------

def mover_auto():
    global posicion, velocidad, aceleracion

    # Calcular la nueva posición y velocidad, delta_tiempo: se utiliza para calcular los cambios en la posición y velocidad del auto en cada paso de tiempo.
    posicion = posicion + velocidad * delta_tiempo + 0.5 * aceleracion * delta_tiempo**2
    velocidad = velocidad + aceleracion * delta_tiempo
    
 #---------------------------------------------------------------------
 #verificar si el auto esta fuera del rango del lienzo
 #---------------------------------------------------------------------

    #derecha 
    if posicion < 0:  #si la posición del auto es menor que 0, cual indicaría que ha salido del rango del lienzo hacia la izquierda. 
        posicion = 0 #se establece la posición del auto en 0
        velocidad = 0 #se detiene la velocidad estableciéndola en 0.
    #izquierda
    elif posicion > 1400:
        posicion = 1400
        velocidad = 0 

    # Calcular el desplazamiento del fondo según la velocidad del auto
    desplazamiento_fondo = -velocidad * delta_tiempo

    # Verificar si el fondo alcanza su límite y reiniciarlo
    if canvas.coords(fondo_id)[0] <= -1400:  #la imagen ha alcanzado o superado su límite izquierdo en el lienzo.
        canvas.coords(fondo_id, 0, 0) #"reinicia" la posición del fondo, colocándolo de nuevo en el extremo izquierdo del lienzo

    # Mover el fondo del lienzo junto con el auto
    canvas.move(fondo_id, desplazamiento_fondo, 0) # El valor 0 en el tercer argumento indica que no habrá desplazamiento en el eje Y (vertical).

    # Actualizar la posición del auto en el lienzo
    canvas.coords(auto_id, posicion, 100) #100 es la posición fija del auto en el eje Y (vertical)

    # Actualizar los valores de posición y velocidad en la interfaz
    posicion_label.config(text=f"Posición: {posicion:.2f} m")
    velocidad_label_simulacion.config(text=f"Velocidad: {velocidad:.2f} m/s")

    # Continuar moviendo el auto si no ha alcanzado la distancia objetivo
    if posicion < distancia_objetivo: #verifica si la posición actual del auto es menor que la distancia objetivo
        root.after(20, mover_auto) #permite que el auto continúe moviéndose en la simulación.


#---------------------------------------------------------------------
#iniciar el movimiento del auto en la simulación.
#---------------------------------------------------------------------


def iniciar_movimiento():
    global aceleracion, distancia_objetivo
    aceleracion = float(aceleracion_entry.get())
    distancia_objetivo = float(distancia_entry.get())

    mover_auto()


#---------------------------------------------------------------------
#Reiniciar el movimiento del auto en la simulación.
#---------------------------------------------------------------------

def reiniciar_simulacion():
    global posicion, velocidad, aceleracion
    posicion = 0
    velocidad = 0
    aceleracion = 0
    canvas.coords(auto_id, posicion, 100)  # Reiniciar la posición del auto en el lienzo
    posicion_label.config(text="Posición: ")  # Reiniciar la etiqueta de posición en la interfaz
    velocidad_label_simulacion.config(text="Velocidad: ")  # Reiniciar la etiqueta de velocidad en la interfaz


#---------------------------------------------------------------------
# Crea la ventana de Simulacion 
#---------------------------------------------------------------------
#resolucion e imagenes por: Sebastian.
root = tk.Tk()
root.title("Simulación de Auto y Cálculo de MRUA")
root.geometry("1200x850")
root.configure(bg="#F0F0F0") #configuracion del color de fondo de la ventana: rojo,verde,azul

# Cargar la imagen del auto
image_path = "auto1.png"
image = Image.open(image_path)
image = image.resize((100, 50), Image.ANTIALIAS) #Antilias: algoritmo de suavizado durante el redimensionamiento para obtener una imagen de mejor calidad.
auto_image = ImageTk.PhotoImage(image)

# Cargar la imagen de fondo
fondo_path = "camino.png"
fondo_image = Image.open(fondo_path)
fondo_image = fondo_image.resize((1400, 200), Image.ANTIALIAS)
fondo_photo = ImageTk.PhotoImage(fondo_image)


# Crear lienzo para mostrar el auto con imagen de fondo
canvas = tk.Canvas(root, width=1400, height=200, highlightthickness=0) # establece el grosor del borde resaltado del lienzo
canvas.create_image(0, 0, anchor=tk.NW, image=fondo_photo)
canvas.pack()


# mostrar el fondo en el lienzo
fondo_id = canvas.create_image(0, 0, anchor=tk.NW, image=fondo_photo)

# Mostrar el auto en el lienzo
auto_id = canvas.create_image(0, 130, anchor=tk.NW, image=auto_image)


# BOTONES INICIAR Y REINICIAR
botones_frame = tk.Frame(root, bg="#F0F0F0") #color del fondo del marco
botones_frame.pack(pady=10) #se utiliza para colocar el marco en la ventana principal y establece un espacio de relleno vertical de 10 píxeles alrededor del marco.

# INICIAR
iniciar_button = tk.Button(botones_frame, text="Iniciar", command=iniciar_movimiento)
iniciar_button.grid(row=0, column=0, padx=5) #pandx = espacio de 5 píxeles a la izquierda y a la derecha del botón.

#  REINICIAR
reiniciar_button = tk.Button(botones_frame, text="Reiniciar", command=reiniciar_simulacion)
reiniciar_button.grid(row=0, column=2, padx=5)

#---------------------------------------------------------------------
#TEXTO DE POSICION Y VELOCIDAD 
#---------------------------------------------------------------------

# POSICION
posicion_label = tk.Label(root, text="Posición: ", bg="#F0F0F0")
posicion_label.pack()

# VELOCIDAD
velocidad_label_simulacion = tk.Label(root, text="Velocidad: ", bg="#F0F0F0")
velocidad_label_simulacion.pack()

#----------------------------------------------------------------------------
#Configuracion de Ingreso de texto y Resultados con sus respectivas formulas 
#----------------------------------------------------------------------------

# MARCO
calculo_frame = tk.Frame(root, bg="#F0F0F0")
calculo_frame.pack(pady=10) #se utiliza para colocar el marco dentro de la ventana principal. El argumento pady=10 establece un espacio de relleno de 10 píxeles en la dirección vertical (arriba y abajo) alrededor del marco.


# DISTANCIA
distancia_label = tk.Label(calculo_frame, text="Distancia a Recorrer (m):", bg="#F0F0F0")
distancia_label.grid(row=0, column=0, padx=10, pady=5)

distancia_entry = tk.Entry(calculo_frame) #widget de entrada es un campo de texto donde el usuario puede ingresar datos
distancia_entry.grid(row=0, column=1, padx=10, pady=5)

# VELOCIDAD INICIAL
velocidad_inicial_label = tk.Label(calculo_frame, text="Velocidad Inicial (m/s):", bg="#F0F0F0") #label: texto estático o descriptivo
velocidad_inicial_label.grid(row=1, column=0, padx=10, pady=5)

velocidad_inicial_entry = tk.Entry(calculo_frame)
velocidad_inicial_entry.grid(row=1, column=1, padx=10, pady=5)

# VELOCIDAD FINAL
velocidad_final_label = tk.Label(calculo_frame, text="Velocidad Final (m/s):", bg="#F0F0F0")
velocidad_final_label.grid(row=2, column=0, padx=10, pady=5)

velocidad_final_entry = tk.Entry(calculo_frame)
velocidad_final_entry.grid(row=2, column=1, padx=10, pady=5)

# TIEMPO
tiempo_label = tk.Label(calculo_frame, text="Tiempo (s):", bg="#F0F0F0")
tiempo_label.grid(row=3, column=0, padx=10, pady=5)

tiempo_entry = tk.Entry(calculo_frame)
tiempo_entry.grid(row=3, column=1, padx=10, pady=5)

# ACELERACION
aceleracion_label = tk.Label(calculo_frame, text="Aceleración (m/s^2):", bg="#F0F0F0")
aceleracion_label.grid(row=4, column=0, padx=10, pady=5)

aceleracion_entry = tk.Entry(calculo_frame)
aceleracion_entry.grid(row=4, column=1, padx=10, pady=5)


# CALCULAR
#columspan: el número de columnas que el botón debe ocupar en la cuadrícula.
calcular_button = tk.Button(calculo_frame, text="Calcular", command=calcular_resultados)
calcular_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# RESULTADOS
resultados_frame = tk.Frame(root, bg="#F0F0F0")
resultados_frame.pack(pady=10)


# DISTANCIA RECORRIDA
distancia_label_resultado = tk.Label(resultados_frame, text="Distancia Recorrida: ", bg="#F0F0F0")
distancia_label_resultado.grid(row=1, column=0, padx=10, pady=5)

# ACELERACION FINAL
aceleracion_label_resultado = tk.Label(resultados_frame, text="Aceleración Final: ", bg="#F0F0F0")
aceleracion_label_resultado.grid(row=2, column=0, padx=10, pady=5)

# VELOCIDAD CAMBIO
velocidad_cambio_label = tk.Label(resultados_frame, text="Velocidad Cambio: ", bg="#F0F0F0")
velocidad_cambio_label.grid(row=3, column=0, padx=10, pady=5)

# DISTANCIA SIN VELOCIDAD FINAL
distancia_sin_velocidad_final_label = tk.Label(resultados_frame, text="Distancia Sin Velocidad Final: ", bg="#F0F0F0")
distancia_sin_velocidad_final_label.grid(row=4, column=0, padx=10, pady=5)

# TIEMPO FINAL
tiempo_final_label = tk.Label(resultados_frame, text="Tiempo Final: ", bg="#F0F0F0")
tiempo_final_label.grid(row=5, column=0, padx=10, pady=5)

# VELOCIDAD FINAL AL CUADRADO
velocidad_final_cuadrado_label = tk.Label(resultados_frame, text="Velocidad Final al Cuadrado: ", bg="#F0F0F0")
velocidad_final_cuadrado_label.grid(row=6, column=0, padx=10, pady=5)


# VARIABLES DE SIMULACION
posicion = 0
velocidad = 0
aceleracion = 0
distancia_objetivo = 0
delta_tiempo = 0.1 #es una variable que representa el intervalo de tiempo entre cada iteración del movimiento del auto.

root.mainloop()


