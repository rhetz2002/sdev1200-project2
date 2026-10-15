# Air Combat Command    
     
     
## concept summary        

in this game you take controll of a warior with a sword in a randomly generated maze, your objective is to make it to the end of the maze while you fight off attacking enemies. the enemies either have a ranged attack or mele atack. mele atacking enemies will hit when the player touches the enemie ranged attacking enemies will wit when the projectile hits the player. your attacks hit with a small range as you swing a sword, i may add power ups later on but probably not in the inital release. i may also add a boss near the end but also not in the first release.
      
## core loop            
                  
The player will take controll of a warior with a sword in a randomly generated maze going from one room to the next fighting enemeis there are two types of enemies mele and ranged. the player has a set hp value that decreses when hit. the player can heal by random health drops. when the player reaches the end of the maze the game is ends
                                                  
## controls                   
                        
W, A, S, D to move and space to swing and esc to pause. a Very simple and average control scheme.                 
                                                                                 
## goal                              
                          
The goal at this point in time is to reach the end of the maze (i may add a boss in my own time as i think this may turn into a pet project)                     
                                              
## features                   
                             
(v1 must have)                 
                         
- enemies                 
                
- controls including attack                     
                                  
- win condition                                
                             
- enemie path finding                       
                                    
- basic graphics                     
                           
(later)                       
                      
- maze generation                
                    
- power ups                   
                     
- menus                      
                  
- proper art                      
                       
- health items               
                    
## game states                     
                    
- menu / title screen                         
                                
- main gameplay

- screen transitions.
                   
- game over                 
                
- win screen                
               
## art direction

basic shapes for v1.0 may make some art for it as i go into v2 but will be dependent on time and workload (# and may not be that good)

## algorithm

im hopeing to use two algorithms in this game if i have time, the main one that will be implimented in v1 is a pathfinding algorythm that tracks the players position im going to be using the A* family of algorythms for this

for a maze genoration algorithm i found this simple but handy algorithm for generating a dungion like maze 
[https://www.roguebasin.com/index.php?title=A_Simple_Dungeon_Generator_for_Python_2_or_3](https://www.roguebasin.com/index.php?title=A_Simple_Dungeon_Generator_for_Python_2_or_3)