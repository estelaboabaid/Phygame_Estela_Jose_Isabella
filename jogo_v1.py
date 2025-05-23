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
button_image = pygame.transform.scale(button_image, (350, 100))

#imagem do coracao 
heart_img = pygame.image.load(os.path.join(caminho_img, 'heart_red.png')).convert_alpha()
heart_img = pygame.transform.scale(heart_img, (40, 40))

#imagem do coracao quebrado 
heart_broken_img = pygame.image.load(os.path.join(caminho_img, 'heart_broken.png')).convert_alpha()
heart_broken_img = pygame.transform.scale(heart_broken_img, (40, 40))

# Picareta 
picareta = pygame.image.load(os.path.join(caminho_img, 'picareta_animacao.png')).convert_alpha()  # Faz com que a picareta tenha as dimensões certas para a animação

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
botao1_img = pygame.image.load(os.path.join(caminho_img, 'picareta_Imã.png')).convert_alpha()
botao1_img = pygame.transform.scale(botao1_img, (150, 180))

botao2_img = pygame.image.load(os.path.join(caminho_img, 'picareta_tempo.png')).convert_alpha()
botao2_img = pygame.transform.scale(botao2_img, (150, 180))

botao3_img = pygame.image.load(os.path.join(caminho_img, 'picareta_gelo.png')).convert_alpha()
botao3_img = pygame.transform.scale(botao3_img, (150, 180))

# Valores de exemplo para os botões do menu extra
custos_powerups = {
    "botao1": 300,
    "botao2": 200,
    "botao3": 150
}

upgrades_comprados = {
    "botao1": False,
    "botao2": False,
    "botao3": False
}

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
botao1_rect = botao1_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
botao2_rect = botao2_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))
botao3_rect = botao3_img.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))

