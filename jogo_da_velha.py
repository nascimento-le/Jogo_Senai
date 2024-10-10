
# Example file showing a basic pygame "game loop"
import pygame as pg

# pygame setup
pg.init()
screen = pg.display.set_mode((500, 500))
clock = pg.time.Clock()
running = True
cor_fundo = 1 #azul
#cor_fundo = 2 #vermelho

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            print("Clicou")
            cor_fundo += 1
            if(cor_fundo > 3):
                cor_fundo = 1


    if cor_fundo == 1:
        screen.fill("blue")
    elif cor_fundo == 2:
        screen.fill("orange")
    else:
        screen.fill("purple")

    # flip() the display to put your work on screen
    pg.display.flip()
    

    clock.tick(60)  # limits FPS to 60

pg.quit()