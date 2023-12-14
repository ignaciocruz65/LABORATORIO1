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


def devolverNombre(lista:list):
    lista_limpia = re.sub(r'[^a-zA-Z ]', '', lista)
    return lista_limpia.strip()

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

    def manejar_evento_texto(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                self.nombre_ingresado = self.nombre_ingresado[:-1]
            else:
                self.nombre_ingresado += evento.unicode

    # def actualizar_nombre(self):
    #     return nombre_ingresado
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
                        self.menu_principal = False
                        self.menu_setting = False
                        self.vol = True
                        import pygame,sys
                        from trampas import Meteoro
                        from trampa2 import Asteroide
                        from explocion import Explosion
                        from vida import Vida
                        from player import Player
                        from items import Item
                        from enemigo import Enemigo,Enemigo_dos
                        from balas import Bullet
                        from item_bala import Item_doble
                        from item_fuego import Item_fuego
                        from pygame.sprite import Group
                        from retorno import Return
                        from nivel_dos import Nivel2
                        from menu import Menu
                        import re

                        pygame.init()
                        pygame.mixer.init()
                        class Game:
                            
                            def __init__(self):

                                self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
                                self.sonido_disparo = None
                                self.grupo_sprites = Group()
                                self.grupo_meteoros = Group()
                                self.grupo_asteroide = Group()
                                self.grupo_bullets = Group()
                                self.grupo_items_vida = Group()
                                self.grupo_items_doble = Group()
                                self.grupo_items_fuego = Group()
                                self.grupo_blas_enemigo = Group()
                                self.grupo_botones_game_over = Group()
                                self.grupo_botones_pause = Group()
                                self.grupo_enemigos = Group()
                                self.vida = Vida()
                                self.choco = False
                                self.vida.vida_player()
                                self.cambiar_bala_doble = False
                                self.cambiar_bala_fuego = False
                                self.cambiar_bala_simple = True
                                self.paused = False
                                self.running = True
                                self.running_over = True
                                self.mostrar_texto = False
                                self.game_over = False
                                self.escudo = 10
                                self.tiempo_inicial = 0
                                self.tiempo_inicio = 0
                                self.tiempo_mostrando_texto = 600 
                                self.tiempo_transcurrido = 0
                                self.score_general = 0
                                self.datos_score = []
                                self.reloj = pygame.time.Clock()
                                self.imagen_fondo = pygame.image.load(r"C:\Users\Nacho\Desktop\Nueva carpeta\vsc\PROGRAMACION 1\JuegoPy\imgs_nivel1\city_lvl1.jpg").convert()
                                self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (ANCHO_PANTALLA, ALTO_PANTALLA))
                                self.generar_sprites()
                                menu = Menu()
                                self.menu_instancia = menu
                                self.nombre = self.menu_instancia.nombre_ingresado
                                
                                # self.actualizar_nombre()
                            
                            # def actualizar_nombre(self):
                            #     self.nombre = self.menu_instancia.actualizar_nombre()
                            def generar_sprites(self):
                                self.player = Player(self.grupo_sprites,self.grupo_bullets)
                                self.enemigo = Enemigo(self.grupo_sprites,self.grupo_blas_enemigo,r"PROGRAMACION 1\JuegoPy\enemigos\nave_alien2.png",r"PROGRAMACION 1\JuegoPy\enemigos\laser_alien2.png",97,75,120)
                                # grupo_enemigos = pygame.sprite.Group()
                                self.enemigo1 = Enemigo_dos(self.grupo_sprites,self.grupo_blas_enemigo,1,-150,200)
                                self.enemigo2 = Enemigo_dos(self.grupo_sprites,self.grupo_blas_enemigo,2,-150,200)
                                self.enemigo3 = Enemigo_dos(self.grupo_sprites,self.grupo_blas_enemigo,3,ANCHO_PANTALLA + 150,200)
                                self.enemigo4 = Enemigo_dos(self.grupo_sprites,self.grupo_blas_enemigo,4,ANCHO_PANTALLA + 150,200)


                                # self.grupo_sprites.add(self.enemigo1)
                                self.grupo_sprites.add(self.enemigo1,self.enemigo2,self.enemigo3,self.enemigo4)
                                self.grupo_enemigos.add(self.enemigo1,self.enemigo2,self.enemigo3,self.enemigo4)
                                self.grupo_sprites.add(self.player)
                                
                                for i in range(3):
                                    asteriode = Asteroide()
                                    self.grupo_sprites.add(asteriode) 
                                    self.grupo_asteroide.add(asteriode)
                                for i in range(1):
                                    item = Item()
                                    self.grupo_sprites.add(item) 
                                    self.grupo_items_vida.add(item)
                                for i in range(1):
                                    item_doble_bala = Item_doble()
                                    self.grupo_sprites.add(item_doble_bala) 
                                    self.grupo_items_doble.add(item_doble_bala)
                                # for i in range(1):
                                #     item_fuego = Item_fuego()
                                #     self.grupo_sprites.add(item_fuego)
                                #     self.grupo_items_fuego.add(item_fuego)

                            def play_soud(self,ruta):
                                self.sonido_disparo = pygame.mixer.Sound(ruta)
                                self.sonido_disparo.play()
                                self.volumen = VOLUMEN
                                self.sonido_disparo.set_volume(self.volumen)


                                with open("score1.json", 'w') as archivo:
                                    json.dump(self.score_general, archivo)
                                    # archivo.write(',')

                            def colicion_item_vida_player(self):
                                choques = pygame.sprite.spritecollide(self.player,self.grupo_items_vida,True)
                                for choque in choques:
                                    item_vida = Item()
                                    self.grupo_sprites.add(item_vida)
                                    self.grupo_items_vida.add(item_vida)   
                                    self.vida.aumentar_vida(True)
                                    self.play_soud("PROGRAMACION 1\JuegoPy\sonido\BLIP.WAV")
                                self.vida.dibujar_vidas(self.pantalla,"nada")

                            def choque_item_doble_player(self):
                                choco = False
                                choques = pygame.sprite.spritecollide(self.player,self.grupo_items_doble,True)
                                for choque in choques:
                                    item_doble_bala = Item_doble()
                                    self.grupo_sprites.add(item_doble_bala)
                                    self.grupo_items_doble.add(item_doble_bala)
                                    self.cambiar_bala_doble = True
                                    self.cambiar_bala_fuego = False
                                    self.cambiar_bala_simple = False
                                    self.choco = True

                            def choque_item_fuego_player(self):
                                choques = pygame.sprite.spritecollide(self.player,self.grupo_items_fuego,True)
                                for choque in choques:
                                    item_fuego = Item_fuego()
                                    self.grupo_sprites.add(item_fuego)
                                    self.grupo_items_fuego.add(item_fuego)
                                    self.cambiar_bala_fuego = True
                                    self.cambiar_bala_simple = False
                                    self.cambiar_bala_doble = False

                            #colicion balas con asteriodes
                            def colision_balas_asteroides(self):
                                hits = pygame.sprite.groupcollide(self.grupo_asteroide, self.grupo_bullets, True, True)
                                for hit in hits:
                                    self.play_soud("PROGRAMACION 1\JuegoPy\sonido\BANGLRG.WAV")
                                    explocion = Explosion(hit.rect.center)
                                    self.grupo_sprites.add(explocion)

                                    asteriode = Asteroide()
                                    self.grupo_sprites.add(asteriode)
                                    self.grupo_asteroide.add(asteriode) 
                                    self.score_general += 15
                        #colicion jugador con asteriode
                            def colision_jugador_asteroide(self):
                                hits = pygame.sprite.spritecollide(self.player, self.grupo_asteroide, True)
                                for hit in hits:
                                    explocion = Explosion(hit.rect.center)
                                    self.grupo_sprites.add(explocion)
                                    asteriode = Asteroide()
                                    self.grupo_sprites.add(asteriode)
                                    self.grupo_asteroide.add(asteriode)
                                    self.escudo -= 5
                                    if self.escudo <= 0:
                                        self.vida.eliminar_vidas(True)
                            # def control_pausa_gameover(self):
                            #     if len(self.vida.lista_vidas) == 0:
                            #         self.game_over = True
                            #         self.running = False
                                    

                            # colision laser item
                            def colision_laser_item(self):
                                hits = pygame.sprite.groupcollide(self.grupo_items_vida, self.grupo_bullets, True, True)
                                for hit in hits:
                                    item = Item()
                                    self.grupo_sprites.add(item)
                                    self.grupo_items_vida.add(item)
                                    self.vida.eliminar_vidas(True)
                                    self.tiempo_inicial = pygame.time.get_ticks()
                                    if self.enemigo.vida > 0:
                                        self.enemigo.vida += 10
                                        self.mostrar_texto = True   
                                if self.mostrar_texto and pygame.time.get_ticks() - self.tiempo_inicial <= self.tiempo_mostrando_texto:   
                                    font = pygame.font.Font(None, 30)
                                    text = font.render("+10", True, (255, 255, 255))
                                    text_rect = text.get_rect(center=(self.pantalla.get_width() // 2, self.pantalla.get_height() // 2))
                                    self.pantalla.blit(text, text_rect)
                                else:   
                                    self.mostrar_texto = False

                            def colision_laser_enemigo_dos(self):
                                for enemigo in self.grupo_enemigos:
                                    impactos = pygame.sprite.spritecollide(enemigo,self.grupo_bullets,True)
                                    for impacto in impactos:
                                        self.play_soud("PROGRAMACION 1\JuegoPy\sonido\BANGHUGE.WAV")
                                        if enemigo == self.enemigo1:  
                                            self.enemigo1.vida -= 5
                                        elif enemigo == self.enemigo2:
                                            self.enemigo2.vida -= 5
                                        elif enemigo == self.enemigo3:
                                            self.enemigo3.vida -= 5
                                        elif enemigo == self.enemigo4:
                                            self.enemigo4.vida -= 5
                                        if self.enemigo1.vida <= 0 and self.enemigo2.vida <= 0 and self.enemigo3.vida <= 0 and self.enemigo4.vida <= 0:
                                            self.enemigo1.vida = 0
                                            self.enemigo2.vida = 0
                                            self.enemigo3.vida = 0
                                            self.enemigo4.vida = 0
                                        if self.cambiar_bala_doble:
                                            punto_explocion = (impacto.rect.center[0],impacto.rect.center[1]-20)
                                        if self.cambiar_bala_simple:
                                            punto_explocion = (impacto.rect.center[0],impacto.rect.center[1]-20) 
                                        if self.cambiar_bala_fuego:
                                            punto_explocion = (impacto.rect.center[0],impacto.rect.center[1]-100)
                                        explocion = Explosion(punto_explocion)
                                        self.grupo_sprites.add(explocion)
                                        self.score_general += 20
                                
                            # colicion laserjugador con enemigo
                            def colision_laser_enemigo(self):
                                daños = pygame.sprite.spritecollide(self.enemigo,self.grupo_bullets,True)
                                for daño in daños:
                                    self.play_soud("PROGRAMACION 1\JuegoPy\sonido\BANGHUGE.WAV")
                                    self.enemigo.vida -= 10
                                    if self.enemigo.vida <= 0: #se verifica que sea menor o igual que cero y se establece para que cumpla la condicion
                                        self.enemigo.vida = 0
                                    if self.cambiar_bala_doble:
                                        punto_explocion = (daño.rect.center[0],daño.rect.center[1]-20)
                                    if self.cambiar_bala_simple:
                                        punto_explocion = (daño.rect.center[0],daño.rect.center[1]-20) 
                                    if self.cambiar_bala_fuego:
                                        punto_explocion = (daño.rect.center[0],daño.rect.center[1]-100)
                                    explocion = Explosion(punto_explocion)
                                    self.grupo_sprites.add(explocion)
                                    self.score_general += 20
                            def colision_laser_player(self):
                                impactos = pygame.sprite.spritecollide(self.player,self.grupo_blas_enemigo,True)
                                for impacto in impactos:
                                    self.play_soud("PROGRAMACION 1\JuegoPy\sonido\BANGLRG.WAV")
                                    explocion = Explosion(impacto.rect.center)
                                    self.grupo_sprites.add(explocion)
                                    self.escudo -= 10
                                    if self.escudo <= 0:
                                        self.vida.eliminar_vidas(True)

                            def puntuacion_draw(self):
                                dibujar_texto("SCORE:",WHITE,self.pantalla,ANCHO_PANTALLA-150,70,25)
                                dibujar_texto(str(self.score_general),RED,self.pantalla,ANCHO_PANTALLA-60,70,25)
                                # dibujar_texto(str(len(self.vida.lista_vidas)),RED,self.pantalla,ANCHO_PANTALLA-60,70,25)

                            def evento_mouse(self):
                                mouse_pos = pygame.mouse.get_pos()
                                if self.game_over :
                                    for boton1 in self.grupo_botones_game_over:
                                        if boton1.rect.collidepoint(mouse_pos) :
                                            play_soud("PROGRAMACION 1\JuegoPy\sonido\DOORPNUM.WAV",self.volumen)
                                            if boton1 == self.boton_menu:
                                                print("menu")
                                                pass
                                            elif boton1 == self.boton_star:
                                                
                                                # self.running_over = False 
                                                self.running = True
                                                # self.game_over = False
                                                print(f"{self.running}   {self.game_over}")
                                                self.ejecutar()


                                                # self.game_over = False
                                                pass
                                elif self.paused:
                                    for boton in self.grupo_botones_pause:
                                        if boton.rect.collidepoint(mouse_pos) :
                                            play_soud("PROGRAMACION 1\JuegoPy\sonido\DOORPNUM.WAV",0.2)
                                            if boton == self.boton_menu:
                                                pass
                            def escudo_player(self):
                                ancho_barra = 100
                                alto_barra = 17
                                x = 10
                                y = 80
                                fill = (self.escudo / 100) * ancho_barra
                                border = pygame.Rect(x, y, ancho_barra, alto_barra)
                                fill = pygame.Rect(x, y, fill, alto_barra)
                                pygame.draw.rect(self.pantalla, RED, fill)
                                pygame.draw.rect(self.pantalla, WHITE, border, 2)
                                dibujar_texto("ESCUDO",WHITE,self.pantalla,60,50,20)
                            def control_tiempo(self):
                                self.tiempo_actual = pygame.time.get_ticks()
                                self.tiempo_transcurrido = self.tiempo_actual - self.tiempo_inicio
                                segundos = (self.tiempo_transcurrido // 1000) % 60
                                dibujar_texto(f"TIEMPO: {segundos}",WHITE,self.pantalla,ANCHO_PANTALLA-100,20,20)
                            def ejecutar(self):       
                            # game over conf
                                self.boton_menu = Boton("PROGRAMACION 1\JuegoPy\menuu\menu.png",ANCHO_PANTALLA // 2 ,ALTO_PANTALLA // 2 + 40)
                                self.boton_star = Boton("PROGRAMACION 1\JuegoPy\menuu\startt.png",ANCHO_PANTALLA // 2 ,ALTO_PANTALLA // 2 + 100)
                                self.tiempo_inicio = pygame.time.get_ticks()
                                self.tiempo_game_over = 0
                                self.tiempo_mision_ok = 0
                                #     print(self.tiempo_nivel)
                                print("nivel 1")
                                while self.running_over:
                                    # self.flag_control = 
                                    # print(f"{self.running}{self.game_over}")
                                    for evento in pygame.event.get():
                                        if evento.type == pygame.QUIT:
                                            # self.guradar_datos_game()  
                                            # print(self.game_over)
                                            # self.datos.append(self.score)
                                            # self.running = False
                                            pygame.quit()
                                            sys.exit()
                                        elif evento.type == pygame.KEYDOWN:
                                            if evento.key == pygame.K_SPACE:    
                                                if self.cambiar_bala_doble:
                                                    self.player.double_shoot()
                                                if self.cambiar_bala_simple:
                                                    self.player.shoot()  
                                                if self.cambiar_bala_fuego:
                                                    self.player.shoot_fire_bol()
                                                self.play_soud("PROGRAMACION 1\JuegoPy\sonido\RIFLE.WAV")
                                            if evento.key == pygame.K_RETURN:
                                                self.paused = not self.paused
                                            # if evento.key == pygame.K_ESCAPE:
                                            #     # self.running = False
                                            #     # pygame.quit()
                                            #     # sys.exit()
                                            #     self.cambiar_nivel()
                                            #     print("ok")
                                        if evento.type == pygame.MOUSEBUTTONDOWN:
                                            self.evento_mouse()
                                    # self.control_pausa_gameover()
                                    self.control_tiempo()
                                    # print(self.tiempo_transcurrido,"     ",self.tiempo_game_over)
                                    # print(self.tiempo_nivel)
                                    if self.enemigo.vida > 0:
                                        self.tiempo_mision_ok = self.tiempo_transcurrido + 6000

                                    if len(self.vida.lista_vidas) > 0:
                                        self.tiempo_game_over = self.tiempo_transcurrido + 6000
                                        

                                    # if not self.paused :
                                    if self.running:
                                        print(self.nombre)
                                        
                                        # print(self.enemigo1.vida,self.enemigo2.vida,self.enemigo3.vida,self.enemigo4.vida)
                                        self.pantalla.blit(self.imagen_fondo, (0, 0))
                                        if self.tiempo_transcurrido > 1000:
                                            self.grupo_sprites.update()
                                            self.grupo_sprites.draw(self.pantalla)
                                        if self.enemigo1.vida == 0 and self.enemigo2.vida == 0 and self.enemigo3.vida == 0 and self.enemigo4.vida == 0:
                                            # print("Segundo enemigo")
                                            self.grupo_sprites.add(self.enemigo)
                                        if self.enemigo.vida == 0: #Tiene que estar en == 0 
                                            dibujar_texto("Mision Completada",WHITE,self.pantalla,ANCHO_PANTALLA//2,ALTO_PANTALLA//2.5,90)
                                            if self.tiempo_transcurrido >= self.tiempo_mision_ok:                
                                                crear_y_cargar_datos(self.nombre,self.score_general)
                                                # self.guardar = GuardarDatos(self.score_general,0,0)
                                                
                                                import pygame,sys,random
                                                from explocion import Explosion
                                                from retorno import Return
                                                from nivel_tres import NivelTres


                                                class Bomba(pygame.sprite.Sprite):
                                                    def __init__(self):
                                                        super().__init__()
                                                        self.image = pygame.image.load(r"PROGRAMACION 1\JuegoPy\imgs_nivel2\projectilealien.png")
                                                        self.rect = self.image.get_rect()
                                                        self.velocidad = 2 #Velocidad de minialiens
                                                        # Establecer la posición inicial en los laterales, arriba o abajo
                                                        self.posicion_inicial()

                                                    def posicion_inicial(self):
                                                        lado = random.choice(["izquierda", "derecha", "arriba", "abajo"])

                                                        if lado == "izquierda":
                                                            self.rect.left = 0
                                                            self.rect.centery = random.randint(0, ALTO_PANTALLA)
                                                        elif lado == "derecha":
                                                            self.rect.right = ANCHO_PANTALLA
                                                            self.rect.centery = random.randint(0, ALTO_PANTALLA)
                                                        elif lado == "arriba":
                                                            self.rect.top = 0
                                                            self.rect.centerx = random.randint(0, ANCHO_PANTALLA)
                                                        elif lado == "abajo":
                                                            self.rect.bottom = ALTO_PANTALLA
                                                            self.rect.centerx = random.randint(0, ANCHO_PANTALLA)

                                                    def update(self):
                                                        objetivo_x = ANCHO_PANTALLA // 2
                                                        objetivo_y = ALTO_PANTALLA // 2

                                                        dx = objetivo_x - self.rect.centerx
                                                        dy = objetivo_y - self.rect.centery -50

                                                        distancia = abs(dx) + abs(dy)
                                                        velocidad_x = dx / distancia * self.velocidad
                                                        velocidad_y = dy / distancia * self.velocidad

                                                        self.rect.x += velocidad_x
                                                        self.rect.y += velocidad_y
                                                class Planeta(pygame.sprite.Sprite):
                                                    def __init__(self):
                                                        super().__init__()
                                                        self.image = pygame.image.load(r"PROGRAMACION 1\JuegoPy\imgs_nivel2\planetatierra.png")
                                                        self.image = pygame.transform.scale(self.image,(90,90))
                                                        self.rect = self.image.get_rect()
                                                        self.rect.center = (ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2 - 50)
                                                class Mira(pygame.sprite.Sprite):
                                                    def __init__(self, ) -> None:
                                                        super().__init__()
                                                        self.image = pygame.image.load(r"PROGRAMACION 1\JuegoPy\imgs_nivel2\mira.png")
                                                        # imagen.set_colorkey(BLACK)
                                                        self.image = pygame.transform.scale(self.image,(100,100))
                                                        self.rect = self.image.get_rect()
                                                        self.rect.topleft = (ANCHO_PANTALLA / 2,ALTO_PANTALLA - 110)

                                                    def update(self):
                                                        # Actualizar la posición del sprite según la posición del mouse
                                                        self.rect.center = pygame.mouse.get_pos()
                                                class Punto(pygame.sprite.Sprite):
                                                    def __init__(self, ) -> None:
                                                        super().__init__()
                                                        self.image = pygame.image.load(r"PROGRAMACION 1\JuegoPy\recursos\proyectil.png")
                                                        # imagen.set_colorkey(BLACK)
                                                        self.image = pygame.transform.scale(self.image,(6,3))
                                                        self.rect = self.image.get_rect()
                                                        self.rect.topleft = (ANCHO_PANTALLA / 2,ALTO_PANTALLA - 110)

                                                    def update(self):
                                                        # Actualizar la posición del sprite según la posición del mouse
                                                        self.rect.center = pygame.mouse.get_pos()
                                                class Nivel2():
                                                    def __init__(self) -> None:
                                                        pass  
                                                        pygame.init()
                                                        pygame.mixer.init()
                                                        self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
                                                        self.reloj = pygame.time.Clock()
                                                        self.grupo_sprite = pygame.sprite.Group()
                                                        self.grupo_bombas = pygame.sprite.Group()
                                                        # mira = pygame.sprite.Group()
                                                        self.tierra = Planeta()
                                                        self.grupo_sprite.add(self.tierra)
                                                        self.vida_tierra = 200
                                                        self.mira = Mira()
                                                        self.grupo_sprite.add(self.mira)
                                                        self.punto = Punto()
                                                        self.grupo_sprite.add(self.punto)
                                                        self.tiempo_transcurrido_game = 0
                                                        self.tiempo_transcurrido_nivel = 0
                                                        self.tiempo_inicio_game = 0
                                                        self.score = 0
                                                        self.running = True
                                                        for i in range(10):
                                                            bomba = Bomba()
                                                            self.grupo_bombas.add(bomba)
                                                            self.grupo_sprite.add(bomba)
                                                            
                                                        
                                                            # ">-------------Eres un valiente astronauta encargado de proteger la Tierra de la inminente destrucción----------------<\n" \
                                                            # ">-------Tu misión es destruir los asteroides dirigidos por el enemigo antes de que impacten en nuestro planeta------<\n" \
                                                            # "> ¡Apunta con precisión y destruye tantos asteroides como puedas en un tiempo determinado para salvar la Tierra! <\n" \
                                                            # ">-----------------------------------------------¡Buena suerte, astronauta!----------------------------------------------------<"
                                                        self.texto = \
                                                            ">---------------------------------Eres un humano valiente la verdad.------------------------------------<\n" \
                                                            ">--------La victoria todavia no esta en tus manos, debes defender los ataques alienigenas-----<\n" \
                                                            ">Es momento de probar tu punteria, debes destruir los misiles en el menor tiempo posible-<\n" \
                                                            ">----------------------------------------------¡GLHF!---------------------------------------------------<"
                                                    def puntuacion_draw(self):
                                                        dibujar_texto("PUNTUACION:",WHITE,self.pantalla,ANCHO_PANTALLA-180,70,25)
                                                        dibujar_texto(str(self.score),RED,self.pantalla,ANCHO_PANTALLA-40,70,25)
                                                        # dibujar_texto(str(len(self.vida.lista_vidas)),ORANGE,self.pantalla,ANCHO_PANTALLA-100,130,20)
                                                        # colicion mira bomba
                                                    def colicion_mira_bomba(self):
                                                        impactos = pygame.sprite.spritecollide(self.punto,self.grupo_bombas,True)
                                                        for impacto in impactos:
                                                            punto_explocion = (impacto.rect.center)
                                                            explocion = Explosion(punto_explocion)
                                                            self.grupo_sprite.add(explocion)
                                                            self.grupo_sprite.add(explocion)
                                                            bomba = Bomba()
                                                            self.grupo_bombas.add(bomba)
                                                            self.grupo_sprite.add(bomba)
                                                            self.score += 15
                                                            play_soud("PROGRAMACION 1\JuegoPy\sonido\BANGMED.WAV",0.2)
                                                        play_soud(r"PROGRAMACION 1\JuegoPy\recursos1\laser5.ogg",0.2)

                                                    def colision_bomba_tierra(self):
                                                        hits = pygame.sprite.spritecollide(self.tierra,self.grupo_bombas, True)
                                                        for hit in hits:
                                                            punto_explocion = (hit.rect.center[0]+20,hit.rect.center[1]-20)

                                                            explocion = Explosion(punto_explocion)
                                                            self.grupo_sprite.add(explocion)
                                                            bomba = Bomba()
                                                            self.grupo_bombas.add(bomba)
                                                            self.grupo_sprite.add(bomba) 
                                                            self.vida_tierra -= 20
                                                            # print("colision")
                                                    def escudo_tierra(self):
                                                        ancho_barra = 200
                                                        alto_barra = 17
                                                        x = 10
                                                        y = 40
                                                        # print(vida)
                                                        fill = (self.vida_tierra / 200) * ancho_barra
                                                        border = pygame.Rect(x, y, ancho_barra, alto_barra)
                                                        fill = pygame.Rect(x, y, fill, alto_barra)
                                                        pygame.draw.rect(self.pantalla, RED, fill)
                                                        pygame.draw.rect(self.pantalla, WHITE, border, 2)
                                                        dibujar_texto("TIERRA",WHITE,self.pantalla,60,10,20)    
                                                    def play_soud(ruta):
                                                            sonido_disparo = pygame.mixer.Sound(ruta)
                                                            sonido_disparo.play()
                                                            volumen = VOLUMEN
                                                            sonido_disparo.set_volume(volumen)
                                                    def control_tiempo_game(self,orden,y):
                                                        self.tiempo_actual = pygame.time.get_ticks()
                                                        self.tiempo_transcurrido = self.tiempo_actual - self.tiempo_inicio_game - 1000
                                                        segundos = (self.tiempo_transcurrido // 1000) % 60
                                                        if orden:
                                                            dibujar_texto("TIEMPO:",RED,self.pantalla,ANCHO_PANTALLA-110,y,20)
                                                            dibujar_texto(f"{segundos}",RED,self.pantalla,ANCHO_PANTALLA-40,y,20)

                                                    def control_tiempo_nivel(self,orden,y):
                                                            tiempo_actual = pygame.time.get_ticks()
                                                            self.tiempo_transcurrido_nivel = tiempo_actual - self.tiempo_inicio_nivel
                                                            segundos = (self.tiempo_transcurrido_nivel // 1000) % 60
                                                            if orden:
                                                                dibujar_texto(f"TIEMPO: {segundos}",RED,self.pantalla,ANCHO_PANTALLA-500,y,20)

                                                    def dibujar_parrafo(self):
                                                        # Dividir el texto en líneas
                                                        lines = self.texto.splitlines()

                                                        # Posición inicial del texto
                                                        x = 10
                                                        y = 290
                                                        for line in lines:
                                                            dibujar_texto(line,WHITE,self.pantalla,600,y,16)
                                                            y += 40

                                                    def leer_archivo_json(self):
                                                        with open("score1.json", 'r') as archivo:
                                                            datos = json.load(archivo)
                                                            return datos
                                                    def guardar_datos(self):
                                                        with open("score2.json", 'w') as archivo:
                                                            json.dump(self.score, archivo)
                                                    
                                                    def nivel_dos(self):
                                                        imagen_fondo = pygame.image.load(r"PROGRAMACION 1\JuegoPy\imgs_nivel2\espaciolvl2.jpg").convert()
                                                        imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_PANTALLA, ALTO_PANTALLA))
                                                        pygame.mouse.set_visible(False)
                                                        self.tiempo_inicio_nivel = pygame.time.get_ticks()
                                                        # if self.tiempo_transcurrido_game > 15000:
                                                        #     print("hola")
                                                        #     self.tiempo_inicio_game = pygame.time.get_ticks()

                                                        while self.running:
                                                            print("nivel 2")
                                                            # print(self.tiempo_transcurrido_game)
                                                            for event in pygame.event.get():
                                                                if event.type == pygame.QUIT:
                                                                    pygame.quit()
                                                                    sys.exit()
                                                                elif event.type == pygame.MOUSEBUTTONDOWN :
                                                                    self.colicion_mira_bomba()
                                                                    print("disparo")
                                                            # print(vida_tierra)
                                                            if self.tiempo_transcurrido_nivel > 0:
                                                                self.pantalla.blit(imagen_fondo,(0,0))
                                                                dibujar_texto("ATAQUE 2",WHITE,self.pantalla,ANCHO_PANTALLA//2,70,130)
                                                                self.dibujar_parrafo()
                                                            if self.tiempo_transcurrido_nivel > 10000:
                                                                self.pantalla.blit(imagen_fondo,(0,0))
                                                                self.escudo_tierra()
                                                                self.grupo_sprite.update()
                                                                self.grupo_sprite.draw(self.pantalla)
                                                                self.colision_bomba_tierra()
                                                                self.puntuacion_draw()
                                                                self.control_tiempo_game(True,30)
                                                            if self.vida_tierra <= 0:
                                                                self.guardar_datos()
                                                                self.guardar = GuardarDatos(self.leer_archivo_json(),self.score,0)
                                                                
                                                                pygame.mouse.set_visible(True)
                                                                dibujar_texto("Perdiste",RED,self.pantalla,ANCHO_PANTALLA//4,ALTO_PANTALLA//4,100)
                                                                
                                                                self.running = False
                                                                retorno = Return()
                                                                retorno.ejecutar()
                                                            if self.tiempo_transcurrido_nivel > 31000:  # en 31000
                                                                self.guardar = GuardarDatos(0,self.score,0)
                                                                print('error 3')
                                                                import pygame,sys
                                                                from menu import Menu
                                                                from trampas import Meteoro
                                                                # from trampa2 import Asteroide
                                                                from explocion import Explosion
                                                                from vida import Vida
                                                                from player import Player
                                                                from items import Item
                                                                from enemigo import Enemigo,Enemigo_dos
                                                                from balas import Bullet
                                                                from item_bala import Item_doble
                                                                from item_fuego import Item_fuego
                                                                from pygame.sprite import Group
                                                                from retorno import Return

                                                                class NivelTres:
                                                                    def __init__(self):
                                                                        pygame.init()
                                                                        pygame.mixer.init()

                                                                        self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
                                                                        self.sonido_disparo = None
                                                                        self.grupo_sprites = Group()
                                                                        self.grupo_meteoros = Group()
                                                                        self.grupo_asteroide = Group()
                                                                        self.grupo_bullets = Group()
                                                                        self.grupo_items_vida = Group()
                                                                        self.grupo_items_doble = Group()
                                                                        self.grupo_items_fuego = Group()
                                                                        self.grupo_blas_enemigo = Group()
                                                                        self.grupo_botones_game_over = Group()
                                                                        self.grupo_botones_pause = Group()
                                                                        self.grupo_enemigos = Group()
                                                                        self.vida = Vida()
                                                                        self.choco = False
                                                                        self.vida.vida_player()
                                                                        self.cambiar_bala_doble = False
                                                                        self.cambiar_bala_fuego = False
                                                                        self.cambiar_bala_simple = True
                                                                        self.paused = False
                                                                        self.running = True
                                                                        self.running_over = True
                                                                        self.mostrar_texto = False
                                                                        self.game_over = False
                                                                        self.escudo = 100
                                                                        self.nombre = ""
                                                                        self.tiempo_inicial = 0
                                                                        self.tiempo_inicio = 0
                                                                        self.tiempo_mostrando_texto = 600 
                                                                        self.tiempo_transcurrido = 0
                                                                        self.score_general = 0
                                                                        self.datos_score = []
                                                                        self.reloj = pygame.time.Clock()
                                                                        self.imagen_fondo = pygame.image.load(r"PROGRAMACION 1\JuegoPy\imgs_nivel3\espaciofinall.jpg").convert()
                                                                        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (ANCHO_PANTALLA, ALTO_PANTALLA))
                                                                        self.generar_sprites()
                                                                        self.texto = \
                                                                        "Felicidades, pero esto aun no termina.\n" \
                                                                        "Debes derrotar a los aliens, y al alien MAYOR.\n" \
                                                                        "Nuestra batalla épica y determinará el destino del planeta tierra.\n" \
                                                                        "Derrotalo y podras cantar victoria finalmente!\n" \


                                                                    def generar_sprites(self):
                                                                        self.player = Player(self.grupo_sprites,self.grupo_bullets)
                                                                        self.enemigo = Enemigo(self.grupo_sprites,self.grupo_blas_enemigo,r"PROGRAMACION 1\JuegoPy\imgs_nivel3\finalboss.png",r"PROGRAMACION 1\JuegoPy\imgs_nivel3\finalbossprojectile.png",180,180,200)
                                                                        # grupo_enemigos = pygame.sprite.Group()
                                                                        self.enemigo1 = Enemigo_dos(self.grupo_sprites,self.grupo_blas_enemigo,1,-150,200)
                                                                        self.enemigo2 = Enemigo_dos(self.grupo_sprites,self.grupo_blas_enemigo,2,-150,200)
                                                                        self.enemigo3 = Enemigo_dos(self.grupo_sprites,self.grupo_blas_enemigo,3,ANCHO_PANTALLA + 150,200)
                                                                        self.enemigo4 = Enemigo_dos(self.grupo_sprites,self.grupo_blas_enemigo,4,ANCHO_PANTALLA + 150,200)
                                                                        self.enemigo5 = Enemigo_dos(self.grupo_sprites,self.grupo_blas_enemigo,1,-150,100)
                                                                        self.enemigo6 = Enemigo_dos(self.grupo_sprites,self.grupo_blas_enemigo,2,-150,100)
                                                                        self.enemigo7 = Enemigo_dos(self.grupo_sprites,self.grupo_blas_enemigo,3,ANCHO_PANTALLA + 150,100)
                                                                        self.enemigo8 = Enemigo_dos(self.grupo_sprites,self.grupo_blas_enemigo,4,ANCHO_PANTALLA + 150,100)


                                                                        # self.grupo_sprites.add(self.enemigo1)
                                                                        self.grupo_sprites.add(self.enemigo1,self.enemigo2,self.enemigo3,self.enemigo4,self.enemigo5,self.enemigo6,self.enemigo7,self.enemigo8)
                                                                        self.grupo_enemigos.add(self.enemigo1,self.enemigo2,self.enemigo3,self.enemigo4,self.enemigo5,self.enemigo6,self.enemigo7,self.enemigo8)
                                                                        self.grupo_sprites.add(self.player)
                                                                    
                                                                        for i in range(5):
                                                                            asteriode = Meteoro()
                                                                            self.grupo_sprites.add(asteriode) 
                                                                            self.grupo_asteroide.add(asteriode)
                                                                        for i in range(1):
                                                                            item = Item()
                                                                            self.grupo_sprites.add(item) 
                                                                            self.grupo_items_vida.add(item)
                                                                        for i in range(1):
                                                                            item_doble_bala = Item_doble()
                                                                            self.grupo_sprites.add(item_doble_bala) 
                                                                            self.grupo_items_doble.add(item_doble_bala)
                                                                        # for i in range(1):
                                                                        #     item_fuego = Item_fuego()
                                                                        #     self.grupo_sprites.add(item_fuego)
                                                                        #     self.grupo_items_fuego.add(item_fuego)

                                                                
                                                                    def play_soud(self,ruta):
                                                                        self.sonido_disparo = pygame.mixer.Sound(ruta)
                                                                        self.sonido_disparo.play()
                                                                        self.volumen = VOLUMEN
                                                                        self.sonido_disparo.set_volume(self.volumen)
                                                                

                                                                    def leer_archivo_json(self,ruta):
                                                                        with open(ruta, 'r') as archivo:
                                                                            datos = json.load(archivo)
                                                                            return datos
                                                                    def guardar_datos(self):
                                                                        with open("score3.json", 'w') as archivo:
                                                                            json.dump(self.score_general, archivo)


                                                                    def colicion_item_vida_player(self):
                                                                        choques = pygame.sprite.spritecollide(self.player,self.grupo_items_vida,True)
                                                                        for choque in choques:
                                                                            item_vida = Item()
                                                                            self.grupo_sprites.add(item_vida)
                                                                            self.grupo_items_vida.add(item_vida)   
                                                                            self.vida.aumentar_vida(True)
                                                                            self.play_soud("PROGRAMACION 1\JuegoPy\sonido\BLIP.WAV")
                                                                        self.vida.dibujar_vidas(self.pantalla,"nada")

                                                                    def choque_item_doble_player(self):
                                                                        choco = False
                                                                        choques = pygame.sprite.spritecollide(self.player,self.grupo_items_doble,True)
                                                                        for choque in choques:
                                                                            item_doble_bala = Item_doble()
                                                                            self.grupo_sprites.add(item_doble_bala)
                                                                            self.grupo_items_doble.add(item_doble_bala)
                                                                            self.cambiar_bala_doble = True
                                                                            self.cambiar_bala_fuego = False
                                                                            self.cambiar_bala_simple = False
                                                                            self.choco = True

                                                                    def choque_item_fuego_player(self):
                                                                        choques = pygame.sprite.spritecollide(self.player,self.grupo_items_fuego,True)
                                                                        for choque in choques:
                                                                            item_fuego = Item_fuego()
                                                                            self.grupo_sprites.add(item_fuego)
                                                                            self.grupo_items_fuego.add(item_fuego)
                                                                            self.cambiar_bala_fuego = True
                                                                            self.cambiar_bala_simple = False
                                                                            self.cambiar_bala_doble = False

                                                                    #colicion balas con asteriodes
                                                                    def colision_balas_asteroides(self):
                                                                        hits = pygame.sprite.groupcollide(self.grupo_asteroide, self.grupo_bullets, True, True)
                                                                        for hit in hits:
                                                                            self.play_soud("PROGRAMACION 1\JuegoPy\sonido\BANGLRG.WAV")
                                                                            explocion = Explosion(hit.rect.center)
                                                                            self.grupo_sprites.add(explocion)

                                                                            asteriode = Meteoro()
                                                                            self.grupo_sprites.add(asteriode)
                                                                            self.grupo_asteroide.add(asteriode) 
                                                                            self.score_general += 15
                                                                #colicion jugador con asteriode
                                                                    def colision_jugador_asteroide(self):
                                                                        hits = pygame.sprite.spritecollide(self.player, self.grupo_asteroide, True)
                                                                        for hit in hits:
                                                                            explocion = Explosion(hit.rect.center)
                                                                            self.grupo_sprites.add(explocion)
                                                                            asteriode = Meteoro()
                                                                            self.grupo_sprites.add(asteriode)
                                                                            self.grupo_asteroide.add(asteriode)
                                                                            self.escudo -= 5
                                                                            if self.escudo <= 0:
                                                                                self.vida.eliminar_vidas(True)
                                                                    # def control_pausa_gameover(self):
                                                                    #     if len(self.vida.lista_vidas) == 0:
                                                                    #         self.game_over = True
                                                                    #         self.running = False
                                                                            

                                                                    # colision laser item
                                                                    def colision_laser_item(self):
                                                                        hits = pygame.sprite.groupcollide(self.grupo_items_vida, self.grupo_bullets, True, True)
                                                                        for hit in hits:
                                                                            item = Item()
                                                                            self.grupo_sprites.add(item)
                                                                            self.grupo_items_vida.add(item)
                                                                            self.vida.eliminar_vidas(True)
                                                                            self.tiempo_inicial = pygame.time.get_ticks()
                                                                            if self.enemigo.vida > 0:
                                                                                self.enemigo.vida += 10
                                                                                self.mostrar_texto = True   
                                                                        if self.mostrar_texto and pygame.time.get_ticks() - self.tiempo_inicial <= self.tiempo_mostrando_texto:   
                                                                            font = pygame.font.Font(None, 30)
                                                                            text = font.render("live enemi +10...", True, (255, 255, 255))
                                                                            text_rect = text.get_rect(center=(self.pantalla.get_width() // 2, self.pantalla.get_height() // 2))
                                                                            self.pantalla.blit(text, text_rect)
                                                                        else:   
                                                                            self.mostrar_texto = False

                                                                    def colision_laser_enemigo_dos(self):
                                                                        for enemigo in self.grupo_enemigos:
                                                                            impactos = pygame.sprite.spritecollide(enemigo,self.grupo_bullets,True)
                                                                            for impacto in impactos:
                                                                                self.play_soud("PROGRAMACION 1\JuegoPy\sonido\BANGHUGE.WAV")
                                                                                if enemigo == self.enemigo1:  
                                                                                    self.enemigo1.vida -= 5
                                                                                elif enemigo == self.enemigo2:
                                                                                    self.enemigo2.vida -= 5
                                                                                elif enemigo == self.enemigo3:
                                                                                    self.enemigo3.vida -= 5
                                                                                elif enemigo == self.enemigo4:
                                                                                    self.enemigo4.vida -= 5
                                                                                elif enemigo == self.enemigo5:  
                                                                                    self.enemigo5.vida -= 5
                                                                                elif enemigo == self.enemigo6:
                                                                                    self.enemigo6.vida -= 5
                                                                                elif enemigo == self.enemigo7:
                                                                                    self.enemigo7.vida -= 5
                                                                                elif enemigo == self.enemigo8:
                                                                                    self.enemigo8.vida -= 5    
                                                                                if self.cambiar_bala_doble:
                                                                                    punto_explocion = (impacto.rect.center[0],impacto.rect.center[1]-20)
                                                                                if self.cambiar_bala_simple:
                                                                                    punto_explocion = (impacto.rect.center[0],impacto.rect.center[1]-20) 
                                                                                if self.cambiar_bala_fuego:
                                                                                    punto_explocion = (impacto.rect.center[0],impacto.rect.center[1]-100)
                                                                                explocion = Explosion(punto_explocion)
                                                                                self.grupo_sprites.add(explocion)
                                                                                self.score_general += 20
                                                                        
                                                                    # colicion laserjugador con enemigo
                                                                    def colision_laser_enemigo(self):
                                                                        daños = pygame.sprite.spritecollide(self.enemigo,self.grupo_bullets,True)
                                                                        for daño in daños:
                                                                            self.play_soud("PROGRAMACION 1\JuegoPy\sonido\BANGHUGE.WAV")
                                                                            self.enemigo.vida -= 10
                                                                            if self.cambiar_bala_doble:
                                                                                punto_explocion = (daño.rect.center[0],daño.rect.center[1]-20)
                                                                            if self.cambiar_bala_simple:
                                                                                punto_explocion = (daño.rect.center[0],daño.rect.center[1]-20) 
                                                                            if self.cambiar_bala_fuego:
                                                                                punto_explocion = (daño.rect.center[0],daño.rect.center[1]-100)
                                                                            explocion = Explosion(punto_explocion)
                                                                            self.grupo_sprites.add(explocion)
                                                                            self.score_general += 20
                                                                    def colision_laser_player(self):
                                                                        impactos = pygame.sprite.spritecollide(self.player,self.grupo_blas_enemigo,True)
                                                                        for impacto in impactos:
                                                                            self.play_soud("PROGRAMACION 1\JuegoPy\sonido\BANGLRG.WAV")
                                                                            explocion = Explosion(impacto.rect.center)
                                                                            self.grupo_sprites.add(explocion)
                                                                            self.escudo -= 10
                                                                            if self.escudo <= 0:
                                                                                self.vida.eliminar_vidas(True)

                                                                    def puntuacion_draw(self):
                                                                        dibujar_texto("SCORE:",WHITE,self.pantalla,ANCHO_PANTALLA-135,70,25)
                                                                        dibujar_texto(str(self.score_general),RED,self.pantalla,ANCHO_PANTALLA-40,70,25)
                                                                        # dibujar_texto(str(len(self.vida.lista_vidas)),ORANGE,self.pantalla,ANCHO_PANTALLA-100,130,20)

                                                                    
                                                                    def dibujar_parrafo(self):
                                                                        # Dividir el texto en líneas
                                                                        lines = self.texto.splitlines()
                                                                        # Posición inicial del texto
                                                                        x = 10
                                                                        y = 290
                                                                        for line in lines:
                                                                            dibujar_texto(line,RED,self.pantalla,600,y,24)
                                                                            y += 40
                                                                    
                                                                    def evento_mouse(self):
                                                                        mouse_pos = pygame.mouse.get_pos()
                                                                        if self.game_over :
                                                                            for boton1 in self.grupo_botones_game_over:
                                                                                if boton1.rect.collidepoint(mouse_pos) :
                                                                                    play_soud("PROGRAMACION 1\JuegoPy\sonido\DOORPNUM.WAV",self.volumen)
                                                                                    if boton1 == self.boton_menu:
                                                                                        print("menu")
                                                                                        pass
                                                                                    elif boton1 == self.boton_star:
                                                                                        
                                                                                        # self.running_over = False 
                                                                                        self.running = True
                                                                                        # self.game_over = False
                                                                                        print(f"{self.running}   {self.game_over}")
                                                                                        self.ejecutar()


                                                                                        # self.game_over = False
                                                                                        pass
                                                                        elif self.paused:
                                                                            for boton in self.grupo_botones_pause:
                                                                                if boton.rect.collidepoint(mouse_pos) :
                                                                                    play_soud("PROGRAMACION 1\JuegoPy\sonido\DOORPNUM.WAV",0.2)
                                                                                    if boton == self.boton_menu:
                                                                                        pass
                                                                    def escudo_player(self):
                                                                        ancho_barra = 100
                                                                        alto_barra = 17
                                                                        x = 10
                                                                        y = 80
                                                                        fill = (self.escudo / 100) * ancho_barra
                                                                        border = pygame.Rect(x, y, ancho_barra, alto_barra)
                                                                        fill = pygame.Rect(x, y, fill, alto_barra)
                                                                        pygame.draw.rect(self.pantalla, RED, fill)
                                                                        pygame.draw.rect(self.pantalla, WHITE, border, 2)
                                                                        dibujar_texto("ESCUDO",RED,self.pantalla,60,50,20)
                                                                    def control_tiempo(self):
                                                                        self.tiempo_actual = pygame.time.get_ticks()
                                                                        self.tiempo_transcurrido = self.tiempo_actual - self.tiempo_inicio
                                                                        segundos = (self.tiempo_transcurrido // 1000) % 60
                                                                        dibujar_texto("TIEMPO: {0}".format(segundos),RED,self.pantalla,ANCHO_PANTALLA-100,20,20)
                                                                    def ejecutar(self):       
                                                                        # game over conf
                                                                        self.boton_menu = Boton("PROGRAMACION 1\JuegoPy\menu\menu.png",ANCHO_PANTALLA // 2 ,ALTO_PANTALLA // 2 + 40)
                                                                        self.boton_star = Boton("PROGRAMACION 1\JuegoPy\menu\star.png",ANCHO_PANTALLA // 2 ,ALTO_PANTALLA // 2 + 100)
                                                                        self.tiempo_inicio = pygame.time.get_ticks()
                                                                        self.tiempo_game_over = 0
                                                                        self.tiempo_mision_ok = 0

                                                                        #     print(self.tiempo_nivel)
                                                                        while self.running_over:
                                                                            # print("nivel 1")
                                                                            # self.flag_control = 
                                                                            # print(f"{self.running}{self.game_over}")
                                                                            for evento in pygame.event.get():
                                                                                if evento.type == pygame.QUIT:
                                                                                    # self.guradar_datos_game()  
                                                                                    # print(self.game_over)
                                                                                    # self.datos.append(self.score)
                                                                                    # self.running = False
                                                                                    pygame.quit()
                                                                                    sys.exit()
                                                                                elif evento.type == pygame.KEYDOWN:
                                                                                    if evento.key == pygame.K_SPACE:    
                                                                                        if self.cambiar_bala_doble:
                                                                                            self.player.double_shoot()
                                                                                        if self.cambiar_bala_simple:
                                                                                            self.player.shoot() 
                                                                                        if self.cambiar_bala_fuego:
                                                                                            self.player.shoot_fire_bol()
                                                                                        self.play_soud("PROGRAMACION 1\JuegoPy\sonido\RIFLE.WAV")
                                                                                    if evento.key == pygame.K_RETURN:
                                                                                        self.paused = not self.paused
                                                                                    # if evento.key == pygame.K_ESCAPE:
                                                                                    #     # self.running = False
                                                                                    #     # pygame.quit()
                                                                                    #     # sys.exit()
                                                                                    #     self.cambiar_nivel()
                                                                                    #     print("ok")
                                                                                if evento.type == pygame.MOUSEBUTTONDOWN:
                                                                                    self.evento_mouse()
                                                                            # self.control_pausa_gameover()
                                                                            self.control_tiempo()
                                                                            # print(self.tiempo_transcurrido,"     ",self.tiempo_game_over)
                                                                            # print(self.tiempo_nivel)
                                                                            if self.enemigo.vida > 0:
                                                                                self.tiempo_mision_ok = self.tiempo_transcurrido + 6000

                                                                            if len(self.vida.lista_vidas) > 0:
                                                                                self.tiempo_game_over = self.tiempo_transcurrido + 6000
                                                                            

                                                                            # if not self.paused :
                                                                            if self.running:
                                                                                if self.tiempo_transcurrido > 0:
                                                                                    self.pantalla.blit(self.imagen_fondo, (0, 0))
                                                                                    dibujar_texto("ATAQUE FINAL",WHITE,self.pantalla,ANCHO_PANTALLA//2,100,100)
                                                                                    self.dibujar_parrafo()
                                                                                if self.tiempo_transcurrido > 6000:
                                                                                    self.pantalla.blit(self.imagen_fondo, (0, 0))
                                                                                    self.grupo_sprites.update()
                                                                                    self.grupo_sprites.draw(self.pantalla)
                                                                                if self.enemigo1.vida == 0:
                                                                                    self.grupo_sprites.add(self.enemigo)
                                                                                if self.enemigo.vida <= 0:
                                                                                    # self.guardar_datos()
                                                                                    self.guardar = GuardarDatos(self.leer_archivo_json("score1.json"),self.leer_archivo_json("score2.json"),self.score_general)
                                                                                    dibujar_texto("Mision Completada",MORA,self.pantalla,ANCHO_PANTALLA//2,ALTO_PANTALLA//2.5,90)
                                                                                    print(self.nombre)
                                                                                    crear_y_cargar_datos(self.nombre,self.score_general)

                                                                                    if self.tiempo_transcurrido >= self.tiempo_mision_ok:                
                                                                                        self.running = False
                                                                                        retorno = Return()
                                                                                        retorno.ejecutar()
                                                                                        pygame.quit()
                                                                                        sys.exit()
                                                                                # if self.tiempo_transcurrido > 21000:
                                                                                #     # self.running_over = False
                                                                                self.control_tiempo()
                                                                                # colision items con player
                                                                            if self.tiempo_transcurrido > 8000:  
                                                                                self.colicion_item_vida_player() 
                                                                                self.choque_item_doble_player()
                                                                                self.choque_item_fuego_player()
                                                                                if self.choco:
                                                                                    self.vida.dibujar_vidas(self.pantalla,"D")
                                                                                # colision 
                                                                                self.colision_balas_asteroides()
                                                                                self.colision_laser_enemigo()
                                                                                self.colision_laser_enemigo_dos()
                                                                                self.colision_laser_item()
                                                                                self.colision_laser_player()
                                                                                # score 
                                                                                self.puntuacion_draw()
                                                                                self.escudo_player()
                                                                                self.colision_jugador_asteroide() 
                                                                            if len(self.vida.lista_vidas) <= 0:
                                                                                self.guardar = GuardarDatos(self.leer_archivo_json("score1.json"),self.leer_archivo_json("score2.json"),self.score_general)
                                                                                # guardar.guardar_datos_juego() 
                                                                                dibujar_texto("Fallaste",ORANGE,self.pantalla,ANCHO_PANTALLA//4,ALTO_PANTALLA//4,100)
                                                                                # self.running = False
                                                                                self.running = False
                                                                                retorno = Return()
                                                                                retorno.ejecutar()
                                                                            # if self.paused:
                                                                            #     dibujar_texto("PAUSA",ORANGE,self.pantalla,ANCHO_PANTALLA // 2-150,100,150)
                                                                            #     self.grupo_botones_pause.add(self.boton_menu)
                                                                            #     self.grupo_botones_pause.update()
                                                                            #     self.grupo_botones_pause.draw(self.pantalla)
                                                                            # print(len(self.vida.lista_vidas)) 
                                                                                # self.grupo_botones_game_over.draw(self.pantalla)
                                                                            pygame.display.flip()

                                                                            self.reloj.tick(FPS)
                                                                        pygame.quit() # Fin

                                                                # juego = NivelTres ()
                                                                # juego.ejecutar()

                                                                pygame.quit()
                                                                sys.exit()
                                                            self.control_tiempo_nivel(False,50)


                                                            pygame.display.flip()
                                                            self.reloj.tick(FPS)
                                                        pygame.quit() # Fin
                                                        
                                                # nivel_dos = Nivel2()
                                                # nivel_dos.nivel_dos()
                                                pygame.quit()
                                                sys.exit()
                                        # if self.tiempo_transcurrido > 21000:
                                        #     # self.running_over = False
                                        self.control_tiempo()
                                        # colision items con player
                                        self.colicion_item_vida_player() 
                                        self.choque_item_doble_player()
                                        self.choque_item_fuego_player()
                                        if self.choco:
                                            self.vida.dibujar_vidas(self.pantalla,"D")
                                        # colision 
                                        self.colision_balas_asteroides()
                                        self.colision_laser_enemigo()
                                        self.colision_laser_enemigo_dos()
                                        self.colision_laser_item()
                                        self.colision_laser_player()
                                        self.escudo_player()
                                        # score   
                                        self.puntuacion_draw()
                                        self.colision_jugador_asteroide() 
                                    if len(self.vida.lista_vidas) <= 0:
                                        self.guardar = GuardarDatos(self.score_general,0,0)
                                        # guardar.guardar_datos_juego() 
                                        dibujar_texto("Perdiste",RED,self.pantalla,ANCHO_PANTALLA//4,ALTO_PANTALLA//4,100)
                                        # self.running = False
                                        self.running = False
                                        retorno = Return()
                                        retorno.ejecutar()
                                    # if self.paused:
                                    #     dibujar_texto("PAUSA",ORANGE,self.pantalla,ANCHO_PANTALLA // 2-150,100,150)
                                    #     self.grupo_botones_pause.add(self.boton_menu)
                                    #     self.grupo_botones_pause.update()
                                    #     self.grupo_botones_pause.draw(self.pantalla)
                                    # print(len(self.vida.lista_vidas)) 
                                        # self.grupo_botones_game_over.draw(self.pantalla)
                                    pygame.display.flip()

                                    self.reloj.tick(FPS)
                                pygame.quit() # Fin

                        if __name__ == "__main__":
                            print('main')
                            menu = Menu()
                            game = Game()
                            game.menu_instancia = menu
                            game.ejecutar()
                            
                        pygame.quit()
                        sys.exit()
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
                    # elif boton == self.boton_levels:
                    #     self.menu_levels = True
                    #     self.menu_score = False
                    #     self.menu_principal = False
                    #     self.menu_setting = False
        # elif self.menu_levels:
        #     for boton in self.grupo_botones_levels:
        #         if boton.rect.collidepoint(mouse_pos):
        #             play_soud("PROGRAMACION 1\JuegoPy\sonido\DOORPNUM.WAV",self.volumen)
        #             if boton == self.boton_retornar_levels:
        #                 self.menu_principal = True
        #                 self.menu_levels = False
        elif self.menu_score:
            for boton in self.grupo_botones_score:
                if boton.rect.collidepoint(mouse_pos):
                    play_soud("PROGRAMACION 1\JuegoPy\sonido\DOORPNUM.WAV",self.volumen)
                    if boton == self.boton_retornar_score:
                        self.menu_principal = True
                        self.menu_score = False
    #Chequear si se usa
    # def guardar_nombre(self):
    #     with open("nombre.txt", "w") as archivo:
    #         archivo.write(self.nombre)
    def menu_inicio(self):
        pygame.font.init()
        screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA)) 
        clock = pygame.time.Clock()

        # pantalla principal config
        self.boton_start = Boton("PROGRAMACION 1\JuegoPy\menuu\startt.png", ANCHO_PANTALLA // 2- 150, ALTO_PANTALLA // 2 + 100)
        # self.boton_levels = Boton("PROGRAMACION 1\JuegoPy\menuu\levels.png", ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2 +100)
        self.boton_exit = Boton(r"PROGRAMACION 1\JuegoPy\menuu\quit.png", ANCHO_PANTALLA // 2+ 150, ALTO_PANTALLA // 2 + 100)
        self.boton_config = Boton("PROGRAMACION 1\JuegoPy\menuu\engranaje.png",ANCHO_PANTALLA -103,ALTO_PANTALLA-160,(100,100))
        self.boton_score = Boton("PROGRAMACION 1\JuegoPy\menuu\scores.png", 915,ALTO_PANTALLA - 2,(150,60))
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
            # print(self.lista_score)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if self.menu_principal:
                        self.menu_principal = False
                        self.menu_score = False
                
                    # else:
                    #     self.menu_levels = False
                    #     # self.menu_setting = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.manejar_evento_mouse()       
                
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    menu.manejar_evento_texto(event)  # Manejar el evento de ingreso de texto
            if self.menu_principal:
                
                screen.blit(self.imagen_menu, (0, 0))
                self.grupo_botones.draw(screen)
                dibujar_texto("Aliens vs Humanos", WHITE, screen, 600, 100, 80)
                rectangulo_nombre = pygame.Rect(ANCHO_PANTALLA // 2 - 100, ALTO_PANTALLA // 2, 200, 30)
                pygame.draw.rect(screen, WHITE, rectangulo_nombre)
                fuente = pygame.font.Font(None, 20)
                texto_superficie = fuente.render((self.nombre_ingresado), True, BLACK)
                texto_rect = texto_superficie.get_rect(center=rectangulo_nombre.center)
                screen.blit(texto_superficie, texto_rect)
                # nombre_actualizado = self.actualizar_nombre()
                print(self.nombre_ingresado)
                
            elif self.menu_setting:
                self.grupo_botones_conf.add(self.barra_vol)
                screen.blit(self.imagen_menu_conf, (0, 0))
                dibujar_texto("VOLUMEN", MORA, screen, 200, 400, 40)
                dibujar_texto("CONFIGURACION", WHITE, screen, 600, 90, 100)
                self.grupo_botones_conf.draw(screen)
            # elif self.menu_levels:
            #     screen.blit(self.imagen_menu_conf, (0, 0))
            #     dibujar_texto("LEVELS", WHITE, screen, 600, 100, 80)
                # self.grupo_botones_levels.draw(screen)
            elif self.menu_score:
                screen.blit(self.imagen_score,(0,0))
                self.dibujar_score()
                dibujar_texto("Puntuaciones", WHITE, screen, 600, 40, 100)
                self.grupo_botones_score.draw(screen)
            
            
            delta_ms = clock.tick(FPS)
            pygame.display.flip()
        

        pygame.quit() # Fin


if __name__ == "__main__":
    menu = Menu()
    menu.menu_inicio()

# if menu.menu_principal == False and menu.menu_setting == False:
#         game = Game()
#         game.ejecutar()