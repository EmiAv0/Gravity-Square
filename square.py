import pygame
import sys
from pygame.event import Event
pygame.init()

# Set up display
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Move a Square")

# Set color and square parameters
square_color = (255, 0, 0)  # Red
square_position = (100, 100)  # Top-left corner
square_size = (50, 50)  # Width and height
x=100
y=100

# Fill screen with black
screen.fill((0, 0, 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    running = True
    while running:
        gspeed = 0.07
        y = y + gspeed #this & gspeed are gravity
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            screen.fill((0, 0, 0))

            pygame.draw.rect(screen, square_color, (*square_position, *square_size))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("Left arrow pressed")
                    x=x-50
                    pygame.display.flip()

                if event.key == pygame.K_RIGHT:
                    print("Right arrow pressed")
                    x=x+50
                    pygame.display.flip()

                if event.key == pygame.K_UP:
                    print("Up arrow pressed")
                    y = y-50
                    pygame.display.flip()

                if event.key == pygame.K_DOWN:
                    print("Down arrow pressed")
                    y = y+50
                    pygame.display.flip()
        square_position = (x,y)
        print(square_position)
        screen.fill((0, 0, 0)) # Fill screen with black
        pygame.draw.rect(screen, square_color, (*square_position, *square_size))
        pygame.display.flip()

pygame.quit()
sys.exit()