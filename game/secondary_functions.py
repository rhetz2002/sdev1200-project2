import pygame
import sys

from pygame.locals import (
    QUIT
)

def program_kill():
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
    
            pygame.quit()
            sys.exit()




