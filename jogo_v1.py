import pygame
import os
import random

pygame.init()

# Tamanho da tela
WIDTH = 900
HEIGHT = 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Diamonds Slash')


# Caminhos
caminho_base = os.path.dirname(__file__)
caminho_img = os.path.join(caminho_base, 'imagens')

#SONS
pygame.mixer.init()

# Caminho dos sons
caminho_som = os.path.join(caminho_base, 'sons')

# Sons de quebra
som_quebra_diamante = pygame.mixer.Sound(os.path.join(caminho_som, 'cristal_quebrando.wav'))
som_quebra_pedra = pygame.mixer.Sound(os.path.join(caminho_som, 'pedra_quebrando.wav'))

#Ajustando os sons
som_quebra_diamante.set_volume(0.1)
som_quebra_pedra.set_volume(0.1)

# Carrega imagens
background_inicio = pygame.image.load(os.path.join(caminho_img, 'background.png')).convert()
background_inicio = pygame.transform.scale(background_inicio, (WIDTH, HEIGHT))

# Cronometro
fonte = pygame.font.SysFont("arial", 36)
tempo_inicial = pygame.time.get_ticks()  # em milissegundos
tempo_total = 60 * 1000  # 60 segundos em milissegundos

#Botão menu 
menu = pygame.image.load(os.path.join(caminho_img, 'menu_bottao.png')).convert_alpha()
menu_tam = pygame.transform.scale(menu, (350, 300))


# Orbe amaldiçoado
orbe_img = pygame.image.load(os.path.join(caminho_img, 'orbe.png')).convert_alpha()
orbe_img = pygame.transform.scale(orbe_img, (80, 80))

background_jogo = pygame.image.load(os.path.join(caminho_img, 'mina.png')).convert()
background_jogo = pygame.transform.scale(background_jogo, (WIDTH, HEIGHT))

background_mundos = pygame.image.load(os.path.join(caminho_img, 'fundo_mundos.jpg')).convert()
background_mundos = pygame.transform.scale(background_mundos, (WIDTH, HEIGHT))

background_mistico = pygame.image.load(os.path.join(caminho_img, 'mistico.png')).convert()
background_mistico = pygame.transform.scale(background_mistico, (WIDTH, HEIGHT))

background_planeta = pygame.image.load(os.path.join(caminho_img, 'mundo.png')).convert()
background_planeta = pygame.transform.scale(background_planeta, (WIDTH, HEIGHT))

background_verde = pygame.image.load(os.path.join(caminho_img, 'mundo_verde.png')).convert()
background_verde = pygame.transform.scale(background_verde, (WIDTH, HEIGHT))

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
recomeco = pygame.transform.scale(recomeco, (210, 100))
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
diamond_laranja_broken_img = pygame.image.load(os.path.join(caminho_img, 'broken_laranja.png')).convert_alpha()
diamond_laranja_broken_img = pygame.transform.scale(diamond_laranja_broken_img, (80, 80))

# Verde
diamond_verde_img = pygame.image.load(os.path.join(caminho_img, 'diamante_verde.png')).convert_alpha()
diamond_verde_img = pygame.transform.scale(diamond_verde_img, (80, 80))
diamond_verde_broken_img = pygame.image.load(os.path.join(caminho_img, 'diamons_verde_broken.png')).convert_alpha()
diamond_verde_broken_img = pygame.transform.scale(diamond_verde_broken_img, (80, 80))

# Moeda
coin_img = pygame.image.load(os.path.join(caminho_img, 'coin.png')).convert_alpha()
coin_img = pygame.transform.scale(coin_img, (40, 40))

# Pedra
pedra_img = pygame.image.load(os.path.join(caminho_img, 'pedra.png')).convert_alpha()
pedra_img = pygame.transform.scale(pedra_img, (50, 50))
pedra_broken_img = pygame.image.load(os.path.join(caminho_img, 'pedra_broken.png')).convert_alpha()
pedra_broken_img = pygame.transform.scale(pedra_broken_img, (50, 50))

