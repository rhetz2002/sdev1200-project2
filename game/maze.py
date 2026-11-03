import heapq
import pygame

maze_map = [[[[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1]],
             [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]]]

class wall_block (pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        
        self.row = 0

        self.collum = 0
        
        self.image = pygame.image.load('sprites/enviroment_wall.png').convert_alpha()  
        
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()

        

    def maze_draw (self, screen, playerX, playerY, sprites):

        #self.rect.topleft = (self.row * 100, self.collum * 100)

        count = 0

        room = maze_map[playerY][playerX]               # lock onto the first two layers

        for x, row in enumerate(room):               # the whole row, e.g. [1,0,0,0,...,1]

            for y, tile in enumerate(row):  # j = index inside that row -> maze_map[a][b][i][j]
                
                if tile == 1: 
                
                    self.rect.topleft = (y * 100, x * 100)
                    screen.blit(self.image, self.rect)
                    

