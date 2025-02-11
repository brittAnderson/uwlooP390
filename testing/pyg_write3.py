import pygame
pygame.init()


my_font = pygame.font.Font(None,72)
test_text = my_font.render("Hello P390", 1, (200,10,200))
test_text_pos = test_text.get_rect(centerx = 400)

mywindow = pygame.display.set_mode([800,800])
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mywindow.fill((128,15,15))
    pygame.draw.circle(mywindow, (0,200,0), (400,400), 75)
    mywindow.blit(test_text, test_text_pos)
    pygame.display.flip()
        
pygame.quit()