#mundos
mundo_planeta_img = pygame.image.load(os.path.join(caminho_img, 'bottao_planeta.png')).convert_alpha()
mundo_planeta_img = pygame.transform.scale(mundo_planeta_img, (200, 200))
mundo_mistico_img = pygame.image.load(os.path.join(caminho_img, 'bottao_mistico.png')).convert_alpha()
mundo_mistico_img = pygame.transform.scale(mundo_mistico_img, (200, 200))

#bloq
mundo_mistico_bloq = pygame.image.load(os.path.join(caminho_img, 'mistico_bloq.png')).convert_alpha()
mundo_mistico_bloq = pygame.transform.scale(mundo_mistico_bloq, (200, 200))

mundo_verde_img = pygame.image.load(os.path.join(caminho_img, 'bottao_verde.png')).convert_alpha()
mundo_verde_img = pygame.transform.scale(mundo_verde_img, (200, 200))
mundo1_img = pygame.image.load(os.path.join(caminho_img, 'bottao_mundoB.png')).convert_alpha()
mundo1_img = pygame.transform.scale(mundo1_img, (200, 200))

# Botão inferior direito na tela de mundos
botao_extra_img = pygame.image.load(os.path.join(caminho_img, 'botao_extra.png')).convert_alpha()
botao_extra_img = pygame.transform.scale(botao_extra_img, (200, 150))

