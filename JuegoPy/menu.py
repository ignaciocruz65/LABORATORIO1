import pygame
import sys
import re
from basedatos import *
from constantes import*
from auxiliar import*
from pygame.sprite import Group
from pygame import mixer


pygame.init()
mixer.init()
mixer.music.set_volume(0.5)
def reproducir_melodia(ruta):
    pygame.mixer.init()
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.play(-1)  # Reproducir la melodía en bucle infinito
    
def leer_archivo_json():
    with open("PROGRAMACION 1\JuegoPy\datos_juego.json", 'r') as archivo:
        datos = json.load(archivo)
        return datos
def obtener_suma_por_diccionario():
    suma_por_diccionario = []  
    lista = leer_archivo_json()
    for diccionario in lista:
        suma = sum(diccionario.values())
        suma_por_diccionario.append(suma)
    return suma_por_diccionario
def ordenar_lista_mayor_a_menor():
    lista = obtener_suma_por_diccionario()
    lista_ordenada = sorted(lista, reverse=True)
    return lista_ordenada


class Menu():
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
        self.lista_imagenes = []
        self.lista_opciones = []
        self.sprite_fondo = pygame.image.load(r"PROGRAMACION 1\JuegoPy\menuu\espaciomenu.jpg").convert()
        self.sprite_conf = pygame.image.load(r"PROGRAMACION 1\JuegoPy\menuu\espacioconfig.png").convert()
        self.sprite_score = pygame.image.load(r"PROGRAMACION 1\JuegoPy\menuu\fondoconfig.jpg").convert()
        self.imagen_score = pygame.transform.scale(self.sprite_score,(ANCHO_PANTALLA,ALTO_PANTALLA))
        self.imagen_menu = pygame.transform.scale(self.sprite_fondo,(ANCHO_PANTALLA,ALTO_PANTALLA))
        self.imagen_menu_conf = pygame.transform.scale(self.sprite_conf,(ANCHO_PANTALLA,ALTO_PANTALLA))
        self.menu_principal = True
        self.menu_setting = False
        # self.menu_levels = False
        self.menu_score = False
        self.volumen = 0.2
        self.vol = False
        self.grupo_botones = Group()
        self.grupo_botones_conf = Group()
        self.grupo_botones_levels = Group()
        self.grupo_botones_score = Group()
        self.press_cambiar_img  = 0
        self.nombre_ingresado = ''
    def dibujar_score(self):
        lista = ordenar_lista_mayor_a_menor()
        y = 250
        if len(lista) < 10:
            for indice in range(len(lista)):
                texto_formateado = "{0}         {1}".format(str(indice + 1), str(lista[indice]))
                dibujar_texto(texto_formateado,WHITE,self.screen,ANCHO_PANTALLA//2 - 60,y,30)
                y += 35
    def dibujar_top5(self):
        # Obtener los mejores 5 puntajes
        with sqlite3.connect('PROGRAMACION 1/JuegoPy/jugadores.db') as conexion:
            consulta_top5 = '''
                SELECT nombre, score FROM Jugadores2 ORDER BY score DESC LIMIT 5
            '''
            cursor = conexion.execute(consulta_top5)
            mejores_puntuaciones = cursor.fetchall()

        # Mostrar en la pantalla
        y = 250
        for i, (nombre, score) in enumerate(mejores_puntuaciones, start=1):
            texto = f'{i}. {nombre}: {score}'
            dibujar_texto(texto, WHITE, self.screen, ANCHO_PANTALLA // 2, y, 30)
            y += 40

    def manejar_evento_texto(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                self.nombre_ingresado = self.nombre_ingresado[:-1]
            elif evento.key == pygame.K_RETURN:
                if self.nombre_ingresado == '':
                    print('El nombre no puede estar vacío.')
                if not self.nombre_ingresado.isalnum():
                    print('El nombre solo puede contener letras y números.')
            else:
                self.nombre_ingresado += evento.unicode

    def manejar_evento_mouse(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.menu_setting:
            for boton in self.grupo_botones_conf:

                if boton.rect.collidepoint(mouse_pos):
                    play_soud("PROGRAMACION 1\JuegoPy\sonido\DOORPNUM.WAV",self.volumen)
                    if boton == self.flecha_baja:
                        if self.press_cambiar_img > 0:
                            print("menos")
                            if self.press_cambiar_img == 0:
                                self.volumen = 0
                            else:
                                self.press_cambiar_img -= 1
                                self.volumen -= 0.5 / 7
                        self.barra_vol = Boton(r"PROGRAMACION 1\JuegoPy\menu\vol_{0}.png".format(self.press_cambiar_img), 205, ALTO_PANTALLA - self.y)
                    elif boton == self.flecha_sube:
                        if self.press_cambiar_img < 6:
                            # if self.pre
                            self.volumen += 0.5/ 7
                            self.press_cambiar_img += 1
                        self.barra_vol = Boton(r"PROGRAMACION 1\JuegoPy\menu\vol_{0}.png".format(self.press_cambiar_img), 205, ALTO_PANTALLA - self.y)
                    elif boton == self.boton_retornar_setting:
                        self.menu_principal = True
                        self.menu_setting = False
        # self.menu_principal
        elif self.menu_principal: 
            for boton in self.grupo_botones:
                if boton.rect.collidepoint(mouse_pos):
                    play_soud("PROGRAMACION 1\JuegoPy\sonido\DOORPNUM.WAV",self.volumen)
                    if boton == self.boton_start:
                        if (self.nombre_ingresado.isalnum()):
                            self.menu_principal = False
                            self.menu_setting = False
                            self.vol = True
                            from game import Game
                            self.game = Game()
                            self.game.nombre = self.nombre_ingresado
                            self.game.ejecutar()
                            pygame.quit()
                            sys.exit()
                        else:
                            print('ingrese un nombre valido para iniciar')
                    elif boton == self.boton_config:
                        self.menu_setting = True
                        self.menu_principal = False
                    elif boton == self.boton_exit:
                        self.menu_principal = False
                        self.menu_setting = False
                        # self.menu_levels = False
                        self.menu_score = False
                    elif boton == self.boton_score:
                        self.menu_score = True
                        self.menu_principal = False
                        self.menu_setting = False
        elif self.menu_score:
            for boton in self.grupo_botones_score:
                if boton.rect.collidepoint(mouse_pos):
                    play_soud("PROGRAMACION 1\JuegoPy\sonido\DOORPNUM.WAV",self.volumen)
                    if boton == self.boton_retornar_score:
                        self.menu_principal = True
                        self.menu_score = False

    def menu_inicio(self):
        pygame.font.init()
        screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA)) 
        clock = pygame.time.Clock()

        # pantalla principal config
        self.boton_start = Boton("PROGRAMACION 1\JuegoPy\menuu\startt.png", ANCHO_PANTALLA // 2- 150, ALTO_PANTALLA // 2 + 110)
        self.boton_exit = Boton(r"PROGRAMACION 1\JuegoPy\menuu\quit.png", ANCHO_PANTALLA // 2+ 150, ALTO_PANTALLA // 2 + 110)
        self.boton_config = Boton("PROGRAMACION 1\JuegoPy\menuu\engranaje2.png",ANCHO_PANTALLA // 2 - 2 ,ALTO_PANTALLA//2 + 100,(100,100))
        self.boton_score = Boton("PROGRAMACION 1\JuegoPy\menuu\scores.png", ANCHO_PANTALLA // 2 - 10 ,ALTO_PANTALLA // 2 + 200,(150,60))
        self.grupo_botones.add(self.boton_start, self.boton_exit,self.boton_config,self.boton_score)
        if self.vol:
            play_soud(r"PROGRAMACION 1\JuegoPy\recursos1\music.ogg",self.volumen)

        # pantalla setting config
        self.y = 150
        self.flecha_sube = Boton(r"PROGRAMACION 1\JuegoPy\menuu\suibir.png", 310, ALTO_PANTALLA - self.y)
        self.flecha_baja = Boton(r"PROGRAMACION 1\JuegoPy\menuu\bajar.png",  100, ALTO_PANTALLA - self.y)
        self.boton_retornar_setting = Boton(r"PROGRAMACION 1\JuegoPy\menuu\back.png", ANCHO_PANTALLA / 2, ALTO_PANTALLA / 2- 80)
        self.grupo_botones_conf.add(self.flecha_sube, self.flecha_baja,self.boton_retornar_setting)
        self.barra_vol = Boton(rf"PROGRAMACION 1\JuegoPy\menu\vol_{self.press_cambiar_img}.png",  205 , ALTO_PANTALLA - self.y)
        # menu score config
        self.boton_retornar_score = Boton(r"PROGRAMACION 1\JuegoPy\menuu\back.png",ANCHO_PANTALLA / 2 , ALTO_PANTALLA  - 100)
        self.grupo_botones_score.add(self.boton_retornar_score)
        # menu levels config
        self.boton_retornar_levels = Boton(r"PROGRAMACION 1\JuegoPy\menuu\back.png",ANCHO_PANTALLA / 2, ALTO_PANTALLA - 100)
        self.grupo_botones_levels.add(self.boton_retornar_levels)
        while self.menu_principal or self.menu_setting or self.menu_score:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if self.menu_principal:
                        self.menu_principal = False
                        self.menu_score = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.manejar_evento_mouse()       
                
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    self.manejar_evento_texto(event) # Manejar el evento de ingreso de texto
            if self.menu_principal:
                
                screen.blit(self.imagen_menu, (0, 0))
                self.grupo_botones.draw(screen)
                dibujar_texto("Aliens vs Humanos", WHITE, screen, 600, 100, 80)
                rectangulo_nombre = pygame.Rect(ANCHO_PANTALLA // 2 - 105, ALTO_PANTALLA // 2, 200, 30)
                pygame.draw.rect(screen, WHITE, rectangulo_nombre)
                fuente = pygame.font.Font(None, 20)
                texto_superficie = fuente.render((self.nombre_ingresado), True, BLACK)
                texto_rect = texto_superficie.get_rect(center=rectangulo_nombre.center)
                screen.blit(texto_superficie, texto_rect)
            elif self.menu_setting:
                self.grupo_botones_conf.add(self.barra_vol)
                screen.blit(self.imagen_menu_conf, (0, 0))
                dibujar_texto("VOLUMEN", MORA, screen, 200, 400, 40)
                dibujar_texto("CONFIGURACION", WHITE, screen, 600, 90, 100)
                self.grupo_botones_conf.draw(screen)
            elif self.menu_score:
                screen.blit(self.imagen_score,(0,0))
                dibujar_texto("Puntuaciones", WHITE, screen, 600, 40, 100)
                self.dibujar_top5()
                self.grupo_botones_score.draw(screen)
            delta_ms = clock.tick(FPS)
            pygame.display.flip()
        

        pygame.quit() # Fin
    

if __name__ == "__main__":
    menu = Menu()
    menu.menu_inicio()
