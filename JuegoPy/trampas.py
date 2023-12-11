import pygame, random
from constantes import*

def cargar_imagenes():
	lista = []
	for i in range(10):
		imagen = pygame.image.load(r"PROGRAMACION 1\JuegoPy\recursos1\meteorGrey{0}.png".format(i+1)).convert()
		lista.append(imagen)
	return lista
class Meteoro(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(cargar_imagenes())
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(ANCHO_PANTALLA - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > ALTO_PANTALLA + 10 or self.rect.left < -25 or self.rect.right > ANCHO_PANTALLA + 22 :
			self.rect.x = random.randrange(ANCHO_PANTALLA - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedy = random.randrange(1, 8)
	
	