button_rect = button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
mundo_planeta_rect = mundo_planeta_img.get_rect(center=( 2 *WIDTH // 3, (HEIGHT // 2) + 85))
mundo_mistico_rect = mundo_mistico_img.get_rect(center=(2 * WIDTH // 3, (HEIGHT // 2) - 150))
mundo_verde_rect = mundo_verde_img.get_rect(center=( WIDTH // 3, (HEIGHT // 2) + 85))
mundo1_rect = mundo1_img.get_rect(center=( WIDTH // 3, (HEIGHT // 2) - 150))
menu_rect = menu_tam.get_rect(center=(WIDTH // 2, HEIGHT // 1.25))
botao_extra_rect = botao_extra_img.get_rect(bottomright=(WIDTH - 10, HEIGHT - 10))

mundos_desbloqueio = {
    "mundo_planeta": {"custo": 250, "desbloqueado": False},
    "mundo_mistico": {"custo": 750, "desbloqueado": False},
    "mundo_verde": {"custo": 1200, "desbloqueado": False}
}

class Diamante(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        chance = random.random()
        if chance < 0.04:
            self.tipo = "orbe"
            self.image_normal = orbe_img
            self.image_broken = orbe_img  
            velocidade_extra = 5
        elif chance < 0.08:
            self.tipo = "roxo"
            self.image_normal = diamond_roxo_img
            self.image_broken = diamond_roxo_broken_img
            velocidade_extra = 10
        elif chance < 0.20:
            self.tipo = "laranja"
            self.image_normal = diamond_laranja_img
            self.image_broken = diamond_laranja_broken_img
            velocidade_extra = 7.5
        elif chance < 0.35:
            self.tipo = "verde"
            self.image_normal = diamond_verde_img
            self.image_broken = diamond_verde_broken_img
            velocidade_extra = 5
        elif chance < 0.50:
            self.tipo = "vermelho"
            self.image_normal = diamond_vermelho_img
            self.image_broken = diamond_vermelho_broken_img
            velocidade_extra = 4
        elif chance < 0.75:
            self.tipo = "pedra"
            self.image_normal = pedra_img
            self.image_broken = pedra_broken_img
            velocidade_extra = 1
        else:
            self.tipo = "azul"
            self.image_normal = diamond_img
            self.image_broken = diamond_broken_img
            velocidade_extra = 2

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
        # Som correspondente
        if self.tipo == "pedra":
            som_quebra_pedra.play()
        else:
            som_quebra_diamante.play()


game = True
tela = "inicio"
clock = pygame.time.Clock()
FPS = 30


diamantes = pygame.sprite.Group()
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 1200)

vidas = [True, True, True]
pontuacao = 0
moedas_totais = 0  # Total acumulado entre rodadas
fase_atual = "padrao"


mensagem_mundo = ""
tempo_mensagem = 0


while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if tela == "inicio":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    tela = "selecionar_mundo"
        elif tela == "selecionar_mundo":
            if event.type == pygame.MOUSEBUTTONDOWN:

        # MUNDO PLANETA
                if mundo_planeta_rect.collidepoint(event.pos):
                    if mundos_desbloqueio["mundo_planeta"]["desbloqueado"]:
                        tela = "jogo"
                        fase_atual = "mundo_planeta"
                        tempo_inicial = pygame.time.get_ticks()
                        pontuacao = 0
                        vidas = [True, True, True]
                        diamantes.empty()
                    elif moedas_totais >= mundos_desbloqueio["mundo_planeta"]["custo"]:
                        moedas_totais -= mundos_desbloqueio["mundo_planeta"]["custo"]
                        mundos_desbloqueio["mundo_planeta"]["desbloqueado"] = True
                        print("Mundo Planeta desbloqueado!")
                    else:
                        print("Moedas insuficientes para desbloquear o Mundo Planeta.")

        # MUNDO MÍSTICO
                elif mundo_mistico_rect.collidepoint(event.pos):
                    if mundos_desbloqueio["mundo_mistico"]["desbloqueado"]:
                        tela = "jogo"
                        fase_atual = "mundo_mistico"
                        tempo_inicial = pygame.time.get_ticks()
                        pontuacao = 0
                        vidas = [True, True, True]
                        diamantes.empty()
                    elif moedas_totais >= mundos_desbloqueio["mundo_mistico"]["custo"]:
                        moedas_totais -= mundos_desbloqueio["mundo_mistico"]["custo"]
                        mundos_desbloqueio["mundo_mistico"]["desbloqueado"] = True
                        mensagem_mundo = "Mundo Místico desbloqueado!"
                        tempo_mensagem = pygame.time.get_ticks()
                    else:
                            mensagem_mundo = "Moedas insuficientes para desbloquear o Mundo Místico."
                            tempo_mensagem = pygame.time.get_ticks()
                    

        # MUNDO VERDE
                elif mundo_verde_rect.collidepoint(event.pos):
                    if mundos_desbloqueio["mundo_verde"]["desbloqueado"]:
                        tela = "jogo"
                        fase_atual = "mundo_verde"
                        tempo_inicial = pygame.time.get_ticks()
                        pontuacao = 0
                        vidas = [True, True, True]
                        diamantes.empty()
                    elif moedas_totais >= mundos_desbloqueio["mundo_verde"]["custo"]:
                        moedas_totais -= mundos_desbloqueio["mundo_verde"]["custo"]
                        mundos_desbloqueio["mundo_verde"]["desbloqueado"] = True
                        print("Mundo Verde desbloqueado!")
                    else:
                        print("Moedas insuficientes para desbloquear o Mundo Verde.")
        # MUNDO MINA (sempre desbloqueado)
                elif mundo1_rect.collidepoint(event.pos):  # supondo que esse botão é o da mina
                    tela = "jogo"
                    fase_atual = "mina"
                    tempo_inicial = pygame.time.get_ticks()
                    pontuacao = 0
                    vidas = [True, True, True]
                    diamantes.empty()

                elif botao_extra_rect.collidepoint(event.pos):
                    tela = "menu_extra"
                    
        elif tela == "jogo":
            if event.type == SPAWN_EVENT:
                diamantes.add(Diamante())
            # Detecção contínua de clique com o mouse sobre diamantes
        if tela == "jogo" and pygame.mouse.get_pressed()[0]:  # Botão esquerdo pressionado
            mouse_pos = pygame.mouse.get_pos()
            for d in diamantes:
                if d.rect.collidepoint(mouse_pos) and not d.broken:
                    d.quebrar()
                    if d.tipo == "orbe":
                        vidas = [False, False, False]
                        tela = "fim"
                    elif d.tipo == "pedra":
                        for i in range(len(vidas)):
                            if vidas[i]:
                                vidas[i] = False
                                break
                        if not any(vidas):
                            # moedas_totais += pontuacao
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

            # Tempo restante
            tempo_passado = pygame.time.get_ticks() - tempo_inicial
            tempo_restante = max(0, (tempo_total - tempo_passado) // 1000)  # em segundos
            # Exibe no canto superior direito
            texto_tempo = fonte.render(f"{tempo_restante}s", True, (255, 255, 255))
            largura_texto = texto_tempo.get_width()
            window.blit(texto_tempo, ((WIDTH - largura_texto) // 2, 10))
            # Quando tempo acabar
            if tempo_restante <= 0:
                moedas_totais += pontuacao
                tela = "fim"
            

        if tela == "fim":
            # moedas_totais += pontuacao
            if event.type == pygame.MOUSEBUTTONDOWN:
                if recomeco_rect.collidepoint(event.pos):
                    tela = "jogo"
                    vidas = [True, True, True]
                    tempo_inicial = pygame.time.get_ticks()
                    pontuacao = 0
                    diamantes.empty()
                elif menu_rect.collidepoint(event.pos):
                    tela = "selecionar_mundo"


        elif tela in ["mundo_planeta", "mundo_mistico", "mundo1", "mundo_verde"]:
            if event.type == pygame.KEYDOWN:
                tela = "inicio"

        elif tela == "menu_extra":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    tela = "selecionar_mundo"

    # TELAS
    if tela == "inicio":
        window.blit(background_inicio, (0, 0))
        window.blit(button_image, button_rect)
        window.blit(coin_img, (10, 10))
        texto_moedas = pygame.font.SysFont(None, 36).render(str(moedas_totais), True, (255, 255, 0))
        window.blit(texto_moedas, (60, 15))

    elif tela == "selecionar_mundo":
        window.blit(background_jogo, (0, 0))
        # Mostrar moedas totais acumuladas no topo
        window.blit(coin_img, (10, 10))
        texto_moedas_totais = pygame.font.SysFont(None, 36).render(str(moedas_totais), True, (255, 255, 0))
        window.blit(texto_moedas_totais, (60, 15))
        # Mundo Planeta
        if mundos_desbloqueio["mundo_planeta"]["desbloqueado"]:
            window.blit(mundo_planeta_img, mundo_planeta_rect)
        #else:
           #window.blit(mundo_planeta_bloq, mundo_planeta_rect)
        window.blit(botao_extra_img, botao_extra_rect)

    # Mundo Místico
        if mundos_desbloqueio["mundo_mistico"]["desbloqueado"]:
            window.blit(mundo_mistico_img, mundo_mistico_rect)
        else:
            window.blit(mundo_mistico_bloq, mundo_mistico_rect)

    # Mundo Verde
        if mundos_desbloqueio["mundo_verde"]["desbloqueado"]:
            window.blit(mundo_verde_img, mundo_verde_rect)
        #else:
            #window.blit(mundo_verde_bloq, mundo_verde_rect)

    # Mundo Mina (sempre desbloqueado, usa apenas 1 imagem)
        window.blit(mundo1_img, mundo1_rect)


    elif tela == "mundo_planeta":
        window.fill((10, 10, 50))
        font = pygame.font.SysFont(None, 48)
        texto = font.render("Você entrou no Mundo Planeta!", True, (255, 255, 255))
        window.blit(background_planeta, (0, 0))
        sub = pygame.font.SysFont(None, 24).render("Pressione ESPAÇO para voltar", True, (180, 180, 180))
        window.blit(sub, (80, HEIGHT // 2 + 30))

    elif tela == "mundo_mistico":
        window.fill((50, 10, 30))
        font = pygame.font.SysFont(None, 48)
        texto = font.render("Você entrou no Mundo Místico!", True, (255, 255, 255))
        window.blit(background_mistico, (0 , 0))
        sub = pygame.font.SysFont(None, 24).render("Pressione ESPAÇO para voltar", True, (180, 180, 180))
        window.blit(sub, (90, HEIGHT // 2 + 30))

    elif tela == "mundo_verde":
        window.fill((50, 10, 30))
        font = pygame.font.SysFont(None, 48)
        texto = font.render("Você entrou no Mundo Verde!", True, (255, 255, 255)) 
        window.blit(background_verde, (0 , 0))
        sub = pygame.font.SysFont(None, 24).render("Pressione ESPAÇO para voltar", True, (180, 180, 180))
        window.blit(sub, (80, HEIGHT // 2 + 30))


    elif tela == "mundo1":
        window.fill((50, 10, 30))
        font = pygame.font.SysFont(None, 48)
        texto = font.render("Você entrou no Mundo Místico!", True, (255, 255, 255))
        window.blit(background_jogo, (0 , 0))
        sub = pygame.font.SysFont(None, 24).render("Pressione ESPAÇO para voltar", True, (180, 180, 180))
        window.blit(sub, (80, HEIGHT // 2 + 30))

    elif tela == "jogo":
        if fase_atual == "mundo_planeta":
            window.blit(background_planeta, (0, 0))
        elif fase_atual == "mundo_mistico":
            window.blit(background_mistico, (0, 0))
        elif fase_atual == "mundo_verde":
            window.blit(background_verde, (0, 0))
        elif fase_atual == "mundo1":
            window.blit(background_jogo, (0, 0))
        else:
            window.blit(background_jogo, (0, 0))
        # Atualiza e desenha diamantes
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
                    moedas_totais += pontuacao
                    tela = "fim"
            else:
                window.blit(d.image, d.rect)
        # Desenha corações (vidas)
        for i in range(3):
            img = heart_img if vidas[i] else heart_broken_img
            window.blit(img, (WIDTH - (i + 1) * 50, 10))

        # Desenha moeda e pontuação
        window.blit(coin_img, (10, 10))
        moed_part = pygame.font.SysFont(None, 36).render(str(pontuacao), True, (255, 255, 0))
        window.blit(moed_part, (60, 15))


        # Desenha cronômetro no topo centralizado
        tempo_passado = pygame.time.get_ticks() - tempo_inicial
        tempo_restante = max(0, (tempo_total - tempo_passado) // 1000)
        texto_tempo = fonte.render(f"{tempo_restante}s", True, (255, 255, 255))
        largura_texto = texto_tempo.get_width()
        window.blit(texto_tempo, ((WIDTH - largura_texto) // 2, 10))
        # Desenha picareta
        pos_mouse = pygame.mouse.get_pos()
        window.blit(picareta_ini, pos_mouse)


    elif tela == "fim":
        window.blit(background_jogo, (0, 0))
        font = pygame.font.SysFont(None, 48)
        txt = font.render("Fim de jogo!", True, (255, 255, 255))
        window.blit(txt, (155, HEIGHT // 2 - 80))
        window.blit(recomeco, recomeco_rect)
        window.blit(coin_img, (10, 10))
        window.blit(menu_tam, menu_rect)
        moed_t = pygame.font.SysFont(None, 36).render(str(moedas_totais), True, (255, 255, 0))
        window.blit(moed_t, (60, 15))
        window.blit(moed_t, (60, 15))  # Moedas totais 

    elif tela == "menu_extra":
        window.blit(background_jogo, (0, 0)) 
            
    
    pygame.display.update()

pygame.quit()