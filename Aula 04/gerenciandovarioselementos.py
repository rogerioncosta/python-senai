import pygame
from random import randint, choice

def criarBola():
    posx = randint(50, 850)
    posy = randint(50, 450)

    novaBola = {
        "cor" : (randint(0, 255), randint(0, 255), randint(0, 255)),
        "velocidade" : randint(50, 250),
        "posicao" : pygame.Vector2(posx, posy),
        "direcao" : pygame.Vector2(choice([-1, 1]), choice([-1, 1])),
        "tamanho" : randint(25, 70)
    }

    return novaBola

def desenhaBolas(listaBolas):
    for bola in listaBolas:
        pygame.draw.circle(tela, bola["cor"], bola["posicao"], bola["tamanho"])

def animaBolas(listaBolas):
    for bola in listaBolas:
        bola["posicao"].y += bola["velocidade"] * bola["direcao"].y * dt
        bola["posicao"].x += bola["velocidade"] * bola["direcao"].x * dt

        if bola["posicao"].y >= (tamanho[1] - bola["tamanho"]) or bola["posicao"].y <= (0 + bola["tamanho"]):
            bola["direcao"].y *= -1
        
        if bola["posicao"].x >= (tamanho[0] - bola["tamanho"]) or bola["posicao"].x <= (0 + bola["tamanho"]):
            bola["direcao"].x *= -1

# Inicializar o pygame
pygame.init()

tamanho = (900, 500)
# Cria uma tela com tamanho especificado
tela = pygame.display.set_mode(tamanho)

#Define o título da janela
pygame.display.set_caption("Hello Games!")

# Define um relógio para controlar o FPS
relogio = pygame.time.Clock()
dt = 0

listaBolas = []

# Cria um evento para o usuário adicionar bolas
ADICIONA_BOLA = pygame.USEREVENT + 1

# Define um timer para adicionar bolas a cada 10 segundos
pygame.time.set_timer(ADICIONA_BOLA, 100)

while True:
    # Lida com os eventos da aplicação
    for evento in pygame.event.get():
        print(evento)
        if evento.type == pygame.QUIT:
            pygame.quit() # Fechando o pygame

        if evento.type == ADICIONA_BOLA:
            listaBolas.append(criarBola())

    # Preenche a tela com uma cor
    tela.fill((40, 200, 100))

    desenhaBolas(listaBolas)
    animaBolas(listaBolas)

    # Atualiza a tela
    pygame.display.update()
    dt = relogio.tick(60) / 1000 # Define a quantidade de FPS

    # relogio.tick(60) # Define a quantidade de FPS