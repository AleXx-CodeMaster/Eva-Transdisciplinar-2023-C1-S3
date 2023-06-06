#Ing.Civil en Informatica
#Evaluacion Transdisciplinar 2023
#Movimiento Rectilineo Uniforme Acelerado
#---------------------------------------------------------------------
#__________      ___.           __  .__
#\______   \ ____\_ |__   _____/  |_|__| ____ _____
# |       _//  _ \| __ \ /  _ \   __\  |/ ___\\__  \
# |    |   (  <_> ) \_\ (  <_> )  | |  \  \___ / __ \_
# |____|_  /\____/|___  /\____/|__| |__|\___  >____  /
#        \/           \/                    \/     \/
#---------------------------------------------------------------------
import pygame as PG
import PySimpleGUI as SG

WIDTH = 980  # Ancho
HEIGHT = 551

def PyGame_Init():
    PG.init()
    PG.mouse.set_visible(False)
    PG.display.set_caption('Movimiento Rectilíneo Uniforme Acelerado')
    window = PG.display.set_mode((WIDTH, HEIGHT))
    return window

# Carga de la imagen de fondo
def Load_Background():
    background_image = PG.image.load("camino.png").convert()
    background_rect = background_image.get_rect()
    background_rect.x = 0
    return background_image, background_rect

# Carga de la imagen del auto
def Load_Car():
    car_image = PG.image.load("auto.png").convert_alpha()
    car_rect = car_image.get_rect()
    car_rect.center = (WIDTH // 2, HEIGHT // 2)
    return car_image, car_rect

# Función para calcular la posición del auto en función del tiempo y la aceleración
def Calculate_Car_Position(time, acceleration):
    initial_velocity = 0
    position = initial_velocity * time + (0.1 * acceleration * time ** 2)
    return position

# Función principal del juego
def main():
    window = PyGame_Init()
    background_image, background_rect = Load_Background()
    car_image, car_rect = Load_Car()

    # Velocidad de desplazamiento horizontal
    car_speed = 1

    # Variables para el cálculo del movimiento
    time = 0
    acceleration = 0

    # Variables para la posición del auto
    car_position_x = WIDTH // 2  # Posición X inicial del auto
    car_position_y = HEIGHT // 2  # Posición Y inicial del auto

    # Establecer la posición del rectángulo del auto
    car_rect.x = 300
    car_rect.y = 400

    # Bucle principal del juego
    running = True
    clock = PG.time.Clock()

    while running:
        for event in PG.event.get():
            if event.type == PG.QUIT:
                running = False

        # Actualizar la posición y velocidad del auto
        car_rect.x += car_speed
        car_speed += acceleration

        # Actualizar la posición del fondo en función de la velocidad del auto
        background_speed = car_speed * 0.6
        background_rect.x -= background_speed

        # Si el fondo se ha desplazado completamente fuera de la ventana, reiniciar su posición
        if background_rect.right <= WIDTH:
            background_rect.x = 0

        # Si el auto se ha desplazado completamente fuera de la ventana, reiniciar su posición
        if car_rect.right <= 0:
            car_rect.x = WIDTH

        # Dibujar el fondo en la ventana
        window.blit(background_image, background_rect)

        # Dibujar el auto en la ventana
        window.blit(car_image, car_rect)

        # Copiar una porción del fondo al inicio para lograr un reinicio fluido
        if background_rect.x > 0:
            window.blit(background_image, (background_rect.x - WIDTH, background_rect.y), (0, 0, WIDTH - background_rect.x, HEIGHT))

        # Actualizar la pantalla
        PG.display.flip()

        # Controlar la velocidad de fotogramas
        clock.tick(120)  # 120 FPS

        # Actualizar el tiempo y calcular la posición del auto
        time += 1 / 120  # Tiempo transcurrido en segundos (120 FPS)
        position = Calculate_Car_Position(time, acceleration)

    # Salir del programa
    PG.quit()

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
