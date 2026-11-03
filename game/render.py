import pygame
from maze import wall_block



class screen_start(pygame.sprite.Sprite):
    def __init__(self):
        
        super().__init__()
        
        self.image = pygame.image.load('sprites/screen_start.png').convert_alpha()
        
        self.rect = self.image.get_rect()

        self.rect = self.image.get_rect(center=(700, 450))


def display_setup():

    width = 1400
    height = 900
    screen = pygame.display.set_mode((width, height))
    return screen

def sprite_initalise(sprite_list_single, sprite_list_group):

    sprites = {}

    for item in sprite_list_single:

        name = item.__name__
        
        sprites[f'{name}1'] = item()

        sprites[f'{name}_sprite'] = pygame.sprite.GroupSingle()

        sprites[f'{name}_sprite'].add(sprites[f'{name}1'])

    for item in sprite_list_group:

        name = item.__name__
    
        sprites[f'{name}1'] = item()
    
        sprites[f'{name}_sprite'] = pygame.sprite.Group()
    
        sprites[f'{name}_sprite'].add(sprites[f'{name}1'])

    return sprites

    #begening render

def main_menu_render(sprites, screen):

    sprites['screen_start_sprite'].draw(screen) 
        
    pygame.display.flip() 

# maze, player_chunk

def game_render(sprites, screen, x, y):

    screen.fill((255, 255, 255))

    sprites['player_sprite'].draw(screen)

    sprites['wall_block1'].maze_draw(screen, x, y, sprites)

    pygame.display.flip()



    #win or loose render

    