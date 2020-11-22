import pygame
import time
import random
import gameController

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
MINIMUM_WIDTH_THING = 30
MARGINS = 110
WHITE = (5, 100, 255)
TEXT_COLOUR = (210, 105, 30)
PIPE_COLOUR = (162, 0, 37)
pipes = []

player = gameController.createPlayer('Vasco', 'C:\\Users\\Beatriz Ribeiro\\Documents\\Python\\Pygame\\flappyVasco\\mano.png', 72, 90) #90 para mano.png

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

def things(pipe): 
    pygame.draw.rect(gameDisplay, pipe.getColour(), [pipe.getX(), pipe.getY(), pipe.getWidth(), pipe.getHeight()] )

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
    del pipes[:]
    game_loop()

#actions
def crash():
    message_display('ÉS PÉSSIMO...')


def game_loop():
    idxHasNextPipe = 0
    x = round((DISPLAY_WIDTH * 0.02)) #puts image in the middle
    y = round((DISPLAY_HEIGHT * 0.45))

    y_change = 0
    things_speed = 4
    THING_WIDTH = 100
    x_start_things = DISPLAY_WIDTH
    y_start_thing_1 = 0
    height_thing_1 = random.randrange(10, (DISPLAY_HEIGHT - (MINIMUM_WIDTH_THING + MARGINS + player.getIcon().getHeight())))
    y_start_thing_2 = random.randrange(height_thing_1 + MARGINS + player.getIcon().getHeight(), DISPLAY_HEIGHT - 10)
    pipe1 = gameController.createPipe(THING_WIDTH,height_thing_1, PIPE_COLOUR, x_start_things, y_start_thing_1 )
    pipe2 = gameController.createPipe(THING_WIDTH, DISPLAY_HEIGHT - y_start_thing_2, PIPE_COLOUR, x_start_things, y_start_thing_2)
    space_between_things = random.randrange(200, 400)
    pipes.append(pipe1)
    pipes.append(pipe2)
    gameExit = False 

    while not gameExit:
       
        for event in pygame.event.get():  #list of events per frame per second
            if event.type == pygame.QUIT:   #checks if user wants to quit
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_UP:
                    y_change = -7

            if event.type == pygame.KEYUP:
                y_change = 3

        y += y_change 

        gameDisplay.blit(backgroundImage,[0,0])
        for pipe in pipes:
            things(pipe)
            pipe._Pipe__x = pipe.getX() - things_speed
        icon(x,y) #draws the icon in second
        
        if y > DISPLAY_HEIGHT - player._Player__icon._Icon__height or y < 0:
           crash()

        
        if pipes[0].getX() < 0 - THING_WIDTH:
            idxHasNextPipe -= 2
            del pipes[0:2]           

        for idx , pipe in enumerate(pipes):

            if x + player._Player__icon._Icon__width > pipe.getX():
                if y > pipe.getY() and y < pipe.getY() + pipe.getHeight() or \
                    y + player.getIcon().getHeight() > pipe.getY() and \
                        y + player.getIcon().getHeight() < pipe.getY() + pipe.getHeight():
                    crash()
                              
            if pipe.getX() < DISPLAY_WIDTH - (space_between_things + THING_WIDTH) and idx == idxHasNextPipe:
                idxHasNextPipe += 2
                x_start_things = DISPLAY_WIDTH
                height_thing_1 = random.randrange(10, (DISPLAY_HEIGHT - (MINIMUM_WIDTH_THING + MARGINS + player.getIcon().getHeight())))
                y_start_thing_2 = random.randrange(height_thing_1 + MARGINS + player.getIcon().getHeight(), DISPLAY_HEIGHT - 10)
                pipe1 = gameController.createPipe(THING_WIDTH,height_thing_1, PIPE_COLOUR, x_start_things, y_start_thing_1 )
                pipe2 = gameController.createPipe(THING_WIDTH, DISPLAY_HEIGHT - y_start_thing_2, PIPE_COLOUR, x_start_things, y_start_thing_2)
                pipes.append(pipe1)
                pipes.append(pipe2)
                space_between_things = random.randrange(200, 400)

        pygame.display.update()
        clock.tick(100)


game_loop()
pygame.quit()
quit()