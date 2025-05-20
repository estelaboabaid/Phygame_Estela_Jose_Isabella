import pygame
import os
import random
import sys


pygame.init()

# Tamanho da tela
WIDTH = 900
HEIGHT = 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Diamonds Slash') #nome do jogo


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
fonte = pygame.font.SysFont("arial", 36)  # inicia a fonte que cronometro ira usar 
tempo_inicial = pygame.time.get_ticks()  # Faz o tempo rodar como um relogio
tempo_total = 60 * 1000  # 60 segundos em milissegundos

#Botão menu 
menu = pygame.image.load(os.path.join(caminho_img, 'menu_bottao.png')).convert_alpha()
menu_tam = pygame.transform.scale(menu, (350, 300))


# Orbe amaldiçoado
orbe_img = pygame.image.load(os.path.join(caminho_img, 'orbe.png')).convert_alpha()
orbe_img = pygame.transform.scale(orbe_img, (80, 80))

#tela de fundo do mundo 'mina'
background_jogo = pygame.image.load(os.path.join(caminho_img, 'mina.png')).convert()
background_jogo = pygame.transform.scale(background_jogo, (WIDTH, HEIGHT))

#tela de fundo do mundo mistico 
background_mistico = pygame.image.load(os.path.join(caminho_img, 'mistico.png')).convert()
background_mistico = pygame.transform.scale(background_mistico, (WIDTH, HEIGHT))

#tela de fundo do mundo de planetas
background_planeta = pygame.image.load(os.path.join(caminho_img, 'mundo.png')).convert()
background_planeta = pygame.transform.scale(background_planeta, (WIDTH, HEIGHT))

#tela de fundo do mundo verde
background_verde = pygame.image.load(os.path.join(caminho_img, 'mundo_verde.png')).convert()
background_verde = pygame.transform.scale(background_verde, (WIDTH, HEIGHT))

#botao de jogar 
button_image = pygame.image.load(os.path.join(caminho_img, 'button.png')).convert_alpha()
button_image = pygame.transform.scale(button_image, (350, 300))

#imagem do coracao 
heart_img = pygame.image.load(os.path.join(caminho_img, 'heart_red.png')).convert_alpha()
heart_img = pygame.transform.scale(heart_img, (40, 40))

#imagem do coracao quebrado 
heart_broken_img = pygame.image.load(os.path.join(caminho_img, 'heart_broken.png')).convert_alpha()
heart_broken_img = pygame.transform.scale(heart_broken_img, (40, 40))

# Picareta iniciante
picareta_ini = pygame.image.load(os.path.join(caminho_img, 'picareta_iniciante.png')).convert_alpha()
picareta_ini = pygame.transform.scale(picareta_ini, (70, 70))

