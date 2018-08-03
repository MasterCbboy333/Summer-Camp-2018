import pygame
#----Variables---#
screensize = [1000,700]
red = (255,0,0)
green = (0,128,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
padelsize = [100,40]
padelx=screensize[0]/2
padely=screensize[1]-100
#--End of Variables---#
pygame.init()
screen = pygame.display.set_mode((screensize[0],screensize[1]))
pygame.display.set_caption("Aiden's game")
clock = pygame.time.Clock()
screen.fill(red)

close = False

while not close: #game loop
    for event in pygame.event.get():#event handeling loop
        if event.type == pygame.QUIT:
            close = True       
    
    pygame.draw.rect(screen,blue,(padelx,padely,padelsize[0],padelsize[1]))
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
