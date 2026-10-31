import pygame

from pygame.locals import (
    QUIT
)

import sys

from secondary_functions import program_kill
from render import display_setup
from render import sprite_initalise
from render import main_menu_render
from render import game_render

from render import screen_start

sprite_list_single = [screen_start]

sprite_list_single1 = [ "player_attack_up_face", "player_idel_up_face", "player_attack_down_face",
"player_idel_down_face", screen_start, "enviroment_floor_goal", "player_attack_left_face", 
"player_idel_left_face", "player_attack_right_face", "player_idel_right_face"]

sprite_list_group1 = [ "enemy_mage", "enviroment_wall", "enemy_mele", "enviroment_floor" ]

running = True
menu = True
game = False

screen = display_setup()

sprites = sprite_initalise(sprite_list_single, sprite_list_group1)

while running: 

    while menu is True:

        for event in pygame.event.get():
                  
            if event.type == pygame.MOUSEBUTTONDOWN:
                           
                if event.button == 1:
                    
                    mouseX, mouseY = event.pos
                
                    if 840 >= mouseX >= 540 and 780 >= mouseY >= 670:
                        
                        menu = False
                                
                        game = True

            # if player clicks on X quit game
            
            if event.type == QUIT:
                
                        pygame.quit()
                        sys.exit()

        # show main menu

        main_menu_render(sprites, screen)

    while game is True:

        game_render(sprites, screen)        

        running = program_kill()