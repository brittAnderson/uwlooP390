import pygame
pygame.init()


mywindow = pygame.display.set_mode([800,800])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mywindow.fill((128,15,15))
    pygame.display.flip()
        
pygame.quit()
