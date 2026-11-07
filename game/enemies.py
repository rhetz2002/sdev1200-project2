import pygame
from maze import maze_map
from maze import wall_block

class mage(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        
        self.image = pygame.image.load('sprites/enemy_mage.png').convert_alpha()  
        
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()

    def atk(self):
        
        bullet = orange_bullet()

        bullet.fire(self.rect.x, self.rect.y)

        return bullet

    def spawn(self, item):

        self.rect.topleft = (item, -110)

    def update(self):

        self.rect.y += 1

        if self.rect.y >= 900:

            self.kill()

class mele(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        
        self.image = pygame.image.load('sprites/enemy_mele.png').convert_alpha()  
        
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()

    def atk(self):
        
        bullet = orange_bullet()

        bullet.fire(self.rect.x, self.rect.y)

        return bullet

    def spawn(self, chunkX_curent, chunkY_curent, chunkX_past, chunkY_past):

        #if chunkX_curent =! chunkX_past or if chunkY_curent =! chunkY_past:

        #room = maze_map[chunkY_curent][chunkX_curent]

        #for x, row in enumerate(room):              

            #for y, tile in enumerate(row):  
                #if tile == 2: 
                
                    #self.rect.topleft = (y * 100, x * 100)
                    #screen.blit(self.image, self.rect)




        self.rect.topleft = (item, -110)

    def update(self):

        self.rect.y += 1

        if self.rect.y >= 900:

            self.kill()

#def pathfindtest ()

#    alcorithnm

