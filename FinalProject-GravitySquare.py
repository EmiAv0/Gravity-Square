#PI/AIDAN GILLISEPSE -> pls make the square eat little squares which gives a speed boost (they need to respawn), and fix gravity. thx!
import pygame
import sys
import time
import random
from pygame.event import Event
pygame.init()

# Set up display
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Gravity Square")

square_color = (160, 32, 240)
square_position = (100, 100)  # Top-left corner
sqh= 50
sqw=50
square_size = (sqh, sqw)  # Width and height
square_rect = pygame.Rect(square_position[0], square_position[1], square_size[0], square_size[1])

food_color = (255,0,0)
food_position = (random.randint(200,800),random.randint(200,800))
food_size = (25,25)
food_rect = pygame.Rect(food_position[0], food_position[1], food_size[0], food_size[1])

square_rect.x=100
square_rect.y=float(100)
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 22)
playing = True
running = True
yjumpspeed=50
gravity_timer = 0
gravity_delay = 10
food_touched = 0

while playing:
    screen.fill((0, 0, 0))  # Fill screen with blackfont = pygame.font.Font(None, 36)
    text = font.render("Welcome to Gravity Square!", True, (255, 255, 255))
    screen.blit(text, (300, 400))
    pygame.display.flip()
    time.sleep(2)
    screen.fill((0, 0, 0))  # Fill the screen with black color
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    running = True
    gspeed = 1

    while running:
         # Fill screen with blackfont = pygame.font.Font(None, 36)
        text2 = font.render("Score: " + str(food_touched), True, (255, 255, 255))
        screen.blit(text2, (200, 800))
        pygame.display.flip()
        gravity_timer += 1
        gspeed += 0.00001
        print(gspeed)
        # added by pi: this basically just only applies gravity every couple of frames
        if gravity_timer >= gravity_delay:
            gravity_timer = 0
            square_rect.y += gspeed

        square_rect.x = float(square_rect.x)
        square_rect.y = float(square_rect.y)

        for event in pygame.event.get():
            text2 = font.render("Score: " + str(food_touched), True, (255, 255, 255))
            screen.blit(text2, (200, 800))
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("Left arrow pressed")
                    square_rect.x -= 25

                if event.key == pygame.K_RIGHT:
                    print("Right arrow pressed")
                    square_rect.x += 25

                if event.key == pygame.K_UP:
                    print("Up arrow pressed")
                    square_rect.y -= yjumpspeed

                if event.key == pygame.K_DOWN:
                    print("Down arrow pressed")
                    square_rect.y += yjumpspeed

        print(square_rect.x, square_rect.y)
        square_rect.size = square_size
        screen.fill((0, 0, 0)) # Fill screen with black
        pygame.draw.rect(screen, square_color, (square_rect.x, square_rect.y, square_size[0], square_size[1]))
        pygame.draw.rect(screen, food_color, (food_rect.x, food_rect.y, food_size[0], food_size[1]))

        # if we eat the food then we increase the amount we jumpy by
        if square_rect.colliderect(food_rect):
            yjumpspeed += 0.7 # increase jump height
            # then we move the actual location of the food
            food_rect.x = random.randint(200, 800)
            food_rect.y = random.randint(200, 800)
            food_touched += 1
            yjumpspeed += 0.7
            sqh += 10
            sqw += 10
            square_size = (sqh, sqw)
            print("food touched:", food_touched)
            pygame.display.flip()

        if (square_rect == 1000) and (square_rect == 1000):
            print("You win!")
            print("Would you like to play again?")
            Y_N = input("Y or N: ")


        if (square_rect.x>1000 or square_rect.x<0) or (square_rect.y>1000 or square_rect.y<0):
            print("Game Over!")
            time.sleep(1)
            print("Would you like to play again?")
            Y_N = input("Y or N: ")

            if (Y_N == "N"):
                running = False
                print("Thank you for playing Gravity Square!")
                pygame.quit()
                sys.exit()

            if (Y_N == "Y"):
                square_color = (160, 32, 240)
                square_position = (100, 100)  # Top-left corner
                square_size = (50, 50)  # Width and height
                square_rect.x = 100
                square_rect.y = 100
                playing = True