#base del movimento(auto)
import pygame
#definicion de variables
v0 = 0 #velocidad inicial 
a = 2 # aceleraciont 
t=0 #tiempo

#Iniciar pygame
pygame.init()
pygame.display.set_caption("movimiento rectilineo uniforme acelerado") 
#display 
width= 960
height=640
pantalla= pygame.display.set_mode((width,height))
time= pygame.time.clock()

#cargar imagen
car_imagene= pygame.display.set_mode

