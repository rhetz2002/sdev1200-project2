# dungeon crawl  
     
## concept summary        

In this game you take control of a warrior with a sword in a randomly generated maze, your objective is to make it to the end of the maze while you fight off attacking enemies. The enemies either have a ranged attack or mele attack. Mele attacking enemies will hit when the player touches the enemy, ranged attacking enemies will wit when the projectile hits the player. Your attacks hit with a small range as you swing a sword, I may add power ups later on but probably not in the initial release. I may also add a boss near the end but also not in the first release. 
      
## core loop            
                  
The player will take control of a warrior with a sword in a randomly generated maze going from one room to the next fighting enemies. There are two types of enemies mele and ranged. The player has a set hp value that decreases when hit. If the players hp reaches zero, the game is over. The player can heal with random health drops. When the player reaches the end of the maze, the game ends and the player wins. 
                                                  
## controls                   
                        
W, A, S, D to move and space to swing and esc to pause. a Very simple and average control scheme.                 
                                                                                 
## goal                              
                          
The goal at this point in time is to reach the end of the maze. (I may add a boss in my own time as I think this may turn into a pet project.)                     
                                              
## features                   
                             
(v1 must have)                 
                         
- enemies                 
                
- controls including attack                     
                                  
- win condition                                
                             
- enemy path finding                     
                                    
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

Basic shapes for v1.0, may make some art for it as I go into v2 but will be dependent on time and workload. (# and may not be that good)

## algorithm

I'm hoping to use two algorithms in this game if I have time. The main one that will be implemented in v1 is a pathfinding algorithm that tracks the player's position. I'm going to be using focused D* as it's good at recalculating on the fly if the player moves. 

For another algorithm to compare it too ill go with dynamic D* which is an earlier iteration of focused D*. It's supposedly a bit slower, so I think it'd be interesting to compare the old to the new. 

For a maze generation algorithm, I found this simple but handy algorithm for generating a dungeon like maze.  
[https://www.roguebasin.com/index.php?title=A_Simple_Dungeon_Generator_for_Python_2_or_3](https://www.roguebasin.com/index.php?title=A_Simple_Dungeon_Generator_for_Python_2_or_3)

As this one will probably be something i do in my free time, I'll not be choosing something to compare it too 