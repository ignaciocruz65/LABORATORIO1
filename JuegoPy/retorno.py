import pygame,sys
from constantes import*
from auxiliar import*
from pygame.sprite import Group
class Return:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        self.pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
        
        self.grupo_botones_game_over = Group()
        self.grupo_botones_pause = Group()

        self.paused = False
        self.running = True
        self.running_over = True
        self.mostrar_texto = False
        self.game_over = False
        self.reloj = pygame.time.Clock()
        self.imagen_fondo = pygame.image.load(r"PROGRAMACION 1\JuegoPy\menuu\gameoverpic.jpg").convert()
        self.imagen_fondo = pygame.transform.scale(self.imagen_fondo, (ANCHO_PANTALLA, ALTO_PANTALLA))
    
    def evento_mouse(self):
        mouse_pos = pygame.mouse.get_pos()
        for boton1 in self.grupo_botones_game_over:
            if boton1.rect.collidepoint(mouse_pos) :
                play_soud("PROGRAMACION 1\JuegoPy\sonido\DOORPNUM.WAV",0.2)
                if boton1 == self.boton_menu:
                    from menu import Menu
                    menu = Menu()
                    menu.menu_inicio()
                    pygame.quit()
                    sys.exit()
                elif boton1 == self.boton_star:
                    
                    self.running_over = False 
                    from game import Game
                    game = Game()
                    game.ejecutar()
                    pygame.quit()
                    sys.exit()
    
    def dibujar_texto_puntuacion(self,color, superficie, pos_x, pos_y, tamaño, nombre, score):
        pygame.font.init()
        fuente_texto = r"c:\USERS\NACHO\APPDATA\LOCAL\MICROSOFT\WINDOWS\FONTS\Starborn.TTF"
        fuente = pygame.font.Font(fuente_texto, tamaño)
        texto_renderizado = fuente.render(f'Nombre: {nombre}\nScore: {score}', True, color)
        rect_texto = texto_renderizado.get_rect()
        rect_texto.centerx = pos_x  # Centrar horizontalmente
        rect_texto.y = pos_y  # Alinear en la parte superior
        superficie.blit(texto_renderizado, rect_texto)
        return rect_texto
    def ejecutar(self):       
    # game over conf
        self.boton_menu = Boton("PROGRAMACION 1\JuegoPy\menu\menu.png",ANCHO_PANTALLA // 2 ,ALTO_PANTALLA // 2 + 40)
        self.boton_star = Boton("PROGRAMACION 1\JuegoPy\menuu\startt.png",ANCHO_PANTALLA // 2 ,ALTO_PANTALLA // 2 + 100)
        self.tiempo_inicio = pygame.time.get_ticks()
        self.tiempo_nivel = 0
        

        while self.running_over:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    self.evento_mouse()
            
            if self.running_over:
                self.pantalla.blit(self.imagen_fondo, (0, 0))
                dibujar_sprite_estatico("PROGRAMACION 1\JuegoPy\menuu\gameover.png",self.pantalla,ANCHO_PANTALLA // 2-200,80,400,200)
                self.grupo_botones_game_over.add(self.boton_menu,self.boton_star)
                self.grupo_botones_game_over.update()
                self.grupo_botones_game_over.draw(self.pantalla)
            pygame.display.flip()

            self.reloj.tick(FPS)
        pygame.quit() # Fin
