import sys
import pygame

pygame.init()


class Game:
    
    def __init__(self) -> None:
        pygame.display.set_caption('Demo')
        self.screen = pygame.display.set_mode((640,480))
        self.img = pygame.image.load(r'c:\Users\Nacho\Desktop\Nueva carpeta\vsc\PROGRAMACION 1\Pygame\imgs\ghost.png')
        self.clock = pygame.time.Clock()

        self.movement = [False, False, False,False]
        self.img_pos = [160,260]
        self.collision_area = pygame.Rect(50,50,300,50)
    
    def run(self):
        
        while True:
            self.screen.fill((14,219,248))
            
            img_r = pygame.Rect(self.img_pos[0],self.img_pos[1],self.img.get_width(),self.img.get_height())
            
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen,(0,100,110),self.collision_area)
            else:
                pygame.draw.rect(self.screen,(0,50,110),self.collision_area)
            
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.img_pos[0] += (self.movement[2] - self.movement[3]) * 5
            self.screen.blit(self.img,self.img_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[2] = True
                    if event.key == pygame.K_LEFT:
                        self.movement[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[2] = False
                    if event.key == pygame.K_LEFT:
                        self.movement[3] = False
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()