import pygame

from pygame.locals import (
    QUIT
)

import sys

#from secondary_functions import program_kill
from render import display_setup
from render import sprite_initalise
from render import main_menu_render
from render import game_render
from render import win_render

from render import screen_win
from maze import wall_block
from render import screen_start
from player import player
from enemies import mele
from enemies import mage


#from maze import maze_map

sprite_list_single = [screen_start, player, screen_win]

sprite_list_group = [wall_block, mele, mage]

sprite_list_single1 = [ player, "player_idel_up_face", "player_attack_down_face",
"player_idel_down_face", screen_start, "enviroment_floor_goal", "player_attack_left_face", 
"player_idel_left_face", "player_attack_right_face", "player_idel_right_face"]

sprite_list_group1 = [ "enemy_mage", "enviroment_wall", "enemy_mele", "enviroment_floor" ]

running = True
menu = True
game = False
move_tick = 0
past_chunkX = -999
past_chunkY = -999

screen = display_setup()

sprites = sprite_initalise(sprite_list_single, sprite_list_group)

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
        
        move_tick, chunkX, chunkY, game, win, wallpos = sprites['player1'].player_con(move_tick, sprites)

        game_render(sprites, screen, chunkY, chunkX, past_chunkX, past_chunkY)

        #mele_move(wallpos, sprites['player1'].row, sprites['player1'].collum)

        sprites['mage1'].update(wallpos, sprites['player1'].row, sprites['player1'].collum)       

        for event in pygame.event.get():
            
            if event.type == QUIT:
                
                pygame.quit()
                sys.exit() 
    
    while win is True:

        win_render(sprites, screen)

        for event in pygame.event.get():
            
            if event.type == QUIT:
                
                pygame.quit()
                sys.exit() 

        