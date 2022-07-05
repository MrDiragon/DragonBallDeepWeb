import random
import pygame

pygame.init()  # iniciando o pygame
pygame.mixer.init()  # iniciando o som do game

LARGURA = 1280
ALTURA = 720

# nome do game
TITULO_DO_GAME = 'DRAGON BALL: DEEP WEB'

# fps do game
FPS = 90

som_fundo = pygame.mixer.music.load("audios/dragon ball GT abertura Português de Portugal.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)


class Game:
    def __init__(self):
        # tela do game
        pygame.init()  # iniciando o pygame
        pygame.mixer.init()  # iniciando o som do game
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))  # tamanho da tela
        pygame.display.set_caption(TITULO_DO_GAME)  # titulo do game
        self.fps = pygame.time.Clock()  # fps do game
        self.rondando_game = True  # status do game
        self.x = 0

    def rodar(self):
        # loop do game
        self.jogando = True
        while self.jogando:
            self.fps.tick(FPS)  # fps do game
            self.eventos()  # eventos dentro do game, movimentos
            self.background()
            self.movi_background()
            player.desenhar_player()
            inimigo.desenhar_inimigo()
            tiro.desenhar_tiro()
            esfera.desenhar_esfera()
            self.movi_tiro()
            player.movimentacao()
            tiro.atirar()
            tiro.respawn_tiro()
            tiro.colisao_tiro_tela()
            inimigo.respawn()
            inimigo.respawn_inimigo()
            inimigo.respawn_inimigo_two()
            esfera.respawn_esfera()
            player.alinhar_img_player()
            inimigo.alinhar_img_inimigo()
            tiro.alinhar_img_tiro()
            esfera.alinhar_img_esfera()
            tiro.score_pontos()
            player.vida()
            pygame.display.update()

    def eventos(self):
        # loop dos eventos do game, e parada do game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.rondando_game = False

    def movi_tiro(self):
        if tiro.triggered == True:
            tiro.pos_x_tiro += 10
        if tiro.pos_x_tiro == 1300:
            tiro.triggered = False

    def background(self):
        self.chamar_bg = pygame.image.load('imagens/mapa2.jpg').convert_alpha()
        self.bg = pygame.transform.scale(self.chamar_bg, (LARGURA, ALTURA))
        self.tela.blit(self.bg, (0, 0))

    def movi_background(self):
        rel_x = self.x % self.bg.get_rect().width
        self.tela.blit(self.bg, (rel_x - self.bg.get_rect().width, 0))  # loop Background
        if rel_x < 1280:
            self.tela.blit(self.bg, (rel_x, 0))

        self.x -= 10

    def tela_de_start(self):
        pass

    def tela_de_game_over(self):
        pass


class Inimigo:
    def __init__(self):
        self.pos_inimigo_x = 500
        self.pos_inimigo_y = 360
        self.pos_inimigo_xz = 500
        self.pos_inimigo_yz = 360
        self.inimigo_chamada = pygame.image.load('imagens/freza.png').convert_alpha()
        self.inimigo = pygame.transform.scale(self.inimigo_chamada, (100, 100))  # convertendo tamanho do inimigo
        self.inimigo_two_chamada = pygame.image.load('imagens/buu.png').convert_alpha()
        self.inimigo_two = pygame.transform.scale(self.inimigo_two_chamada, (100, 100))
        self.inimigo_rect = self.inimigo.get_rect()
        self.inimigo_two_rect = self.inimigo_two.get_rect()
        self.pontos = 0

    def desenhar_inimigo(self):
        game.tela.blit(self.inimigo, (self.pos_inimigo_x, self.pos_inimigo_y))
        game.tela.blit(self.inimigo_two, (self.pos_inimigo_xz, self.pos_inimigo_yz))

    def respawn(self):
        self.x = 1350
        self.y = random.randint(1, 640)
        return [self.x, self.y]

    def respawn_two(self):
        self.x = 1350
        self.y = random.randint(1, 640)
        return [self.x, self.y]

    def respawn_inimigo(self):
        if self.pos_inimigo_x == 50  or self.colisao():
            self.pos_inimigo_x = inimigo.respawn()[0]
            self.pos_inimigo_y = inimigo.respawn()[1]
        self.pos_inimigo_x -= 4

    def respawn_inimigo_two(self):
        if self.pos_inimigo_xz == 50 or self.colisao_two():
            self.pos_inimigo_xz = inimigo.respawn_two()[0]
            self.pos_inimigo_yz = inimigo.respawn_two()[1]
        self.pos_inimigo_xz -= 5

    def alinhar_img_inimigo(self):
        self.inimigo_rect.y = self.pos_inimigo_y
        self.inimigo_rect.x = self.pos_inimigo_x
        self.inimigo_two_rect.y = self.pos_inimigo_yz
        self.inimigo_two_rect.x = self.pos_inimigo_xz
        pygame.draw.rect(player.Screen, (255, 0, 0), self.inimigo_rect, 4)
        pygame.draw.rect(player.Screen, (255, 0, 0), self.inimigo_two_rect, 4)

    def colisao(self):
        if player.player_rect.colliderect(self.inimigo_rect) or self.inimigo_rect.x == 60:
            audios.som_colisao.play()
            player.vidas -= 1
            if player.vidas == 0:
                game.jogando = False
                game.rondando_game = False
            return True
        elif tiro.tiro_rect.colliderect(self.inimigo_rect):
            self.pontos += 1
            return True
        else:
            return False

    def colisao_two(self):
        if player.player_rect.colliderect(self.inimigo_two_rect) or self.inimigo_two_rect.x == 60:
            audios.som_colisao.play()
            player.vidas -= 1
            if player.vidas == 0:
                game.jogando = False
                game.rondando_game = False
            return True
        if tiro.tiro_rect.colliderect(self.inimigo_two_rect):
            self.pontos += 1
            return True
        else:
            return False


