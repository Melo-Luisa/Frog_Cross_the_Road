import pygame, easygui, sys
import os
from pathlib import Path

def caminho_arquivo(nome):
    caminho = os.getcwd()
    caminhoAbsoluto = os.path.join(caminho, "sapinho/img", nome)
    caminhoAbsoluto = Path(caminhoAbsoluto)
    return caminhoAbsoluto

def perdedor():
    imagemFundo = pygame.image.load(caminho_arquivo('perdeu.jpg'))
    imagemFundo = pygame.transform.scale(imagemFundo, (largura, altura))
    screen.blit(imagemFundo, (0,0))
    if keys[pygame.K_RETURN]: #para sair aperte enter
        exit()

def vencedor():
    imagemFundo = pygame.image.load(caminho_arquivo('venceu.jpg'))
    imagemFundo = pygame.transform.scale(imagemFundo, (largura, altura))
    screen.blit(imagemFundo, (0,0))
    if keys[pygame.K_RETURN]:#para sair aperte enter
        exit()

pygame.init()#inicia
pygame.display.set_caption("Cross the road")
largura = 800 #tamanho da tela
altura = 600
screen = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()
running = True #loop



# Carrega as imagens
vidas = pygame.image.load(caminho_arquivo('vidas_completo.png')) #imagens da vida
vidas = pygame.transform.scale(vidas, (150, 150)) #redimensão

imagemFundo = pygame.image.load(caminho_arquivo('rua.png'))

sapinho = pygame.image.load(caminho_arquivo('sapinho.png')) #player - jogador
sapinho_redimensionada = pygame.transform.scale(sapinho, (120, 100)) #redimensão

carro = pygame.image.load(caminho_arquivo('carro.png'))#carros imagens
carro_redimensionado = pygame.transform.scale(carro, (10, 10)) #redimensão



# Define as variáveis de posição e velocidade
player_pos = pygame.Vector2(350, 0)
player_rect = pygame.Rect(player_pos.x, player_pos.y, 50, 50)
velocidade1 = 10

carros = [
    {'img': carro, 'rect': pygame.Rect(200, 50, 50, 50), 'velocidade': 6},
    {'img': carro, 'rect': pygame.Rect(300, 150, 50, 50), 'velocidade': 3},
    {'img': carro, 'rect': pygame.Rect(500, 240, 50, 50), 'velocidade': 8},
    {'img': carro, 'rect': pygame.Rect(700, 320, 50, 50), 'velocidade': 4}
]
coracoes = 3 #vidas

inicio = easygui.buttonbox('Jogo: sapinho atravessando a rua', 'Bem-Vindo', ('Instruções', 'Jogar', 'Sair'))
if inicio == 'Instruções':
    tutorial = easygui.buttonbox('Seu objetivo é fazer com que a sapinho travesse a rua, utilizando as setas. Você possui 3 vidas. Caso perca ou ganhe para sair da imagem final aperte o enter.', 'Instruções', ('Voltar', 'Jogar'))
    if tutorial == 'Voltar':
        inicio = easygui.buttonbox('Jogo: sapinho Atravessando a rua', 'Bem-Vindo', ('Instruções', 'Jogar', 'Sair'))
    else: 
        running
elif inicio == 'Sair':
    running = False
    exit()
else:
    pass


while running: #corre o codigo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fundo
    screen.blit(imagemFundo, (0,0))
    #vidas
    screen.blit(vidas, (10, 10))
    # Desenha a imagem da sapinho na posição do jogador
    screen.blit(sapinho_redimensionada, player_pos)

    #habilita as teclas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= velocidade1
    if keys[pygame.K_DOWN]:
        player_pos.y += velocidade1
    if keys[pygame.K_LEFT]:
        player_pos.x -= velocidade1
    if keys[pygame.K_RIGHT]:
        player_pos.x += velocidade1

    player_rect.x = player_pos.x
    player_rect.y = player_pos.y
    #print("Posição do jogador:", player_pos.x, player_pos.y)
   
    #mostrandos o carros dentro da tela e com a velocidade correspondente
    for carro in carros:
        carro['rect'].x += carro['velocidade'] #anda na linha de acordo com a velocidade

        if carro['rect'].x > largura: #caso passe da tela
            carro['rect'].x = -50  # Reinicia a posição do carro

        carro_img_redimensionado = pygame.transform.scale(carro['img'], (200, 200)) #coloca o carro no tamanho de acordo com a lista
        screen.blit(carro_img_redimensionado, carro['rect']) #imprimi imagem

        if player_rect.colliderect(carro['rect']):
            coracoes -= 1  # Diminui uma vida
            player_pos = pygame.Vector2(350, 0)  # Reseta a posição da sapinho
            break
        
    if coracoes == 2:
        vidas = pygame.image.load(caminho_arquivo('vidas_2.png'))
        vidas = pygame.transform.scale(vidas, (150, 150))
        screen.blit(vidas, (10, 10))
    elif coracoes == 1:
        vidas = pygame.image.load(caminho_arquivo('vidas_3.png'))
        vidas = pygame.transform.scale(vidas, (150, 150))
        screen.blit(vidas, (10, 10))
    elif coracoes == 0: #morreu
        vidas = pygame.image.load(caminho_arquivo('sem_vidas.png'))
        vidas = pygame.transform.scale(vidas, (150, 150))
        screen.blit(vidas, (10, 10))
        perdedor()
    if player_pos.y >= 460: #venceu
        #print('venceu')
        vencedor()
            
    pygame.display.update()
    clock.tick(120) 

pygame.quit()