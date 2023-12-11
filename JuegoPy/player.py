import pygame
from constantes import*
from balas import Bullet
from vida import*
# from bala_doble import Bullets
class Player(pygame.sprite.Sprite):
    def __init__(self,grupo_sprites,bullets):
        super().__init__()
        self.grupo_sprites = grupo_sprites
        self.bullets = bullets
        self.imagen = pygame.image.load(r"PROGRAMACION 1\JuegoPy\general\nave.png")#.convert()
        self.imagen.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.imagen,(97,75))
        self.rect = self.image.get_rect()
        self.imagen_bala = r"PROGRAMACION 1\JuegoPy\general\projectile.png"
        self.imagen_dobble_bala = r"PROGRAMACION 1\JuegoPy\general\projectiledoble.png"
        self.imagen_fuego = r"PROGRAMACION 1\JuegoPy\recursos\fuego.png"
        self.rect.centerx = ANCHO_PANTALLA // 2
        self.rect.bottom = ALTO_PANTALLA - 10
        self.speed_x = 0
        self.shield = 100
        # self.vidas = vidas
    def update(self):
        # vida = Vida()
        # print(len(vida.lista_vidas))
        # if self.vidas <= 0:
        #     self.kill()
        #     self.rect = pygame.Rect(0,0,0,0)
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        self.rect.x += self.speed_x
        if self.rect.right > ANCHO_PANTALLA:
            self.rect.right = ANCHO_PANTALLA
        if self.rect.left < 0:
            self.rect.left = 0
        
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top,self.imagen_bala)
        self.grupo_sprites.add(bullet)
        self.bullets.add(bullet)

    def double_shoot(self):
        serparcion_balas = 43
        centra_bala_cañon = 23
        bullet1 = Bullet(self.rect.centerx - serparcion_balas, self.rect.top + centra_bala_cañon,self.imagen_dobble_bala)  # Primera bala
        bullet2 = Bullet(self.rect.centerx + serparcion_balas, self.rect.top + centra_bala_cañon,self.imagen_dobble_bala)  # Segunda bala
        self.grupo_sprites.add(bullet1, bullet2)
        self.bullets.add(bullet1, bullet2)

    def shoot_fire_bol(self):
        bullet = Bullet(self.rect.centerx, self.rect.top - 120 ,self.imagen_fuego)
        self.grupo_sprites.add(bullet)
        self.bullets.add(bullet)
