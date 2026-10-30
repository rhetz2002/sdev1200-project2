import pygame
import sys

from secondary_functions import program_kill
from render import display_setup

running = True
menu = True

display_setup()

while running: 

    while menu is True:

#       show main menu

#       if player clicks on X quit game

        running = program_kill()