## File Structure      

- modified file structure by removing UI.py and adding maze.py

- modified player and enemy classes to reflect current sate and added maze oriented classes and win/start screen sprite classes

- updated player sudo code to reflect current state and better explained

- updated render sudo code to reflect current state and better explained

- updated main sudo code to reflect current state and better explained

overall folder structure      
            
sdev1200-project2             
├── game/                          
│     ├── main.py              
│     ├── maze.py                 
│     ├── render.py               
│     ├── player.py                 
│     ├── enemies.py                 
│     ├── algorithm.py                   
│     ├── secondary_functions.py               
│     └── sprites/                
├── docs/                   
└── README.md                      
                        
## classes                      
                       
- player                    
hp (int)
direction (int)
offset(x, y) (keeps the player on the defined grid)
position (x, y)                              
chunk (x, y) (map will be organized into rooms/chunks that the player will have to traverse, this stores which room/chunk the player is in)                
sprite(file, sprite for up down left right and corresponding sprites for attacking)                                        
player_con (method)                                   
                             
- mage
sprite (file)                                     
hp (int)
position (x, y)
spawn(method)
update (method)                       
attack (method)               
                                
- mele
sprite (file)                                     
hp (int)
position (x, y)
spawn(method)
update (method)                       
attack (method)                    

- win_floor
position (x, y)
sprite(file)

- wall_block
position (x, y)
sprite(file)
wall_location(method)
maze_draw(method)

- screen_start
sprite(file)
position(x, y)

- screen_win
sprite(file)
position(x, y)

## pseudocode                          
                              
_-___________________-_                      
player.py                   
                       
player_con()

grab player input

check if input is w
   
   change to up facing sprite

   if not at edge or in front of a wall

      move one space up

check if input is a

   change to up facing sprite

   if not at edge or in front of a wall

      move one space up

check if input is s

   change to up facing sprite

   if not at edge or in front of a wall

      move one space up

check if input is d

   change to up facing sprite

   if not at edge or in front of a wall

      move one space up

check if input is shift

   if player is facing up, display corresponding attack sprite

   if player is facing down, display corresponding attack sprite

   if player is facing left, display corresponding attack sprite

   if player is facing right, display corresponding attack sprite

if on win tile

   win = true
   game = false

_-___________________-_              
render.py                        
                        
display_setup()

   set up display window

sprite_initialize()

   creates sprite groups based on a list stored 
   in the main.py file and stores in a dictionary

main_menu_render

   renders the menu screen

game_render

   set background as white

   draw player_sprite

   run maze_draw method (also draws enemies)
   
_-___________________-_                      
enemies.py             
                            
stores data and functions                     
pertaining to enemies               
                                  
import path find function                            
                          
move()                    
                                                   
uses path find function to move enemies and updates                            
                          
mage_attack()                       
chooses a num between 1-30                 
if num 1 then attack                       
                        
mele attack()      

if touching player attack                        
                               
enemy_health_check()                      
iterates through valid                        
onscreen enemy health                                      
                                   
if enemy health =< 0 enemy                                  
is dead and unloaded                                        
_-___________________-_                               
                          
algorithm.py                                    
                               
heuristics()

   calculates the Manhattan distance by adding the absolute value of the start and goal

algorithm()

   repeatedly checks the neighboring tiles to find the optimal path to the goal stores in 
   local variable to reconstruct and be followed by the enemy
                              
_-____________________-_                                     
                              
secondary_functions.py                            
                        
_-____________________-_                 
             
main.py

```
(load secondary files)

(load global variables)

(load sprites)

(initialize window)

(core loop)

    while game not started
    
        (load menu screen)

        run program_kill()

    while game start
    
    (initialize tick clock)
    
    run setup()

    start game 
        
        check for game running if game running

            check for player position

                run player_move()

            check loaded enemies position

            run move()

            run program_kill()

    while won

        display win screen

        check for reset click

        run program kill()

```
## game state                    
                             
currently game state lives in main loop in main.py which i think is the cleanest solution for this it is checking for player position, health, and input as well as game tick for certain random events. the main loop is initialized when player clicks start and ends when player wins/looses.                  
                  
## processes                      
                 
the game is checking for these events while running                        
                     
- player health                  
                                                                                           
- player position for winning game and for which chunk of the map / enemies are loaded                  
                   
- enemy health            
                         
- win or lose condition            
                                                                
- keys pressed for player movement/attack or for pausing game                     
                     
- game tick clock           
                                           
- whether player has been hit by enemy                     
                                       
- if X has been clicked to close game               
                                                     
- if game is paused or on win/lose/start screens              
                    
- drawing frames                 