# Simbolo de restart
recomeco = pygame.image.load(os.path.join(caminho_img, 'restart.png')).convert_alpha()
recomeco = pygame.transform.scale(recomeco, (210, 100))
recomeco_rect = recomeco.get_rect(center=(WIDTH // 2, HEIGHT // 1.85))

# diamante azul
diamond_img = pygame.image.load(os.path.join(caminho_img, 'diamond_blue.png')).convert_alpha()
diamond_img = pygame.transform.scale(diamond_img, (80, 80))
#diamante azul quebrado 
diamond_broken_img = pygame.image.load(os.path.join(caminho_img, 'diamond_blue_broken.png')).convert_alpha()
diamond_broken_img = pygame.transform.scale(diamond_broken_img, (80, 80))

# diamante vermelho
diamond_vermelho_img = pygame.image.load(os.path.join(caminho_img, 'diamond_vermelho.png')).convert_alpha()
diamond_vermelho_img = pygame.transform.scale(diamond_vermelho_img, (80, 80))
#diamante vermelho quebrado 
diamond_vermelho_broken_img = pygame.image.load(os.path.join(caminho_img, 'diamond_vermelho_broken.png')).convert_alpha()
diamond_vermelho_broken_img = pygame.transform.scale(diamond_vermelho_broken_img, (80, 80))

# diamante roxo
diamond_roxo_img = pygame.image.load(os.path.join(caminho_img, 'diamond_roxo.png')).convert_alpha()
diamond_roxo_img = pygame.transform.scale(diamond_roxo_img, (80, 80))
#diamante roxo quebrado 
diamond_roxo_broken_img = pygame.image.load(os.path.join(caminho_img, 'diamond_roxo_broken.png')).convert_alpha()
diamond_roxo_broken_img = pygame.transform.scale(diamond_roxo_broken_img, (80, 80))

# diamante laranja
diamond_laranja_img = pygame.image.load(os.path.join(caminho_img, 'diamond_laranja.png')).convert_alpha()
diamond_laranja_img = pygame.transform.scale(diamond_laranja_img, (80, 80))
#diamante laranja quebrado
diamond_laranja_broken_img = pygame.image.load(os.path.join(caminho_img, 'broken_laranja.png')).convert_alpha()
diamond_laranja_broken_img = pygame.transform.scale(diamond_laranja_broken_img, (80, 80))

# diamante verde
diamond_verde_img = pygame.image.load(os.path.join(caminho_img, 'diamante_verde.png')).convert_alpha()
diamond_verde_img = pygame.transform.scale(diamond_verde_img, (80, 80))
#diamante verde quebrado 
diamond_verde_broken_img = pygame.image.load(os.path.join(caminho_img, 'diamons_verde_broken.png')).convert_alpha()
diamond_verde_broken_img = pygame.transform.scale(diamond_verde_broken_img, (80, 80))

# Moeda
coin_img = pygame.image.load(os.path.join(caminho_img, 'coin.png')).convert_alpha()
coin_img = pygame.transform.scale(coin_img, (40, 40))
fonte_moeda = pygame.font.SysFont(None, 28)  #configura valor da moeda

# Pedra
pedra_img = pygame.image.load(os.path.join(caminho_img, 'pedra.png')).convert_alpha()
pedra_img = pygame.transform.scale(pedra_img, (50, 50))
#pedra quebrada 
pedra_broken_img = pygame.image.load(os.path.join(caminho_img, 'pedra_broken.png')).convert_alpha()
pedra_broken_img = pygame.transform.scale(pedra_broken_img, (50, 50))


#botao do mundo planeta 
mundo_planeta_img = pygame.image.load(os.path.join(caminho_img, 'bottao_planeta.png')).convert_alpha()
mundo_planeta_img = pygame.transform.scale(mundo_planeta_img, (200, 200))
#botao do mundo mistico 
mundo_mistico_img = pygame.image.load(os.path.join(caminho_img, 'bottao_mistico.png')).convert_alpha()
mundo_mistico_img = pygame.transform.scale(mundo_mistico_img, (200, 200))
#botao do mundo verde  
mundo_verde_img = pygame.image.load(os.path.join(caminho_img, 'bottao_verde.png')).convert_alpha()
mundo_verde_img = pygame.transform.scale(mundo_verde_img, (200, 200))
#botao do mundo mina 
mundo1_img = pygame.image.load(os.path.join(caminho_img, 'bottao_mundoB.png')).convert_alpha()
mundo1_img = pygame.transform.scale(mundo1_img, (200, 200))


#botao do mundo mistico bloqueado 
mundo_mistico_bloq = pygame.image.load(os.path.join(caminho_img, 'mistico_bloq.png')).convert_alpha()
mundo_mistico_bloq = pygame.transform.scale(mundo_mistico_bloq, (200, 200))
#botao do mundo planeta bloqueado 
mundo_planeta_bloq = pygame.image.load(os.path.join(caminho_img, 'planeta_bloq.png')).convert_alpha()
mundo_planeta_bloq = pygame.transform.scale(mundo_planeta_bloq, (200, 200))
#botao do mundo verde bloqueado 
mundo_verde_bloq = pygame.image.load(os.path.join(caminho_img, 'verde_bloq.png')).convert_alpha()
mundo_verde_bloq = pygame.transform.scale(mundo_verde_bloq, (200, 200))


# Botão inferior direito na tela de mundos
botao_extra_img = pygame.image.load(os.path.join(caminho_img, 'botao_extra.png')).convert_alpha()
botao_extra_img = pygame.transform.scale(botao_extra_img, (200, 150))

# Imagens dos 3 botões distintos do menu_extra
botao1_img = pygame.image.load(os.path.join(caminho_img, 'botao1.png')).convert_alpha()
botao1_img = pygame.transform.scale(botao1_img, (250, 150))

botao2_img = pygame.image.load(os.path.join(caminho_img, 'botao2.png')).convert_alpha()
botao2_img = pygame.transform.scale(botao2_img, (250, 150))

botao3_img = pygame.image.load(os.path.join(caminho_img, 'botao3.png')).convert_alpha()
botao3_img = pygame.transform.scale(botao3_img, (250, 150))

#imagem de fim de jogo 
fim_img = pygame.image.load(os.path.join(caminho_img, 'fim.png')).convert_alpha()
fim_img = pygame.transform.scale(fim_img, (500, 500))

#botao de jogar 
button_rect = button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
#botao do mundo de planeta 
mundo_planeta_rect = mundo_planeta_img.get_rect(center=( 2 *WIDTH // 3, (HEIGHT // 2) + 85))
#botao do mundo mistico 
mundo_mistico_rect = mundo_mistico_img.get_rect(center=(2 * WIDTH // 3, (HEIGHT // 2) - 150))
#botao do mundo verde 
mundo_verde_rect = mundo_verde_img.get_rect(center=( WIDTH // 3, (HEIGHT // 2) + 85))
#botao do mundo verde 
mundo1_rect = mundo1_img.get_rect(center=( WIDTH // 3, (HEIGHT // 2) - 150))
#botao do menu 
menu_rect = menu_tam.get_rect(center=(WIDTH // 2, HEIGHT // 1.25))
botao_extra_rect = botao_extra_img.get_rect(bottomright=(WIDTH - 10, HEIGHT - 10))
# Rects dos botões do menu extra
botao1_rect = botao1_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 140))
botao2_rect = botao2_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
botao3_rect = botao3_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 140))

#botao info 
botao_info = pygame.image.load(os.path.join(caminho_img, 'info.png')).convert_alpha()
botao_info = pygame.transform.scale(botao_info, (250, 150))
info_rect = botao_info.get_rect(center=(WIDTH // 2, HEIGHT // 2 +250))


#dicionario com os custos dos mundos, e define eles como bloqueados, sendo apenas desbloqueados quando o jogador compra
mundos_desbloqueio = {
    "mundo_planeta": {"custo": 250, "desbloqueado": False},
    "mundo_mistico": {"custo": 750, "desbloqueado": False},
    "mundo_verde": {"custo": 1000, "desbloqueado": False}
}

#variaveis para o controle de tela 
sequencia_info = False
indice_tela_info = 0
tempo_tela_info = 0
total_telas_info = 6

#fotos de info 
# Imagens da sequência de info
foto1 = pygame.image.load(os.path.join(caminho_img, 'foto1.png')).convert_alpha()
foto1 = pygame.transform.scale(foto1, (WIDTH, HEIGHT))
foto2 = pygame.image.load(os.path.join(caminho_img, 'foto2.png')).convert_alpha()
foto2 = pygame.transform.scale(foto2, (WIDTH, HEIGHT))
foto3 = pygame.image.load(os.path.join(caminho_img, 'foto3.png')).convert_alpha()
foto3 = pygame.transform.scale(foto3, (WIDTH, HEIGHT))
foto4 = pygame.image.load(os.path.join(caminho_img, 'foto4.png')).convert_alpha()
foto4 = pygame.transform.scale(foto4, (WIDTH, HEIGHT))
foto5 = pygame.image.load(os.path.join(caminho_img, 'foto5.png')).convert_alpha()
foto5 = pygame.transform.scale(foto5, (WIDTH, HEIGHT))
foto6 = pygame.image.load(os.path.join(caminho_img, 'foto6.png')).convert_alpha()
foto6 = pygame.transform.scale(foto6, (WIDTH, HEIGHT))
fotos_info = [foto1, foto2, foto3, foto4, foto5, foto6]


#classe de diamante 
class Diamante(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        chance = random.random() #para a chance dos diamantes serem  definidas 
        if chance < 0.07: #a orbe te chance de 7% de aparecer 
            self.tipo = "orbe"
            self.image_normal = orbe_img 
            self.image_broken = orbe_img  
            velocidade_extra = 5 #aumenta a velocidade 
        elif chance < 0.1: #chance de 8% de aparecer o diamante roxo 
            self.tipo = "roxo"
            self.image_normal = diamond_roxo_img
            self.image_broken = diamond_roxo_broken_img
            velocidade_extra = 10
        elif chance < 0.20: #chance de 20% de aparecer o diamante laranja 
            self.tipo = "laranja"
            self.image_normal = diamond_laranja_img
            self.image_broken = diamond_laranja_broken_img
            velocidade_extra = 7.5
        elif chance < 0.35: #chance de 35% de aparecer o diamante verde
            self.tipo = "verde"
            self.image_normal = diamond_verde_img
            self.image_broken = diamond_verde_broken_img
            velocidade_extra = 6
        elif chance < 0.50: #chance de 50% de aparecer o diamante vermelho
            self.tipo = "vermelho"
            self.image_normal = diamond_vermelho_img
            self.image_broken = diamond_vermelho_broken_img
            velocidade_extra = 5.5
        elif chance < 0.75: #chance de 75% de aparecer a pedra 
            self.tipo = "pedra"
            self.image_normal = pedra_img
            self.image_broken = pedra_broken_img
            velocidade_extra = 5
        else: # o resto é o azul 
            self.tipo = "azul"
            self.image_normal = diamond_img
            self.image_broken = diamond_broken_img
            velocidade_extra = 3

        self.image = self.image_normal
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(10, 200)

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

            # Atração ao cursor se ativa
            if atracao_ativa and self.tipo in ["azul", "vermelho", "verde", "laranja", "roxo"]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = mouse_x - self.rect.centerx
                dy = mouse_y - self.rect.centery
                self.rect.x += int(dx * 0.02)
                self.rect.y += int(dy * 0.02)

            if self.rect.y > HEIGHT:
                if self.tipo == "pedra" or self.tipo == "orbe":
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

vidas = [True, True, True]  # define as vidas como verdadeiras, que mostra que o jogador tem vidas
pontuacao = 0  # inicia a pontuação como 0
moedas_totais = 0  # Total acumulado entre rodadas
fase_atual = "padrao" # Fase padrão, para evitar erro de referência antes de selecionar um mundo

#POWER UPS 
atracao_ativa = False

mensagem_mundo = ""
tempo_mensagem = 0

while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        # tudo que você já tem...

        if tela == "inicio":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    tela = "selecionar_mundo"
                elif info_rect.collidepoint(event.pos):
                    tela = "info"
                    indice_tela_info = 0
                    tempo_tela_info = pygame.time.get_ticks()





        ######
        # MUNDO PLANETA
        elif tela == "selecionar_mundo":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mundo_planeta_rect.collidepoint(event.pos):
                    if mundos_desbloqueio["mundo_planeta"]["desbloqueado"]:  # se o mundo estiver desbloqueado o jogo pode comecar 
                        tela = "jogo"
                        fase_atual = "mundo_planeta" 
                        tempo_inicial = pygame.time.get_ticks() #inicia o tempo do jogo
                        pontuacao = 0
                        vidas = [True, True, True] #faz com que as vidas sejam verdadeiras
                        diamantes.empty() 
    
                    elif moedas_totais >= mundos_desbloqueio["mundo_planeta"]["custo"]:
                        moedas_totais -= mundos_desbloqueio["mundo_planeta"]["custo"]
                        mundos_desbloqueio["mundo_planeta"]["desbloqueado"] = True
                    else:
                        mensagem_mundo = "Moedas insuficientes, mundo bloqueado!"
                        tempo_mensagem = pygame.time.get_ticks()


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
                        mensagem_mundo = "Moedas insuficientes, mundo bloqueado."
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
                    else:
                        mensagem_mundo = "Moedas insuficientes, mundo bloqueado!"
                        tempo_mensagem = pygame.time.get_ticks()
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
            
        if tela == "jogo" and pygame.mouse.get_pressed()[0]:  
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

        
            #####
            # Tempo restante
            tempo_passado = pygame.time.get_ticks() - tempo_inicial
            tempo_restante = max(0, (tempo_total - tempo_passado) // 1000)  # em segundos
            # Exibe no canto superior direito
            texto_tempo = fonte.render(f"{tempo_restante}s", True, (255, 255, 255))
            largura_texto = texto_tempo.get_width()
            window.blit(texto_tempo, ((WIDTH - largura_texto) // 2, 10))
            # Quando tempo acabar
            if tempo_restante <= 0:  #Se o tempo acabar o jogo acaba
                moedas_totais += pontuacao
                tela = "fim"
            

        if tela == "fim":
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botao1_rect.collidepoint(event.pos):
                    atracao_ativa = not atracao_ativa  
                    print("Atração ativada!" if atracao_ativa else "Atração desativada!")
                elif botao2_rect.collidepoint(event.pos):
                    print("Botão 2 clicado!")
                elif botao3_rect.collidepoint(event.pos):
                    print("Botão 3 clicado!")


    if tela == "info":
            window.blit(fotos_info[indice_tela_info], (0, 0))

            if pygame.time.get_ticks() - tempo_tela_info >= 1000:
                indice_tela_info += 1
                tempo_tela_info = pygame.time.get_ticks()
                if indice_tela_info >= total_telas_info:
                    sequencia_info = False
                    tela = "inicio"
    # TELAS
    if tela == "inicio":
        window.blit(background_inicio, (0, 0))
        window.blit(button_image, button_rect)

    # Mostra botão Info
        window.blit(botao_info, info_rect)

    # Mostrar moedas
        window.blit(coin_img, (10, 10))
        texto_moedas = pygame.font.SysFont(None, 36).render(str(moedas_totais), True, (255, 255, 0))
        window.blit(texto_moedas, (60, 15))


    elif tela == "selecionar_mundo":  #Parte do codigo aonde desenha os icones na tela de selecionar o mundo 
        window.blit(background_jogo, (0, 0))

        # Mostrar moedas totais acumuladas no topo
        window.blit(coin_img, (10, 10))
        texto_moedas_totais = pygame.font.SysFont(None, 36).render(str(moedas_totais), True, (255, 255, 0))
        window.blit(texto_moedas_totais, (60, 15))

        # Mundo Planeta canto superior direito 
        if mundos_desbloqueio["mundo_planeta"]["desbloqueado"]: # Se o mundo for desbloqueado(comprado), ele ira aparecer dessa forma
            window.blit(mundo_planeta_img, mundo_planeta_rect)
        else:
            window.blit(mundo_planeta_bloq, mundo_planeta_rect)  # planeta permanece bloqueado 
            bloqueado = not mundos_desbloqueio["mundo_planeta"]["desbloqueado"] # define o que seria o mundo bloqueado
            if bloqueado: # se ele estiver bloqueado a moeda aparece
                x1, y1 = mundo_planeta_rect.center # centraliza as moedas com a posição dos mundos
                valor1 = fonte_moeda.render("500", True, (255, 255, 0))  # faz a moeda do tamanho e valor do mundo
                larg_val1 = valor1.get_width()  # Pega a largura do que sera escrito
                alt_val1 = valor1.get_height()  # Pega a altura do que sera escrito 
                window.blit(valor1, (x1 - larg_val1 //2, y1- 130))  # centraliza o valor em cima da moeda
                window.blit(coin_img, (x1 - larg_val1 //2 + larg_val1 + 5,  y1- 130 + alt_val1//2 - 20))  #desenha moeda em cima do mundo 
            window.blit(botao_extra_img, botao_extra_rect)

    # Mundo Místico, canto inferior direito
        if mundos_desbloqueio["mundo_mistico"]["desbloqueado"]:
            window.blit(mundo_mistico_img, mundo_mistico_rect)
        else:
            window.blit(mundo_mistico_bloq, mundo_mistico_rect)
            bloqueado = not mundos_desbloqueio["mundo_planeta"]["desbloqueado"]
            if bloqueado:
                x2, y2 = mundo_planeta_rect.center 
                val2 = fonte_moeda.render("250", True, (255, 255, 0))
                alt_val2 = val2.get_height()  
                largura_val2 = val2.get_width() 
                window.blit(coin_img, (x2 + largura_val2//2+5, y2 + 100 + alt_val2//2 - 20)) 
                window.blit(val2, (x2 - largura_val2//2, y2 + 100))
            window.blit(botao_extra_img, botao_extra_rect)
            
    # Mundo Verde canto inferior esquerdo
        if mundos_desbloqueio["mundo_verde"]["desbloqueado"]:
            window.blit(mundo_verde_img, mundo_verde_rect)
        else:
            window.blit(mundo_verde_bloq, mundo_verde_rect)
            bloqueado = not mundos_desbloqueio["mundo_planeta"]["desbloqueado"] 
            if bloqueado: 
                x3, y3 = mundo_verde_rect.center
                val3 = fonte_moeda.render("1000", True, (255, 255, 0))
                alt_val3 = val3.get_height()  
                larg_val3 = val3.get_width()  
                base3 = y3 + 100
                window.blit(val3, (x3- larg_val3//2, base3))
                window.blit(coin_img, (x3+larg_val3//2+5, base3+alt_val3//2-20))  
            window.blit(botao_extra_img, botao_extra_rect)

    # Mundo Mina (sempre desbloqueado)
        window.blit(mundo1_img, mundo1_rect)
        # Exibe mensagem de erro por 2 segundos na tela de seleção de mundos
        if mensagem_mundo and pygame.time.get_ticks() - tempo_mensagem < 2000:
            fonte_mensagem = pygame.font.SysFont(None, 36)
            texto_mensagem = fonte_mensagem.render(mensagem_mundo, True, (200, 200, 200))
            window.blit(texto_mensagem, ((WIDTH - texto_mensagem.get_width()) // 2, HEIGHT - 60))



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
        window.blit(coin_img, (10, 10))
        window.blit(menu_tam, menu_rect)
        window.blit(fim_img, ((WIDTH//2) -250, 100))
        moed_t = pygame.font.SysFont(None, 36).render(str(moedas_totais), True, (255, 255, 0))
        window.blit(moed_t, (60, 15))
        window.blit(moed_t, (60, 15))  # Moedas totais 

    elif tela == "menu_extra":
        window.blit(background_jogo, (0, 0))  # Fundo da tela de mundos

        # Título
        fonte_titulo = pygame.font.SysFont(None, 48)
        texto = fonte_titulo.render("POWER UPS", True, (255, 255, 255))
        window.blit(texto, (WIDTH // 2 - texto.get_width() // 2, 80))

        # Botões com imagens distintas
        window.blit(botao1_img, botao1_rect)
        window.blit(botao2_img, botao2_rect)
        window.blit(botao3_img, botao3_rect)

        # Instrução de retorno
        sub = pygame.font.SysFont(None, 24).render("Pressione ESC para voltar", True, (180, 180, 180))
        window.blit(sub, (WIDTH // 2 - sub.get_width() // 2, HEIGHT - 40))
                

    pygame.display.update()

pygame.quit()