class Player:
    def __init__(self):
        self.pos_player_x = 200
        self.pos_player_y = 300
        self.playerImg_chamada = pygame.image.load('imagens/goku.png').convert_alpha()
        self.playerImg = pygame.transform.scale(self.playerImg_chamada,(100, 100))  # convertendo o tamanho do personagem
        self.player_rect = self.playerImg.get_rect()
        self.Screen = pygame.display.set_mode((LARGURA, ALTURA))
        self.vidas = 7

    def desenhar_player(self):
        game.tela.blit(self.playerImg, (self.pos_player_x, self.pos_player_y))

    def movimentacao(self):
        self.tecla = pygame.key.get_pressed()

        if self.tecla[pygame.K_UP] and self.pos_player_y > 1:
            self.pos_player_y -= 8
            if not tiro.triggered:  # se botao de tiro n tiver apertado o tiro fica na mao
                tiro.pos_y_tiro -= 8
        if self.tecla[pygame.K_DOWN] and self.pos_player_y < 665:
            self.pos_player_y += 8
            if not tiro.triggered:
                tiro.pos_y_tiro += 8

    def alinhar_img_player(self):
        self.player_rect.y = self.pos_player_y
        self.player_rect.x = self.pos_player_x
        pygame.draw.rect(self.Screen, (255, 0, 0), self.player_rect, 4)

    def vida(self):
        self.placar_vida = tiro.font.render(f'Vidas: {int(self.vidas)} ', True, (0,0,0))
        self.Screen.blit(self.placar_vida,(400,50))


class Tiro:
    def __init__(self):
        self.triggered = False
        self.vel_x_tiro = 0
        self.pos_x_tiro = 200
        self.pos_y_tiro = 310
        self.tiro_chamada = pygame.image.load('imagens/tiro.png').convert_alpha()
        self.tiro = pygame.transform.scale(self.tiro_chamada, (30, 30))
        self.tiro_rect = self.tiro.get_rect()
        self.font = pygame.font.SysFont('arial',50)

    def desenhar_tiro(self):
        game.tela.blit(self.tiro, (self.pos_x_tiro, self.pos_y_tiro))

    def respawn_tiro(self):
        self.respawn_tiro_x = player.pos_player_x
        self.respawn_tiro_y = player.pos_player_y
        self.vel_x_tiro = 0
        return [self.respawn_tiro_x, self.respawn_tiro_y, self.triggered, self.vel_x_tiro]

    def atirar(self):
        player.tecla = pygame.key.get_pressed()

        if player.tecla[pygame.K_SPACE]:
            audios.som_tiro.play()
            self.triggered = True
            self.vel_x_tiro = 0

    def colisao_tiro_tela(self):
        if self.pos_x_tiro == 1300:
            self.pos_x_tiro, self.pos_y_tiro, self.triggered, self.vel_x_tiro = tiro.respawn_tiro()

    def alinhar_img_tiro(self):
        self.tiro_rect.y = self.pos_y_tiro
        self.tiro_rect.x = self.pos_x_tiro
        pygame.draw.rect(player.Screen, (255, 0, 0), self.tiro_rect, 4)

    def score_pontos(self):
        self.score = self.font.render(f'Pontos: {int(inimigo.pontos)} ', True, (0,0,0))
        player.Screen.blit(self.score,(50,50))


class Esfera:
    def __init__(self):
        self.pos_esfera_x = 500
        self.pos_esfera_y = 360
        self.esfera_chamada = pygame.image.load('imagens/Dragon_ball.svg.png').convert_alpha()
        self.esfera_png = pygame.transform.scale(self.esfera_chamada, (35, 35))  # convertendo tamanho do inimigo
        self.esfera_rect = self.esfera_png.get_rect()

    def desenhar_esfera(self):
        game.tela.blit(self.esfera_png, (self.pos_esfera_x, self.pos_esfera_y))

    def respawn1(self):
        self.x = 3000
        self.y = random.randint(1, 640)
        return [self.x, self.y]

    def respawn_esfera(self):
        if self.colisao_esfera():
            self.pos_esfera_x = self.respawn1()[0]
            self.pos_esfera_y = self.respawn1()[1]
        self.pos_esfera_x -= 5

    def alinhar_img_esfera(self):
        self.esfera_rect.y = self.pos_esfera_y
        self.esfera_rect.x = self.pos_esfera_x
        pygame.draw.rect(player.Screen, (255, 0, 0), self.esfera_rect, 4)

    def colisao_esfera(self):
        if player.player_rect.colliderect(self.esfera_rect):
            player.vidas += 1
            return True
        else:
            return False


class Audios:
    def __init__(self):
        self.som_tiro = pygame.mixer.Sound("audios/punch.mp3")
        self.som_tiro.set_volume(0.09)

        self.som_colisao = pygame.mixer.Sound("audios/hit.mp3")
        self.som_colisao.set_volume(0.8)


game = Game()
inimigo = Inimigo()
player = Player()
tiro = Tiro()
esfera = Esfera()
audios = Audios()

while game.rondando_game:
    game.rodar()