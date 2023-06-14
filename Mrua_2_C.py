import tkinter as tk
from PIL import Image, ImageTk

def calcular_resultados():
    distancia = float(distancia_entry.get())
    velocidad_final = float(velocidad_final_entry.get())
    velocidad_inicial = float(velocidad_inicial_entry.get())
    tiempo = float(tiempo_entry.get())
    aceleracion = float(aceleracion_entry.get())

    # Calcular los resultados
    distancia_recorrida = ((velocidad_inicial+velocidad_final)/2)*tiempo

    aceleracion_final = (velocidad_final-velocidad_inicial)/tiempo

    velocidad_cambio = velocidad_final - velocidad_inicial

    distancia_sin_velocidad_final = velocidad_inicial * tiempo + ((aceleracion*(tiempo**2))/2)

    tiempo_final = (velocidad_final - velocidad_inicial) / aceleracion

    velocidad_final_cuadrado = 2*aceleracion*distancia + velocidad_inicial**2

    # Actualizar los resultados en la interfaz
   
    distancia_label_resultado.config(text=f"Distancia Recorrida: {distancia_recorrida:.2f} m")
    aceleracion_label_resultado.config(text=f"Aceleración Final: {aceleracion_final:.2f} m/s^2")
    velocidad_cambio_label.config(text=f"Velocidad Cambio: {velocidad_cambio:.2f} m/s")
    distancia_sin_velocidad_final_label.config(text=f"Distancia Sin Velocidad Final: {distancia_sin_velocidad_final:.2f} m")
    tiempo_final_label.config(text=f"Tiempo Final: {tiempo_final:.2f} s")
    velocidad_final_cuadrado_label.config(text=f"Velocidad Final al Cuadrado: {velocidad_final_cuadrado:.2f} m/s^2")

def mover_auto():
    global posicion, velocidad, aceleracion

    # Calcular la nueva posición y velocidad
    posicion = posicion + velocidad * delta_tiempo + 0.5 * aceleracion * delta_tiempo**2
    velocidad = velocidad + aceleracion * delta_tiempo
    
    #verificar si el auto esta fuera del rango del lienzo
    if posicion < 0:
        posicion = 0
        velocidad = 0
    elif posicion > 1400:
        posicion = 1400
        velocidad = 0 

    # Calcular el desplazamiento del fondo según la velocidad del auto
    desplazamiento_fondo = -velocidad * delta_tiempo

    # Verificar si el fondo alcanza su límite y reiniciarlo
    if canvas.coords(fondo_id)[0] <= -1400:  # Ancho del fondo
        canvas.coords(fondo_id, 0, 0)

    # Mover el fondo del lienzo junto con el auto
    canvas.move(fondo_id, desplazamiento_fondo, 0)

    # Actualizar la posición del auto en el lienzo
    canvas.coords(auto_id, posicion, 100)

    # Actualizar los valores de posición y velocidad en la interfaz
    posicion_label.config(text=f"Posición: {posicion:.2f} m")
    velocidad_label_simulacion.config(text=f"Velocidad: {velocidad:.2f} m/s")

    # Continuar moviendo el auto si no ha alcanzado la distancia objetivo
    if posicion < distancia_objetivo:
        root.after(20, mover_auto)

def iniciar_movimiento():
    global aceleracion, distancia_objetivo
    aceleracion = float(aceleracion_entry.get())
    distancia_objetivo = float(distancia_entry.get())

    mover_auto()


def reiniciar_simulacion():
    global posicion, velocidad, aceleracion
    posicion = 0
    velocidad = 0
    aceleracion = 0
    canvas.coords(auto_id, posicion, 100)  # Reiniciar la posición del auto en el lienzo
    posicion_label.config(text="Posición: ")  # Reiniciar la etiqueta de posición en la interfaz
    velocidad_label_simulacion.config(text="Velocidad: ")  # Reiniciar la etiqueta de velocidad en la interfaz


# Crear la ventana
root = tk.Tk()
root.title("Simulación de Auto y Cálculo de MRUA")
root.geometry("1200x850")
root.configure(bg="#F0F0F0")

# Cargar la imagen del auto
image_path = "auto1.png"
image = Image.open(image_path)
image = image.resize((100, 50), Image.ANTIALIAS)
auto_image = ImageTk.PhotoImage(image)

# Cargar la imagen de fondo
fondo_path = "camino.png"
fondo_image = Image.open(fondo_path)
fondo_image = fondo_image.resize((1400, 200), Image.ANTIALIAS)
fondo_photo = ImageTk.PhotoImage(fondo_image)

# Crear lienzo para mostrar el auto con imagen de fondo
canvas = tk.Canvas(root, width=1400, height=200, highlightthickness=0)
canvas.create_image(0, 0, anchor=tk.NW, image=fondo_photo)
canvas.pack()


# Continuar moviendo el auto si no ha alcanzado la distancia objetivo
fondo_id = canvas.create_image(0, 0, anchor=tk.NW, image=fondo_photo)

# Mostrar el auto en el lienzo
auto_id = canvas.create_image(0, 130, anchor=tk.NW, image=auto_image)


# Crear etiquetas y campos de entrada para la simulación del auto
simulacion_frame = tk.Frame(root, bg="#F0F0F0")
simulacion_frame.pack(pady=10)

# BOTONES
botones_frame = tk.Frame(root, bg="#F0F0F0")
botones_frame.pack(pady=10)

# BOTON DE INICIAR
iniciar_button = tk.Button(botones_frame, text="Iniciar", command=iniciar_movimiento)
iniciar_button.grid(row=0, column=0, padx=5)


# POSICION
posicion_label = tk.Label(root, text="Posición: ", bg="#F0F0F0")
posicion_label.pack()

# VELOCIDAD
velocidad_label_simulacion = tk.Label(root, text="Velocidad: ", bg="#F0F0F0")
velocidad_label_simulacion.pack()

# Crear etiquetas y campos de entrada para el cálculo de MRUA
calculo_frame = tk.Frame(root, bg="#F0F0F0")
calculo_frame.pack(pady=10)

# DISTANCIA
distancia_label = tk.Label(calculo_frame, text="Distancia a Recorrer (m):", bg="#F0F0F0")
distancia_label.grid(row=0, column=0, padx=10, pady=5)
distancia_entry = tk.Entry(calculo_frame)
distancia_entry.grid(row=0, column=1, padx=10, pady=5)

# VELOCIDAD INICIAL
velocidad_inicial_label = tk.Label(calculo_frame, text="Velocidad Inicial (m/s):", bg="#F0F0F0")
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

# BOTON DE REINICIAR
reiniciar_button = tk.Button(botones_frame, text="Reiniciar", command=reiniciar_simulacion)
reiniciar_button.grid(row=0, column=2, padx=5)

# CALCULAR
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
delta_tiempo = 0.1

root.mainloop()
