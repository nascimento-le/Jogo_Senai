
# Example file showing a basic pygame "game loop"
import pygame as pg

# pygame setup
pg.init() #iniciando o projeto
pg.font.init() #Trazendo a inicialização da fonte utilizada no game
screen = pg.display.set_mode((500, 500)) # Configura o tamanho da tela
pg.display.set_caption("Jogo da velha") #Configura o nome da janela
clock = pg.time.Clock() #biblioteca do tempo
fonte_quadros = pg.font.SysFont("Comic Sans Ms", 30) #seleciono o tipo de fonte e tamanho para o meu parametro

running = True 
cor_fundo = 1 #parametro para cor inicial

jogador1 = fonte_quadros.render("X", True, "black")
jogador2 = fonte_quadros.render("O", True, "black")


while running:
    # controle de eventos do jogo
    # pygame.QUIT evento que ao clicar no X encerra a janela
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN: #evento que indica que o botão foi clicado
            print("Clicou")
            cor_fundo += 1
            if(cor_fundo > 3): #se clicarmos mais que 3x aparecerá a primeira opção de cor, como um looping 
                cor_fundo = 1

    if cor_fundo == 1:
        #screen.fill("blue") #primeiro clique aparece esta primeira cor
        screen.blit(jogador1,(230, 250)) #quando eu selecionar, aparecerá o ícone do jogador 1
    elif cor_fundo == 2:
        #screen.fill("orange") #segundo clique aparece esta segunda cor
        screen.blit(jogador2,(290,250)) #quando eu selecionar, aparecerá o ícone do jogador 2
    else:
        screen.fill("purple") #terceiro clique aparece esta terceira cor

    # flip() the display to put your work on screen
    pg.display.flip()
    

    clock.tick(60)  # limita FPS para 60

pg.quit()