import pygame
import time
import random
import playGameController

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
WHITE = (5, 100, 255)
TEXT_COLOUR = (255, 99, 71)
PIPE_COLOUR = (34, 139, 34)

player = playGameController.createPlayer('Vasco', 'C:\\Users\\Beatriz Ribeiro\\Documents\\Python\\Pygame\\flappyVasco\\mano.png', 72, 90) #90 para mano.png

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

#changes the title of the window
pygame.display.set_caption('Flappy Vasco')

#sets game clock
clock = pygame.time.Clock()

#load characters image
backgroundImage = pygame.image.load('C:\\Users\\Beatriz Ribeiro\\Documents\\Python\\Pygame\\flappyVasco\\arcade_background.jpg')
playerImage = pygame.image.load(player._Player__icon._Icon__url)

#characters and pipes
def icon(x,y):
    gameDisplay.blit(playerImage,(x,y))

def things(x_thing, y_thing, w_thing, h_thing, colour):
    piper = playGameController.createPipe(w_thing, h_thing, colour)
    pygame.draw.rect(gameDisplay, piper._Pipe__colour, [x_thing, y_thing, piper._Pipe__width, piper._Pipe__height])

#messages
def text_objects(text, font):
    textSurface = font.render(text, True, TEXT_COLOUR)
    return textSurface, textSurface.get_rect()

def message_display(message):
    text = pygame.font.Font('freesansbold.ttf', 55)
    TextSurf , TextRect = text_objects(message, text)
    TextRect.center = (round((DISPLAY_WIDTH/2)), round((DISPLAY_HEIGHT/2)))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(2)

    game_loop()

def calculateHeightThing(y_start):
    global DISPLAY_HEIGHT
    if y_start == 0:
        return random.randrange(100, DISPLAY_HEIGHT//2)
    else:
        return DISPLAY_HEIGHT - y_start

#actions
def crash():
    message_display('ÉS PÉSSIMO...')

def game_loop():

    x = round((DISPLAY_WIDTH * 0.02)) #puts image in the middle
    y = round((DISPLAY_HEIGHT * 0.45))

    y_change = 0

    THING_SPEED = 4
    THING_WIDTH = 100
    X_START_THING = 750
    Y_START_THING = random.choice([0, random.randrange(DISPLAY_HEIGHT//2, DISPLAY_HEIGHT - 100)])
    THING_HEIGHT = round(calculateHeightThing(Y_START_THING))
    gameExit = False 

    while not gameExit:
        for event in pygame.event.get():  #list of events per frame per second
            if event.type == pygame.QUIT:   #checks if user wants to quit
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_UP:
                    y_change = -10

            if event.type == pygame.KEYUP:
                y_change = 2

        y += y_change 

        gameDisplay.blit(backgroundImage,[0,0])
        things(X_START_THING, Y_START_THING, THING_WIDTH, THING_HEIGHT, PIPE_COLOUR)
        X_START_THING -= THING_SPEED 
        icon(x,y) #draws the icon in second
        
        if y > DISPLAY_HEIGHT - player._Player__icon._Icon__height or y < 0:
            crash()

        if X_START_THING < 0 - THING_WIDTH:
            X_START_THING = 750
            Y_START_THING = random.choice([0, random.randrange(DISPLAY_HEIGHT//2, DISPLAY_HEIGHT - 100)])
            THING_HEIGHT = round(calculateHeightThing(Y_START_THING))

        if x + player._Player__icon._Icon__width > X_START_THING:
            if y > Y_START_THING and y < Y_START_THING + THING_HEIGHT or \
                y + player._Player__icon._Icon__height > Y_START_THING and \
                    y + player._Player__icon._Icon__height < Y_START_THING + THING_HEIGHT:
                crash()
        pygame.display.update()
        clock.tick(100)


game_loop()
pygame.quit()
quit()