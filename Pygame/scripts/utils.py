import pygame

BASE_IMG_PATH = 'PROGRAMACION 1\Pygame\imgs'

def cargar_img(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0,0,0))
    return img
    