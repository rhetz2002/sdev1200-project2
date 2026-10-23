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
chunk (x, y) (map will be orginized into rooms/chunks that the player will have to traverse this stores which room/chunk the player is in)                
sprite(file)                     
size (int, int)                    
player_move (method)                  
pleyer_attack (method)                      
                             
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

## sudocode                          
                              
_-___________________-_                      
player.py                   
                       
player_move()                           
                                      
moves plyer if key is pressed                           
                              
player attack()                              
                                      
player attacks if key is pressed()                             
                            
_-___________________-_              
render.py                        
                        
render functionality                          
                            
import sprite classes                       
                                             
(still figuring this out a bit but                 
i feel it may be cleaner if i handel                
it in a seperate file)                
                          
_-___________________-_                      
enemies.py             
                            
stores data and funtions                     
pertaining to enemies               
                                  
import pathfind funtion                           
                          
move()                    
                                                   
uses pathfind funtion to move enemies and updates                            
                          
mage_attack()                       
chooses a num between 1-30                 
if num 1 then attack                       
                        
mele attack()                  
if touching player attack                        
                               
enemy_health_check()                      
iterates through valid                        
onscreen enemy health                                      
                                   
if enemy healh =< 0 enemy                                  
is dead and unloaded                                        
_-___________________-_                               
                          
algorithm.py                                    
                               
pathfind_algorithm()                       
                                                                   
stores pathfinding algoritm and when called is executed                      
                              
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

<code>
(load secondary files)

(load sprites)

(core loop)

    while game not started
    
        (load menu screen)

        run program_kill()

    while game start
    
    (initalize tick clock)
    
    run setup()

    start game 
        
        check for game running if game running

            check for player position
                
                if in finish X Y range proceed to win screen

                else check for enemies in valid xy range and load enemies

                unload offscreen enemie sprites 

                run player_move()

                run player_attack()

            check loded enemies position

            run move()

            run mage_attack()

            run mele_attack()

            run enemie_health_check()

            run program_kill()
    while won

        display win screen

        check for reset click

        run program kill()

    when reset 

        run setup()

        start game

        run program_kill()
</code>
## game state                    
                             
curently game state lives in main loop in main.py which i think is the cleanest solution for this it is checking for player position, health, and input as well as game tick for certan random events. the main loop is initalised when player clicks start and ends when player wins/looses.                  
                  
## processess                     
                 
the game is checking for these events while running                        
                     
- player health                  
                                                                                           
- player possition for winning game and for which chunk of the map / enemies are loaded                  
                   
- enemy health            
                         
- win or lose condition            
                                                                
- keys pressed for player movement/attack or for pausing game                     
                     
- game tick clock           
                                           
- wether player has been hit by enemy                     
                                       
- if X has been clicked to close game               
                                                     
- if game is paused or on win/lose/start screens              
                    
- drawing frames                 