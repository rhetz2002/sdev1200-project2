## File Structure      
        
overall folder structure      
            
sdev1200-project2             
├── game/                          
│     ├── main.py              
│     ├── ui.py                 
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
position (x, y)                              
chunk (x, y) (map will be organized into rooms/chunks that the player will have to traverse, this stores which room/chunk the player is in)                
sprite(file)                     
size (int, int)                    
player_move (method)                  
player_attack (method)                      
                             
- enemy_mage                   
move (method)                       
attack (method)                   
hp (int)                     
sprite (file)                          
size (int, int)               
                                
- enemy_mele                    
move (method)                        
attack (method)                       
hp (int)                      
sprite (file)                  
size (int, int)                       

## pseudocode                          
                              
_-___________________-_                      
player.py                   
                       
player_move()                           
                                      
moves plyer if key is pressed                           
                              
player attack()                              
                                      
player attacks if key is pressed                           
                            
_-___________________-_              
render.py                        
                        
render functionality                          
                            
import sprite classes                       
                                             
(still figuring this out a bit                          
but I feel it may be cleaner if                          
I handle it in a separate file)                         
                          
_-___________________-_                      
enemies.py             
                            
stores data and functions                     
pertaining to enemies               
                                  
import pathfind function                            
                          
move()                    
                                                   
uses pathfind function to move enemies and updates                            
                          
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
                               
pathfind_algorithm()                       
                                                                   
stores pathfinding algorithm and when called is executed                      
                              
_-____________________-_                                     
                              
secondary_functions.py                            
                      
setup()                                
                                      
sets up/resets settings to start                     
sate including health score player pos                  
                                   
pause()                
                 
pauses game               
                   
program_kill()               
                                         
closes program if condition is valid              
_-____________________-_                 
             
main.py

```
(load secondary files)

(load sprites)

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
                
                if in finish X Y range proceed to win screen

                else check for enemies in valid x y range and load enemies

                unload offscreen enemy sprites 

                run player_move()

                run player_attack()

            check loaded enemies position

            run move()

            run mage_attack()

            run mele_attack()

            run enemy_health_check()

            run program_kill()
    while won

        display win screen

        check for reset click

        run program kill()

    when reset 

        run setup()

        start game

        run program_kill()
```
## game state                    
                             
currently game state lives in main loop in main.py which i think is the cleanest solution for this it is checking for player position, health, and input as well as game tick for certain random events. the main loop is initalised when player clicks start and ends when player wins/looses.                  
                  
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