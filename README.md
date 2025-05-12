<!-- Phygame_Estela_Jose_Isabella -->

# Diamonds Slash

## **Integrantes:** Estela Boabaid, Isabella Massimini e Jose Capito

# Como funciona

# Ao iniciar o jogo clicando no botão **"Start"**, o jogador será levado para a primeira fase, ambientada em uma **mina subterrânea**.  
# Neste cenário, **diamantes** começarão a surgir de ambos os lados da tela, e o objetivo principal será **coletar o máximo possível** desses 
# diamantes utilizando uma **picareta** controlada pelo jogador no periodo de 2 minutos.

# Cada diamante possui uma **cor específica**, representando diferentes valores em pontos, e cada rodada o jogador possui 3 vidas que são perdidas 
# a cada diamante não coletado. Esses pontos são acumulados à medida que o jogador coleta os diamantes e, posteriormente, convertidos em **moedas**, que podem ser usadas na loja do jogo para adquirir melhorias (*upgrades*), como:

- Novos tipos de picaretas (mais rápidas ou com maior alcance)
- Poderes especiais (*power-ups*) que facilitam a coleta
- Aprimoramentos de velocidade(machado mais veloz, e redução da velocidade dos diamantes), resistência do machado, etc

# Ao atingir determinadas quantidades de pontos ou completar objetivos específicos, o jogador **avança para novos cenários**,  
# cada um com níveis crescentes de dificuldade e diferentes elementos visuais e mecânicos, tornando a experiência cada vez mais **desafiadora e envolvente**.

Cores e seus valores:
-**Azul** = 1 modedas
-**Verde** = 2 moedas
-**Vermelho** = 5 moedas
-**Laranja** = 10 moedas
-**Roxo** = 15 moedas

Machado e seus valores para serem desbloqueados:
-**Machado niver 1** = 
-**Machado niver 2** = 
-**Machado niver 3** = 
-**Machado niver 4** = 
-**Machado niver 5** = 

Cenarios:
-**Basico** = Caverna subterranea
-**Intermediario** = Floresta
-**Avançado** = Mina ao ar livre mistica
-**Lendario** = Marte

Powers-ups:
- **Imã de Diamantes**: atrai diamantes automaticamente
- **Tempo Congelado**: pausa os obstáculos por alguns segundos
- **Toque de Roxo**: diamantes viram todos roxos, que possuem maior valor
- **Modo Fúria da picareta**: super velocidade da picareta por tempo limitado
- **Modo calma diamantes**: reduz a velocidade dos diamantes por tempo limitado
=======

import pygame
import os
import random

pygame.init()

# Tamanho da tela
WIDTH = 500
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo da Isabella')

# Caminhos
caminho_base = os.path.dirname(__file__)
caminho_img = os.path.join(caminho_base, 'assets', 'img')

# Carrega imagens
background_inicio = pygame.image.load(os.path.join(caminho_img, 'background.jpeg')).convert()
background_inicio = pygame.transform.scale(background_inicio, (WIDTH, HEIGHT))

background_jogo = pygame.image.load(os.path.join(caminho_img, 'mina.jpeg')).convert()
background_jogo = pygame.transform.scale(background_jogo, (WIDTH, HEIGHT))

button_image = pygame.image.load(os.path.join(caminho_img, 'button.png')).convert_alpha()
button_image = pygame.transform.scale(button_image, (350, 300))

heart_img = pygame.image.load(os.path.join(caminho_img, 'heart_red.png')).convert_alpha()
heart_img = pygame.transform.scale(heart_img, (40, 40))
heart_broken_img = pygame.image.load(os.path.join(caminho_img, 'heart_broken.png')).convert_alpha()
heart_broken_img = pygame.transform.scale(heart_broken_img, (40, 40))

diamond_img = pygame.image.load(os.path.join(caminho_img, 'diamond_blue.png')).convert_alpha()
diamond_img = pygame.transform.scale(diamond_img, (80, 80))
diamond_broken_img = pygame.image.load(os.path.join(caminho_img, 'diamond_blue_broken.png')).convert_alpha()
diamond_broken_img = pygame.transform.scale(diamond_broken_img, (80, 80))

# Nova imagem da moeda
coin_img = pygame.image.load(os.path.join(caminho_img, 'coin.png')).convert_alpha()
coin_img = pygame.transform.scale(coin_img, (40, 40))

# Posição do botão
button_rect = button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

# Classe dos diamantes
class Diamante(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_normal = diamond_img
        self.image_broken = diamond_broken_img
        self.image = self.image_normal
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(20, 150)
        self.broken = False
        self.break_timer = 0

        if random.choice([True, False]):
            self.rect.x = 0
            self.speedx = random.randint(2, 4)
        else:
            self.rect.x = WIDTH
            self.speedx = -random.randint(2, 4)
        self.speedy = random.randint(3, 6)

    def update(self):
        if self.broken:
            self.break_timer += 1
            if self.break_timer > 15:
                return "remover"
        else:
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.y > HEIGHT:
                return "fim"
        return None

    def quebrar(self):
        self.image = self.image_broken
        self.broken = True

# Controle geral
game = True
tela = "inicio"
clock = pygame.time.Clock()
FPS = 30

diamantes = pygame.sprite.Group()
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 1200)

vidas = [True, True, True]
pontuacao = 0

# Loop principal
while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if tela == "inicio":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    tela = "jogo"

        elif tela == "jogo":
            if event.type == SPAWN_EVENT:
                diamantes.add(Diamante())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for d in diamantes:
                    if d.rect.collidepoint(event.pos) and not d.broken:
                        d.queb
                        
                        pontuacao += 1

    # Renderização
    if tela == "inicio":
        window.blit(background_inicio, (0, 0))
        window.blit(button_image, button_rect)

    elif tela == "jogo":
        window.blit(background_jogo, (0, 0))

        for d in list(diamantes):
            status = d.update()
            if status == "remover":
                diamantes.remove(d)
            elif status == "fim":
                for i in range(len(vidas)):
                    if vidas[i]:
                        vidas[i] = False
                        break
                diamantes.remove(d)
                if not any(vidas):
                    tela = "fim"
            else:
                window.blit(d.image, d.rect)

        # Corações
        for i in range(3):
            img = heart_img if vidas[i] else heart_broken_img
            window.blit(img, (WIDTH - (i + 1) * 50, 10))

        # Moeda + Pontuação
        window.blit(coin_img, (10, 10))
        font = pygame.font.SysFont(None, 36)
        texto_pontuacao = font.render(str(pontuacao), True, (255, 255, 0))
        window.blit(texto_pontuacao, (60, 15))

    elif tela == "fim":
        window.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 48)
        txt = font.render("Fim de jogo!", True, (255, 255, 255))
        window.blit(txt, (140, HEIGHT // 2))

    pygame.display.update()

pygame.quit()
 
>>>>>>> 6b6f52dcd424770fde689e70f57db1dad47f3132
