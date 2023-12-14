import pygame,sys,random
from auxiliar import*
# from pygame.sprite import _Group
from constantes import*
from explocion import Explosion
from retorno import Return
from basedatos import *

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
        self.nombre = ''
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
            ">----------------------------------------------GLHF---------------------------------------------------<"
    def puntuacion_draw(self):
        dibujar_texto("PUNTUACION:",WHITE,self.pantalla,ANCHO_PANTALLA-210,70,25)
        dibujar_texto(str(self.score),RED,self.pantalla,ANCHO_PANTALLA-50,70,25)
        dibujar_texto(self.nombre, LIMON, self.pantalla, ANCHO_PANTALLA//2, 20, 25)
    
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
        self.tiempo_transcurrido = self.tiempo_actual - self.tiempo_inicio_nivel
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
                insertar_datos(self.nombre,self.score)
                pygame.mouse.set_visible(True)
                dibujar_texto("Perdiste",RED,self.pantalla,ANCHO_PANTALLA//4,ALTO_PANTALLA//4,100)
                self.running = False
                retorno = Return()
                retorno.ejecutar()
                pygame.quit()
                sys.exit()
                # retorno.dibujar_texto_puntuacion(WHITE,self.pantalla,ANCHO_PANTALLA//4,ALTO_PANTALLA//2,100,self.nombre,self.score)
            if self.tiempo_transcurrido_nivel > 31000:  # en 31000
                from nivel_tres import NivelTres
                level = NivelTres()
                level.score_general += self.score
                level.nombre = self.nombre
                level.ejecutar()
                pygame.quit()
                sys.exit()
            self.control_tiempo_nivel(False,50)
            pygame.display.flip()
            self.reloj.tick(FPS)
        pygame.quit() # Fin
