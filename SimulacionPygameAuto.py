# Variables del MRUA
import pygame
v0 = 0  # Velocidad inicial
a = 2  # Aceleración constante
t = 0  # Tiempo

pygame.init()#inicia pygame
pygame.display.set_caption("Movimiento rectilíneo uniforme acelerado")#nombre 

# Configuración de la pantalla
width, height = 960, 640  # ancho, alto
pantalla = pygame.display.set_mode((width, height))
time = pygame.time.Clock()

# Carga de la imagen del auto
car_image = pygame.image.load("AutoSinFondo.png")
car_rect = car_image.get_rect()#toma el recuadro del auto, para la posicion
car_rect.center = (width // 2, 540) #posicion inicial nae

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Actualizar la posición del auto según el MRUA
    x = v0 * t + 0.5 * a * t ** 2 #movimeinto
    car_rect.centerx = int(x) #posicion auto asegurando que sea un numero enterO()
    t += 1

    # Dibujar la imagen del auto en la pantalla
    pantalla.fill((255, 255, 255))#relllenar color blanco el fondo
    pantalla.blit(car_image, car_rect)
    pygame.display.flip()
    time.tick(60)  # 60 FPS
