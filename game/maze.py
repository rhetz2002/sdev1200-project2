import heapq
import pygame

# key

# 0 = floor
# 1 = wall
# 2 = mele enemy
# 3 = mage enemy
# 9 = goal
# [[0]] is an empty chunk to keep the list alligned

maze_map = [[[[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,1,1,1,1,1,0,0,0,1,1,1,1,1]],
             [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,2,0,1],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [0,0,0,0,0,0,0,3,0,0,0,0,0,1],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,2,0,0,0,0,0,1],
              [1,1,1,1,1,1,0,0,0,1,1,1,1,1]],
              [[0]]],
            [[[1,1,1,1,1,1,0,0,0,1,1,1,1,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,2,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,0,0,2,0,0,0,0,0,0,2,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1]],
             [[1,1,1,1,1,1,0,0,0,1,1,1,1,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,3,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,1,1,1,1,1,0,0,0,1,1,1,1,1]],
             [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,1,1,1,1,1,0,0,0,1,1,1,1,1]]],
            [[[0]],
             [[1,1,1,1,1,1,0,0,0,1,1,1,1,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1]],
             [[1,1,1,1,1,1,0,0,0,1,1,1,1,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,9],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,9],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,9],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,0,0,0,0,0,0,0,0,0,0,0,0,1],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]]]

class win_floor (pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        
        self.row = 0

        self.collum = 0
        
        self.image = pygame.image.load('sprites/enviroment_floor_goal.png').convert_alpha()  
        
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()
    

class wall_block (pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()
        
        self.row = 0

        self.collum = 0
        
        self.image = pygame.image.load('sprites/enviroment_wall.png').convert_alpha()  
        
        self.image = pygame.transform.scale(self.image, (100, 100))

        self.rect = self.image.get_rect()

    def wall_location (self, playerX, playerY):

        walls = set()

        room = maze_map[playerY][playerX] 

        for x, row in enumerate(room):               

            for y, tile in enumerate(row):  
                
                if tile == 1: 

                    walls.add((x,y))
    
    def maze_draw (self, screen, playerX, playerY, sprites):
        
        self.kill
        win_tile = win_floor()
        win_floor.kill
        sprites['mele1'].kill
        sprites['mage1'].kill

        room = maze_map[playerY][playerX]               

        for x, row in enumerate(room):               

            for y, tile in enumerate(row):  
                
                if tile == 1: 
                
                    self.rect.topleft = (y * 100, x * 100)
                    screen.blit(self.image, self.rect)
                
                elif tile == 9: 

                    win_tile.rect.topleft = (y * 100, x * 100)
                    screen.blit(win_tile.image, win_tile.rect)

                elif tile == 2:

                  sprites['mele1'].spawn. = (y *100, x * 100)
                  screen.blit(sprites['mele1'].image, sprites['mele1'].rect)

                elif tile == 3:

                    
                    
        
        return


                

    
                    

