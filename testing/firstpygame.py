from itertools import compress
import pygame
pygame.init()


my_font = pygame.font.Font(None,72)
test_text = my_font.render("Hello P390", 1, (200,10,200))
test_text_pos = test_text.get_rect(centerx = 400)

#Helper functions
def which_buttons (bs):
    return(list(compress(range(len(bs)),bs)))

#button colors
clrs = [(0,0,255),(0,225,0),(225,0,0)]
actv_clr = 0
rslts = {'trial_num': -1,'color' : None ,'time' : None}

mywindow = pygame.display.set_mode([800,800])
running = True
myrt_clock = pygame.time.Clock()
t1 = myrt_clock.tick(60)
anew = pygame.mouse.get_pressed()
trl = -1,
clr = clrs[0]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mywindow.fill((128,15,15))
    pygame.draw.circle(mywindow, clrs[actv_clr], (400,400), 75)
    mywindow.blit(test_text, test_text_pos)
    pygame.display.flip()
    aold = pygame.mouse.get_pressed()
    if(any(aold) and (aold != anew)):
        t2 = myrt_clock.tick(60)
        rslts['time'] = t2 - t1
        rslts['trial_num'] = rslts['trial_num'] + 1
        actv_clr = which_buttons(aold)[0]
        rslts['color'] = actv_clr
        anew = aold
        print(rslts)
        
pygame.quit()
