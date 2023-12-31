import pygame
from pygame import mixer
import time
import random


#DODGE IT game

# need a font change

pygame.init()

display_width= 800
display_height= 600

black = (0,0,0)
mint = (134,252,162)
red= (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Dodge it')

clock = pygame.time.Clock()

dogeImg= pygame.image.load('doge.png')
dogeImg2= pygame.image.load('doge2.png')
cocoImg= pygame.image.load('coconut1.png') #12
beach= pygame.image.load('beach.png')

mixer.init()
mixer.music.load('bgm.ogg') #beach music
hit_sound = pygame.mixer.Sound('hit.ogg') #coco-hits-sound

def coconut_dodge(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged : " +str(count), True, black)
    gameDisplay.blit(text,(0,0))
def coconut(x,y):        #thing
    gameDisplay.blit(cocoImg,(x,y))
    
def doge(x,y,dog_pos):
    if dog_pos == 0:
        gameDisplay.blit(dogeImg,(x,y))
    if dog_pos == 1:
        gameDisplay.blit(dogeImg2,(x,y))
def crash():
    mixer.music.pause() #beach music stop
    hit_sound.play() #sound
    message_display('Game Over')
     
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('PlaymegamesReguler-2OOee.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    time.sleep(6)
    game_loop()
    
def game_loop():
    x = (display_width * 0.40)
    y = (display_height * 0.70)
    x_change = 0
    dog_pos = 0
    dog_width = 140
    coco_startx = random.randrange(0,650)
    coco_starty = -500
    coco_speed = 7
    coco_height = 85
    coco_width = 85
    #thing width-height?
    dodged = 0
   
    
    gameExit = False
    mixer.music.play(-1) #loops
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dog_pos = 1
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    dog_pos = 0
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change 

        #gameDisplay.fill(mint) #game-background
        gameDisplay.blit(beach,(0,0))
        coconut(coco_startx,coco_starty)
        coco_starty += coco_speed
        doge(x,y,dog_pos)
        coconut_dodge(dodged)

        if x > display_width - dog_width or x < 0:
            x_change = 0
        
        if coco_starty > display_height:
            coco_starty = 0 - coco_height
            coco_startx = random.randrange(0,750)
            dodged += 1
            coco_speed += 0.5

        if y < coco_starty+coco_height:
            print('y crossover')
            #if x > coco_startx and x < coco_startx + coco_width or x+dog_width > coco_startx and x + dog_width < coco_startx+coco_width :
            #if (x + dog_width > coco_startx and x < coco_startx + coco_width) or (x < coco_startx and x + dog_width > coco_startx + coco_width):
            if x < coco_startx + coco_width and x + dog_width > coco_startx:
                print('x crossover')
                crash()
        pygame.display.update()
        clock.tick(60)

game_loop()        
pygame.quit()
quit()
