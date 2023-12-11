import pygame,json
from constantes import*



def dibujar_sprite_estatico(ruta,superficie,pos_x,pos_y,x,y):
    imagen = pygame.image.load(ruta) 
    imagen = pygame.transform.scale(imagen,(x,y))
    rect_imagen = imagen.get_rect()
    rect_imagen.topleft = (pos_x, pos_y)  # Establecer las coordenadas de ubicación
    superficie.blit(imagen,rect_imagen)

def dibujar_texto(texto, color, superficie, pos_x, pos_y, tamaño):
    pygame.font.init()
    fuente_texto = r"c:\USERS\NACHO\APPDATA\LOCAL\MICROSOFT\WINDOWS\FONTS\Starborn.TTF"
    fuente = pygame.font.Font(fuente_texto, tamaño)
    texto_renderizado = fuente.render(texto, True, color)
    rect_texto = texto_renderizado.get_rect()
    rect_texto.centerx = pos_x  # Centrar horizontalmente
    rect_texto.y = pos_y  # Alinear en la parte superior
    superficie.blit(texto_renderizado, rect_texto)
    return rect_texto

def play_soud(ruta,volumen):
        # pygame.mixer.init()
        sonido = pygame.mixer.Sound(ruta)
        sonido.set_volume(volumen)
        sonido.play()

# from pathlib import Path
# import json

    
# # datos = GuardarDatos(100,200,300)
from pathlib import Path
# import json

class GuardarDatos():
    def __init__(self, dato1, dato2, dato3):
        self.datos_juego = {"nivel1": dato1, "nivel2": dato2, "nivel3": dato3}
        self.guardar_datos_juego()

    def cargar_datos_juego(self):
        archivo = Path('datos_juego.json')
        if archivo.is_file():
            with archivo.open('r') as archivo_json:
                datos_guardados = json.load(archivo_json)
        else:
            datos_guardados = []
        return datos_guardados

    def guardar_datos_juego(self):
        lista_datos = self.cargar_datos_juego()
        lista_datos.append(self.datos_juego)
        archivo = Path('datos_juego.json')
        with archivo.open('w') as archivo_json:
            json.dump(lista_datos, archivo_json,indent=2)
            archivo_json.write('\n') 
# datos = GuardarDatos(100, 200, 300)

class Boton(pygame.sprite.Sprite):
    def __init__(self, imagen, x, y,size=None):
        super().__init__()
        self.image = pygame.image.load(imagen).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        if size is not None:
            self.image = pygame.transform.scale(self.image, size)