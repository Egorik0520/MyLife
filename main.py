import pygame

W = 800
H = 600

x = 400
y = 300

pygame.init()
pygame.display.set_caption('Змейка')
display = pygame.display.set_mode((W,H))
pygame.mouse.set_visible(True)

green = (0,128,0)
red = (255,0,0)

start = True
while start:
    for game in pygame.event.get():
        if game.type == pygame.QUIT:
            start = False
    display.fill(green)
    pygame.draw.rect(display,red(x,y,60,60))
    pygame.display.update()

