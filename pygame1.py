import pygame

pygame.init()

display_width= 800
display_height= 600

black = (0,0,0)
white = (255,255,255)
red= (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Dodge it')

clock = pygame.time.Clock()

dogeImg= pygame.image.load('doge.png')
def doge(x,y):
    gameDisplay.blit(dogeImg,(x,y))

x = (display_width * 0.40)
y = (display_height * 0.8)

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    doge(x,y)
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()
