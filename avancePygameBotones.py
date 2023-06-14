import pygame
import sys
from pygame.locals import *

# Initialize the game
pygame.init()

# Set the window size
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640

# Set the window's title
pygame.display.set_caption('Movimiento rectilíneo uniforme acelerado')

# Set the clock
clock = pygame.time.Clock()

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Load the car image
car_image = pygame.image.load("auto1.png")
car_rect = car_image.get_rect()
car_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3)

# Set the initial variables
v0 = 0  # Initial velocity
a = 2  # Acceleration
t = 0  # Time

# Set the running variable
running = True

# Set the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)

# Define the font
font = pygame.font.SysFont(None, 30)

# Define the button positions
button_x = WINDOW_WIDTH // 2 - 120
button_y = WINDOW_HEIGHT - 150
button_width = 100
button_height = 40
button_margin = 20

# Define the button labels
button_labels = ["Initial V", "Final V", "Acceleration"]

# Define the button click functions
def calculate_initial_velocity_button_click():
    global v0
    v0 = a * t
    print('Initial velocity:', v0)

def calculate_final_velocity_button_click():
    global v0, a
    final_velocity = v0 + a * t
    print('Final velocity:', final_velocity)

def calculate_acceleration_button_click():
    global v0, a, t
    acceleration = (v0 + v0 + a * t) / (2 * t)
    print('Acceleration:', acceleration)

# Define the event handlers
def handle_button_click(event):
    global a
    if event.type == MOUSEBUTTONUP:
        mouse_x, mouse_y = event.pos
        if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
            calculate_initial_velocity_button_click()
        elif button_x + button_width + button_margin <= mouse_x <= button_x + 2 * button_width + button_margin and button_y <= mouse_y <= button_y + button_height:
            calculate_final_velocity_button_click()
        elif button_x + 2 * (button_width + button_margin) <= mouse_x <= button_x + 3 * (button_width + button_margin) and button_y <= mouse_y <= button_y + button_height:
            calculate_acceleration_button_click()

# Main loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        handle_button_click(event)

    # Update the position of the car according to the MRUA
    x = v0 * t + 0.5 * a * t ** 2
    car_rect.centerx = int(x)
    t += 1

    # Clear the window
    window.fill(WHITE)

    # Draw the car
    window.blit(car_image, car_rect)

    # Draw the buttons
    for i in range(len(button_labels)):
        pygame.draw.rect(window, RED, (button_x + i * (button_width + button_margin), button_y, button_width, button_height))
        label = font.render(button_labels[i], True, WHITE)
        label_rect = label.get_rect()
        label_rect.center = (button_x + i * (button_width + button_margin) + button_width // 2, button_y + button_height // 2)
        window.blit(label, label_rect)

    # Display the results
    v0_label = font.render('Initial velocity: ' + str(v0), True, BLACK)
    v0_label_rect = v0_label.get_rect()
    v0_label_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 100)
    window.blit(v0_label, v0_label_rect)

    a_label = font.render('Acceleration: ' + str(a), True, BLACK)
    a_label_rect = a_label.get_rect()
    a_label_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 60)
    window.blit(a_label, a_label_rect)

    # Update the display
    pygame.display.update()
    clock.tick(60)

# Quit the game
pygame.quit()
sys.exit()
