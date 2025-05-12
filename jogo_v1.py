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
caminho_img = os.path.join(caminho_base, 'imagens')  # ← alterado aqui

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

# Azul
diamond_img = pygame.image.load(os.path.join(caminho_img, 'diamond_blue.png')).convert_alpha()
diamond_img = pygame.transform.scale(diamond_img, (80, 80))
diamond_broken_img = pygame.image.load(os.path.join(caminho_img, 'diamond_blue_broken.png')).convert_alpha()
diamond_broken_img = pygame.transform.scale(diamond_broken_img, (80, 80))

# Vermelho
diamond_vermelho_img = pygame.image.load(os.path.join(caminho_img, 'diamond_vermelho.png')).convert_alpha()
diamond_vermelho_img = pygame.transform.scale(diamond_vermelho_img, (80, 80))
diamond_vermelho_broken_img = pygame.image.load(os.path.join(caminho_img, 'diamond_vermelho_broken.png')).convert_alpha()
diamond_vermelho_broken_img = pygame.transform.scale(diamond_vermelho_broken_img, (80, 80))

# Moeda
coin_img = pygame.image.load(os.path.join(caminho_img, 'coin.png')).convert_alpha()
coin_img = pygame.transform.scale(coin_img, (40, 40))

# Botão
button_rect = button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

# Classe dos diamantes
class Diamante(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # 25% de chance de ser vermelho
        if random.random() < 0.5:
            self.tipo = "vermelho"
            self.image_normal = diamond_vermelho_img
            self.image_broken = diamond_vermelho_broken_img
            velocidade_extra = 3
        else:
            self.tipo = "azul"
            self.image_normal = diamond_img
            self.image_broken = diamond_broken_img
            velocidade_extra = 1

        self.image = self.image_normal
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(20, 150)

        self.broken = False
        self.break_timer = 0

        if random.choice([True, False]):
            self.rect.x = 0
            self.speedx = random.randint(2, 4) + velocidade_extra
        else:
            self.rect.x = WIDTH
            self.speedx = -random.randint(2, 4) - velocidade_extra

        self.speedy = random.randint(3, 6) + velocidade_extra

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
                        d.quebrar()
                        # Ganha 2 moedas se for vermelho
                        if d.tipo == "vermelho":
                            pontuacao += 2
                        else:
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
