import pygame
import os
import random

pygame.init()

# Tamanho da tela
WIDTH = 500
HEIGHT = 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Diamonds Slash')

# Caminhos
caminho_base = os.path.dirname(__file__)
caminho_img = os.path.join(caminho_base, 'imagens')

# Carrega imagens
background_inicio = pygame.image.load(os.path.join(caminho_img, 'background.jpeg')).convert()
background_inicio = pygame.transform.scale(background_inicio, (WIDTH, HEIGHT))

# Orbe amaldiçoado
orbe_img = pygame.image.load(os.path.join(caminho_img, 'orbe.png')).convert_alpha()
orbe_img = pygame.transform.scale(orbe_img, (80, 80))

background_jogo = pygame.image.load(os.path.join(caminho_img, 'mina.jpeg')).convert()
background_jogo = pygame.transform.scale(background_jogo, (WIDTH, HEIGHT))

button_image = pygame.image.load(os.path.join(caminho_img, 'button.png')).convert_alpha()
button_image = pygame.transform.scale(button_image, (350, 300))

heart_img = pygame.image.load(os.path.join(caminho_img, 'heart_red.png')).convert_alpha()
heart_img = pygame.transform.scale(heart_img, (40, 40))
heart_broken_img = pygame.image.load(os.path.join(caminho_img, 'heart_broken.png')).convert_alpha()
heart_broken_img = pygame.transform.scale(heart_broken_img, (40, 40))

# Picareta iniciante
picareta_ini = pygame.image.load(os.path.join(caminho_img, 'picareta_iniciante.png')).convert_alpha()
picareta_ini = pygame.transform.scale(picareta_ini, (70, 70))

# Simbolo de restart
recomeco = pygame.image.load(os.path.join(caminho_img, 'restart.png')).convert_alpha()
recomeco = pygame.transform.scale(recomeco, (230, 120))
recomeco_rect = recomeco.get_rect(center=(WIDTH // 2, HEIGHT // 1.85))

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

# Roxo
diamond_roxo_img = pygame.image.load(os.path.join(caminho_img, 'diamond_roxo.png')).convert_alpha()
diamond_roxo_img = pygame.transform.scale(diamond_roxo_img, (80, 80))
diamond_roxo_broken_img = pygame.image.load(os.path.join(caminho_img, 'diamond_roxo_broken.png')).convert_alpha()
diamond_roxo_broken_img = pygame.transform.scale(diamond_roxo_broken_img, (80, 80))

# Laranja
diamond_laranja_img = pygame.image.load(os.path.join(caminho_img, 'diamond_laranja.png')).convert_alpha()
diamond_laranja_img = pygame.transform.scale(diamond_laranja_img, (80, 80))
diamond_laranja_broken_img = pygame.image.load(os.path.join(caminho_img, 'diamond_laranja_broken.png')).convert_alpha()
diamond_laranja_broken_img = pygame.transform.scale(diamond_laranja_broken_img, (80, 80))

# Verde
diamond_verde_img = pygame.image.load(os.path.join(caminho_img, 'diamond_verde.png')).convert_alpha()
diamond_verde_img = pygame.transform.scale(diamond_verde_img, (80, 80))
diamond_verde_broken_img = pygame.image.load(os.path.join(caminho_img, 'diamons_verde_broken.png')).convert_alpha()
diamond_verde_broken_img = pygame.transform.scale(diamond_verde_broken_img, (80, 80))

# Moeda
coin_img = pygame.image.load(os.path.join(caminho_img, 'coin.png')).convert_alpha()
coin_img = pygame.transform.scale(coin_img, (40, 40))

# Botão
button_rect = button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

# Pedra
pedra_img = pygame.image.load(os.path.join(caminho_img, 'pedra.png')).convert_alpha()
pedra_img = pygame.transform.scale(pedra_img, (50, 50))
pedra_broken_img = pygame.image.load(os.path.join(caminho_img, 'pedra_broken.png')).convert_alpha()
pedra_broken_img = pygame.transform.scale(pedra_broken_img, (50, 50))




class Diamante(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        chance = random.random()
        if chance < 0.10:
            self.tipo = "roxo"
            self.image_normal = diamond_roxo_img
            self.image_broken = diamond_roxo_broken_img
            velocidade_extra = 7
        elif chance < 0.20:
            self.tipo = "laranja"
            self.image_normal = diamond_laranja_img
            self.image_broken = diamond_laranja_broken_img
            velocidade_extra = 5
        elif chance < 0.35:
            self.tipo = "verde"
            self.image_normal = diamond_verde_img
            self.image_broken = diamond_verde_broken_img
            velocidade_extra = 3.5
        elif chance < 0.50:
            self.tipo = "vermelho"
            self.image_normal = diamond_vermelho_img
            self.image_broken = diamond_vermelho_broken_img
            velocidade_extra = 3
        elif chance < 0.75:
            self.tipo = "pedra"
            self.image_normal = pedra_img
            self.image_broken = pedra_broken_img
            velocidade_extra = 0
        elif chance < 0.20:
            self.tipo = "orbe"
            self.image_normal = orbe_img
            self.image_broken = orbe_img  
            velocidade_extra = 1
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
                if self.tipo == "pedra":
                    return "remover"
                return "fim"
        return None

    def quebrar(self):
        self.image = self.image_broken
        self.broken = True
    


game = True
tela = "inicio"
clock = pygame.time.Clock()
FPS = 30


diamantes = pygame.sprite.Group()
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 1200)

vidas = [True, True, True]
pontuacao = 0

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
                        if d.tipo == "orbe":
                            vidas = [False, False, False]
                            tela = "fim"
                        if d.tipo == "pedra":
                            for i in range(len(vidas)):
                                if vidas[i]:
                                    vidas[i] = False
                                    break
                            if not any(vidas):
                                tela = "fim"
                        elif d.tipo == "vermelho":
                            pontuacao += 5
                        elif d.tipo == "verde":
                            pontuacao += 2
                        elif d.tipo == "laranja":
                            pontuacao += 10
                        elif d.tipo == "roxo":
                            pontuacao += 15
                        else:
                            pontuacao += 1
        elif tela == "fim":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if recomeco_rect.collidepoint(event.pos):
                    # Reinicia o jogo
                    tela = "jogo"
                    vidas = [True, True, True]
                    pontuacao = 0
                    diamantes.empty()


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

        for i in range(3):
            img = heart_img if vidas[i] else heart_broken_img
            window.blit(img, (WIDTH - (i + 1) * 50, 10))

        window.blit(coin_img, (10, 10))
        font = pygame.font.SysFont(None, 36)
        texto_pontuacao = font.render(str(pontuacao), True, (255, 255, 0))
        window.blit(texto_pontuacao, (60, 15))
        pos_mouse = pygame.mouse.get_pos()
        # Desenha o cursor personalizado na posição do mouse
        window.blit(picareta_ini, pos_mouse)

    elif tela == "fim":
        if event.type == pygame.MOUSEBUTTONDOWN:
            if recomeco_rect.collidepoint(event.pos):
                # Reinicia o jogo
                tela = "jogo"
                vidas = [True, True, True]
                pontuacao = 0
                diamantes.empty()
        elif tela == "fim":
            window.blit(background_jogo, (0, 0))
            font = pygame.font.SysFont(None, 48)
            txt = font.render("Fim de jogo!", True, (255, 255, 255))
            window.blit(txt, (140, HEIGHT // 2 - 80))
            window.blit(recomeco, recomeco_rect)


    pygame.display.update()

pygame.quit()