#botao info 
botao_info = pygame.image.load(os.path.join(caminho_img, 'info.png')).convert_alpha()
botao_info = pygame.transform.scale(botao_info, (250, 150))
info_rect = botao_info.get_rect(center=(WIDTH // 2, HEIGHT // 2 +250))


#dicionario com os custos dos mundos, e define eles como bloqueados, sendo apenas desbloqueados quando o jogador compra
mundos_desbloqueio = {
    "mundo_planeta": {"custo": 250, "desbloqueado": False},
    "mundo_mistico": {"custo": 500, "desbloqueado": False},
    "mundo_verde": {"custo": 1000, "desbloqueado": False}
}

#variaveis para o controle de tela 
sequencia_info = False
indice_tela_info = 0
tempo_tela_info = 0
total_telas_info = 17

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
foto7 = pygame.image.load(os.path.join(caminho_img, 'foto7.png')).convert_alpha()
foto7 = pygame.transform.scale(foto7, (WIDTH, HEIGHT))
foto8 = pygame.image.load(os.path.join(caminho_img, 'foto8.png')).convert_alpha()
foto8 = pygame.transform.scale(foto8, (WIDTH, HEIGHT))
foto9 = pygame.image.load(os.path.join(caminho_img, 'foto9.png')).convert_alpha()
foto9 = pygame.transform.scale(foto9, (WIDTH, HEIGHT))
foto10 = pygame.image.load(os.path.join(caminho_img, 'foto10.png')).convert_alpha()
foto10 = pygame.transform.scale(foto10, (WIDTH, HEIGHT))
foto11 = pygame.image.load(os.path.join(caminho_img, 'foto11.png')).convert_alpha()
foto11 = pygame.transform.scale(foto11, (WIDTH, HEIGHT))
foto12 = pygame.image.load(os.path.join(caminho_img, 'foto12.png')).convert_alpha()
foto12 = pygame.transform.scale(foto12, (WIDTH, HEIGHT))
foto13 = pygame.image.load(os.path.join(caminho_img, 'foto13.png')).convert_alpha()
foto13 = pygame.transform.scale(foto13, (WIDTH, HEIGHT))
foto14 = pygame.image.load(os.path.join(caminho_img, 'foto14.png')).convert_alpha()
foto14 = pygame.transform.scale(foto14, (WIDTH, HEIGHT))
foto15 = pygame.image.load(os.path.join(caminho_img, 'foto15.png')).convert_alpha()
foto15 = pygame.transform.scale(foto15, (WIDTH, HEIGHT))
foto16 = pygame.image.load(os.path.join(caminho_img, 'foto16.png')).convert_alpha()
foto16 = pygame.transform.scale(foto16, (WIDTH, HEIGHT))
foto17 = pygame.image.load(os.path.join(caminho_img, 'foto17.png')).convert_alpha()
foto17 = pygame.transform.scale(foto17, (WIDTH, HEIGHT))
fotos_info = [foto1, foto2, foto3, foto4, foto5, foto6, foto7, foto8, foto9, foto10, foto11, foto12, foto13, foto14, foto15, foto16, foto17]


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
            if congelamento_ativo:
                return  # nada se move enquanto congelado
            velocidade_x = self.speedx
            velocidade_y = self.speedy
            if camera_lenta_ativa:
                velocidade_x *= 0.3  # reduz para 30%
                velocidade_y *= 0.3

            self.rect.x += velocidade_x
            self.rect.y += velocidade_y

            # Atração ao cursor se ativa
            if atracao_ativa and self.tipo in ["azul", "vermelho", "verde", "laranja", "roxo"]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dx = mouse_x - self.rect.centerx
                dy = mouse_y - self.rect.centery
                self.rect.x += int(dx * 0.05)
                self.rect.y += int(dy * 0.05)

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

# Inicia uma classe para a animação da picareta
class Machado(pygame.sprite.Sprite):
    def __init__(self, x, y, img_picareta):  # Recebe os comandos do tamanho da picareta
        super().__init__()
        self.image = img_picareta
        self.animacao = False
        self.frame_atual = 0
        tamanho = (110, 110)  
        self.frames = [pygame.transform.scale(pygame.image.load(os.path.join(caminho_img, "ax1.png")).convert_alpha(), tamanho),                  
    pygame.transform.scale(pygame.image.load(os.path.join(caminho_img, "ax2.png")).convert_alpha(), tamanho)]
        self.rect = self.frames[0].get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        
    def iniciar_animacao(self):  # Define como True para iniciar a animação
        self.animacao = True

    def update(self):  # Parte muda a animação de acordo com o que esta no loop
        if self.animacao:
            self.frame_atual = 1
        else:
            self.frame_atual = 0
        
        self.rect.center = pygame.mouse.get_pos()
        self.image = self.frames[self.frame_atual]

game = True
tela = "inicio"
clock = pygame.time.Clock()
FPS = 30

diamantes = pygame.sprite.Group()
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 600)  # Fala de quanto em quanto tempo o diamante ira aparecer

vidas = [True, True, True]  # define as vidas como verdadeiras, que mostra que o jogador tem vidas
pontuacao = 0  # inicia a pontuação como 0
moedas_totais = 0  # Total acumulado entre rodadas
fase_atual = "padrao" # Fase padrão, para evitar erro de referência antes de selecionar um mundo

#POWER UPS 
atracao_ativa = False
upgrade_imã_ativado = False  # novo controle de ativação do botão

#TEMPO ATRACAO E STATUS 
atracao_duracao = 5000  # 5 segundos em milissegundos
tempo_atracao_ativada = 0
vezes_usadas_atracao = 0
vezes_maximas = 3

#CAMERA LENTA E STATUS
upgrade_camera_lenta_ativado = False
camera_lenta_ativa = False
tempo_camera_lenta_ativada = 0
vezes_usadas_camera_lenta = 0
vezes_maximas_camera_lenta = 3

#CONGELAMENTO DE TELA E STATUS
upgrade_congelamento_ativado = False
congelamento_ativo = False
tempo_congelamento_ativado = 0
vezes_usadas_congelamento = 0
vezes_maximas_congelamento = 3


mensagem_mundo = ""
tempo_mensagem = 0

machado_sprite = Machado(100, 500, picareta)
grupo_sprites = pygame.sprite.Group()
grupo_sprites.add(machado_sprite)

# Loop principal
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
                        vezes_usadas_atracao = 0
                        vezes_usadas_camera_lenta = 0
                        vezes_usadas_congelamento = 0


    
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
                        vezes_usadas_atracao = 0
                        vezes_usadas_camera_lenta = 0
                        vezes_usadas_congelamento = 0


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
                        vezes_usadas_atracao = 0
                        vezes_usadas_camera_lenta = 0
                        vezes_usadas_congelamento = 0

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
                    vezes_usadas_atracao = 0
                    vezes_usadas_camera_lenta = 0
                    vezes_usadas_congelamento = 0



                elif botao_extra_rect.collidepoint(event.pos):
                    tela = "menu_extra"
                    
        elif tela == "jogo":
            if event.type == SPAWN_EVENT:
                if not congelamento_ativo:
                    diamantes.add(Diamante())
            # Detecção contínua de clique com o mouse sobre diamantes
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if upgrade_imã_ativado and vezes_usadas_atracao < vezes_maximas:
                        atracao_ativa = True
                        tempo_atracao_ativada = pygame.time.get_ticks()
                        vezes_usadas_atracao += 1
                    elif upgrade_camera_lenta_ativado and vezes_usadas_camera_lenta < vezes_maximas_camera_lenta:
                        camera_lenta_ativa = True
                        tempo_camera_lenta_ativada = pygame.time.get_ticks()
                        vezes_usadas_camera_lenta += 1
                    elif upgrade_congelamento_ativado and vezes_usadas_congelamento < vezes_maximas_congelamento:
                        congelamento_ativo = True
                        tempo_congelamento_ativado = pygame.time.get_ticks()
                        vezes_usadas_congelamento += 1

        
        # Traz o resultado do evento de clique do mouse, para a animação
        if event.type == pygame.MOUSEBUTTONDOWN:
            machado_sprite.animacao = True

        if event.type == pygame.MOUSEBUTTONUP:
            machado_sprite.animacao = False
                


        if tela == "jogo" and pygame.mouse.get_pressed()[0]:  # Evento do botão esquerdo do mouse eo que acontece
            machado_sprite.rect.center = pygame.mouse.get_pos()
            mouse_pos = pygame.mouse.get_pos()
            grupo_sprites.draw(window)
            grupo_sprites.update()

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
                            moedas_totais += pontuacao
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
                    vezes_usadas_atracao = 0
                    vezes_usadas_camera_lenta = 0
                    vezes_usadas_congelamento = 0

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
                    if not upgrades_comprados["botao1"]:
                        if moedas_totais >= custos_powerups["botao1"]:
                            moedas_totais -= custos_powerups["botao1"]
                            upgrades_comprados["botao1"] = True
                            upgrade_imã_ativado = True
                            upgrade_camera_lenta_ativado = False
                            upgrade_congelamento_ativado = False
                            print("UPGRADE IMÃ COMPRADO E ATIVADO!")
                        else:
                            print("Moedas insuficientes para comprar o IMÃ.")
                    else:
                        upgrade_imã_ativado = not upgrade_imã_ativado
                        upgrade_camera_lenta_ativado = False
                        upgrade_congelamento_ativado = False
                        print(f"UPGRADE IMÃ {'ATIVADO' if upgrade_imã_ativado else 'DESATIVADO'}")

                elif botao2_rect.collidepoint(event.pos):
                    if not upgrades_comprados["botao2"]:
                        if moedas_totais >= custos_powerups["botao2"]:
                            moedas_totais -= custos_powerups["botao2"]
                            upgrades_comprados["botao2"] = True
                            upgrade_camera_lenta_ativado = True
                            upgrade_imã_ativado = False
                            upgrade_congelamento_ativado = False
                            print("CÂMERA LENTA COMPRADA E ATIVADA!")
                        else:
                            print("Moedas insuficientes para comprar CÂMERA LENTA.")
                    else:
                        upgrade_camera_lenta_ativado = not upgrade_camera_lenta_ativado
                        upgrade_imã_ativado = False
                        upgrade_congelamento_ativado = False
                        print(f"CÂMERA LENTA {'ATIVADA' if upgrade_camera_lenta_ativado else 'DESATIVADA'}")

                elif botao3_rect.collidepoint(event.pos):
                    if not upgrades_comprados["botao3"]:
                        if moedas_totais >= custos_powerups["botao3"]:
                            moedas_totais -= custos_powerups["botao3"]
                            upgrades_comprados["botao3"] = True
                            upgrade_congelamento_ativado = True
                            upgrade_imã_ativado = False
                            upgrade_camera_lenta_ativado = False
                            print("CONGELAMENTO COMPRADO E ATIVADO!")
                        else:
                            print("Moedas insuficientes para comprar CONGELAMENTO.")
                    else:
                        upgrade_congelamento_ativado = not upgrade_congelamento_ativado
                        upgrade_imã_ativado = False
                        upgrade_camera_lenta_ativado = False
                        print(f"CONGELAMENTO {'ATIVADO' if upgrade_congelamento_ativado else 'DESATIVADO'}")




    if tela == "info": #tela atual de informacoes 
            window.blit(fotos_info[indice_tela_info], (0, 0)) #desenha a imagem na posicao 0,0

            #define o tempo de exibicao dependendo da imagem 
            if indice_tela_info >= total_telas_info -2: #se tiver nas duas ultimas imagens 
                tempo_exibicao = 2000 #o tempo é de 2 segundo 
            else: #no resto das imagens 
                tempo_exibicao = 200# otempo de exibicao é 0.2 segundos 

            #verifica se ja passou o tempo necessario pra trocar de imagem
            if pygame.time.get_ticks() - tempo_tela_info >= tempo_exibicao:
                indice_tela_info += 1#passa pra proxima imagem
                tempo_tela_info = pygame.time.get_ticks()#atualiza o tempo de referencia para a proxima troca de imagem
                if indice_tela_info >= total_telas_info: #se ja mostrou todas as imagens
                    sequencia_info = False #termina a sequencia das fotos de informacao 
                    tela = "inicio" #volta parar a tela inicial 
            

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
        #Sinaliza ativação Ima
        if atracao_ativa:
            overlay_azul = pygame.Surface((WIDTH, HEIGHT))
            overlay_azul.set_alpha(50)
            overlay_azul.fill((0, 0, 255))
            window.blit(overlay_azul, (0, 0))

            overlay_vermelho = pygame.Surface((WIDTH, HEIGHT))
            overlay_vermelho.set_alpha(50)
            overlay_vermelho.fill((255, 0, 0))
            window.blit(overlay_vermelho, (0, 0))
        #Sinaliza ativação camera lenta
        if camera_lenta_ativa:
            overlay_azul = pygame.Surface((WIDTH, HEIGHT))
            overlay_azul.set_alpha(80)
            overlay_azul.fill((0, 0, 180))
            window.blit(overlay_azul, (0, 0))
        
        #Sinaliza ativação do congelamento
        if congelamento_ativo:
            overlay_verde = pygame.Surface((WIDTH, HEIGHT))
            overlay_verde.set_alpha(80)
            overlay_verde.fill((0, 180, 0))
            window.blit(overlay_verde, (0, 0))


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
        grupo_sprites.update()
        # Desativa atração se passou o tempo
        if atracao_ativa and pygame.time.get_ticks() - tempo_atracao_ativada > atracao_duracao:
            atracao_ativa = False
        # Desativa câmera lenta se passou o tempo
        if camera_lenta_ativa and pygame.time.get_ticks() - tempo_camera_lenta_ativada > 5000:
            camera_lenta_ativa = False
        # Desativa congelamento se passou o tempo
        if congelamento_ativo and pygame.time.get_ticks() - tempo_congelamento_ativado > 4000:
            congelamento_ativo = False


        machado_sprite.rect.center = pygame.mouse.get_pos()
        window.blit(machado_sprite.image, machado_sprite.rect)


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
        window.blit(texto, (WIDTH // 2 - texto.get_width() // 2 , 90))

        # Botões com imagens distintas
        window.blit(botao1_img, botao1_rect)
        window.blit(botao2_img, botao2_rect)
        window.blit(botao3_img, botao3_rect)

            # Fonte para o custo
        fonte_custo = pygame.font.SysFont(None, 32)

        # Botão 1
        valor1 = fonte_custo.render(str(custos_powerups["botao1"]), True, (255, 255, 0))
        x1 = botao1_rect.right + 10
        y1 = botao1_rect.centery - valor1.get_height() // 2
        window.blit(valor1, (x1 - 30, y1 + 30))
        window.blit(coin_img, (x1 + valor1.get_width() + 5 - 30 , y1 + 20))

        # Botão 2
        valor2 = fonte_custo.render(str(custos_powerups["botao2"]), True, (255, 255, 0))
        x2 = botao2_rect.right + 10
        y2 = botao2_rect.centery - valor2.get_height() // 2
        window.blit(valor2, (x2 - 30, y2 + 30))
        window.blit(coin_img, (x2 + valor2.get_width() + 5 - 30, y2 + 20))

        # Botão 3
        valor3 = fonte_custo.render(str(custos_powerups["botao3"]), True, (255, 255, 0))
        x3 = botao3_rect.right + 10
        y3 = botao3_rect.centery - valor3.get_height() // 2
        window.blit(valor3, (x3 - 30, y3 + 30))
        window.blit(coin_img, (x3 + valor3.get_width() + 5 - 30, y3 + 20))


        # Instrução de retorno
        sub = pygame.font.SysFont(None, 24).render("Pressione ESC para voltar", True, (180, 180, 180))
        window.blit(sub, (WIDTH // 2 - sub.get_width() // 2, HEIGHT - 40))
                

    pygame.display.update()

pygame.quit()