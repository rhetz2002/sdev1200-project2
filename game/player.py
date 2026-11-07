import pygame
import sys
from pygame.locals import (
    K_w,
    K_s,
    K_a,
    K_d,
    K_LSHIFT,
)
from maze import maze_map


class player(pygame.sprite.Sprite):

    #def __init__(self, lives, health, x, y, image):
    def __init__(self):

        super().__init__()

        def load(name):

            img = pygame.image.load(f'sprites/{name}.png').convert_alpha()
            return pygame.transform.scale(img, (100, 100))

        self.img_up = load('player_idel_up_face')
        self.img_down = load('player_idel_down_face')
        self.img_left = load('player_idel_left_face')
        self.img_right = load('player_idel_right_face')

        self.atk_up = load('player_attack_up_face')
        self.atk_down = load('player_attack_down_face')
        self.atk_left = load('player_attack_left_face')
        self.atk_right = load('player_attack_right_face')

        self.image = self.img_down

        self.offsetX = 0

        self.offsetY = 0

        self.chunkX = 0
        
        self.chunkY = 0

        self.collum = 5

        self.row = 4

        self.rect = self.image.get_rect()

        self.rect.topleft = (self.offsetX + self.row * 100, self.offsetY + self.collum * 100)
        
        self.hp = 20

        self.direction = 0
    
    def player_con(self, move_tick):

        pressed = pygame.key.get_pressed()

        if pressed[K_w]:
            
            self.image = self.img_up

            if self.collum >= 0.5:

                if move_tick >= 150 and maze_map[self.chunkX][self.chunkY][self.collum -1][self.row]  != 1:
                
                    self.collum -= 1
                
                    move_tick = 0

                    self.direction = 1

                else:

                    move_tick += 1
            
            elif self.collum == 0:

                if move_tick >= 150:

                    self.collum = 8 

                    self.chunkX -= 1        

                else:

                    move_tick += 1

        if pressed[K_s]:
            
            self.image = self.img_down

            if self.collum <= 7.5:

                if move_tick >= 150 and maze_map[self.chunkX][self.chunkY][self.collum +1][self.row]  != 1:

                    self.collum += 1

                    move_tick = 0

                    self.direction = 0
                    
                else:

                    move_tick += 1
            
            elif self.collum == 8:
                
                if move_tick >= 150:
                    
                    self.collum = 0 

                    self.chunkX += 1

                else:

                    move_tick += 1

        if pressed[K_a]:
            
            self.image = self.img_left

            if self.row >= 0.5:

                if move_tick >= 150 and maze_map[self.chunkX][self.chunkY][self.collum][self.row - 1]  != 1:    
                
                    self.row -= 1

                    move_tick = 0

                    self.direction = 2             

                else:

                    move_tick += 1

            elif self.row == 0:
                
                if move_tick >= 150:

                    self.row = 13 

                    self.chunkY -= 1

                else:

                    move_tick += 1       


        if pressed[K_d]:
            
            self.image = self.img_right

            if self.row <= 12.5:

                if move_tick >= 150 and maze_map[self.chunkX][self.chunkY][self.collum][self.row + 1]  != 1:
                
                    self.row += 1

                    move_tick = 0

                    self.direction = 3
                
                else:

                    move_tick += 1

            elif self.row == 13:

                if move_tick >= 150:

                    self.row = 0 

                    self.chunkY += 1

                else:

                    move_tick += 1

        if pressed[K_LSHIFT] and self.direction == 0:

            self.image = self.atk_down

        if pressed[K_LSHIFT] and self.direction == 1:

            self.image = self.atk_up

        if pressed[K_LSHIFT] and self.direction == 2:

            self.image = self.atk_left

        if pressed[K_LSHIFT] and self.direction == 3:

            self.image = self.atk_right

        if maze_map[self.chunkX][self.chunkY][self.collum][self.row] == 9:
            win = True
            game = False

        else:

            win = False
            game = True

        self.rect.topleft = (self.offsetX + self.row * 100, self.offsetY + self.collum * 100)
        return move_tick, self.chunkX, self.chunkY, game, win

    #def damage(self):

    #    self.hp -= 1

     #   if self.hp <= 0:

     #       gameover = True

      #      return gameover 