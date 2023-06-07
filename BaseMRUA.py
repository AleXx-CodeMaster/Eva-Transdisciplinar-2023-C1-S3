#base del movimento(auto)
import pygame
#definicion de variables
v0 = 0 #velocidad inicial 
a = 2 # aceleraciont 
t=0 #tiempo


pygame.init() #incia pygame  
pygame.display.set_caption("movimiento rectilineo uniforme acelerado")#nombre de la pestalña
#dimensiones de la pantalla
width= 960 #ancho
height=640 #alto
pantalla= pygame.display.set_mode((width,height)) #dimenciones de la pantalla
time= pygame.time.clock() #fotogramas
#imagen auto
car_imagene= pygame.image.load("carpaint.png")# carga de foto de la nae
car_rect=car_image.get_rect() #obtiene el fondo de la imgagne 
car_rect.center= (width//2, heiht//2)


