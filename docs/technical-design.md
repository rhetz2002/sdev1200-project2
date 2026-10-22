enemies.py

stores data and funtions 
pertaining to enemies

import pathfind funtion

move()

uses pathfind funtion to move enemies and updates

_-___________________-_

algorithm.py

pathfind_algorithm()

stores pathfinding algoritm and when called is executed

_-____________________-_

secondary_functions.py

setup()

sets up/resets settings to start 
sate including health score player pos

_-____________________-_

main.py

(load secondary files)

(load sprites)

(core loop)

    while game not started
    
        (load menu screen)

    when game start
    
    (initalize tick clock)
    
    run setup()

    start game screen while game runnning

        check for player position

        if in finish X Y range proceed to win screen

    while won

        display win screen

        check for reset click

    when reset 

        run setup()

        start game