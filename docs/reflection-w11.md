I think the main thing that surprised me was how it was somehow both easier and harder to implement at the same time. On one hand,              
I always think of enemy path-finding AI as being something that is way over my head. But in this case, it's just tracing a path back                       
to the player. But it was also harder because it was difficult to translate that into python in a way that can interact with the play space I'm setting up.  

I verified correctness (or will be doing so) in the usual way I debug these things. By piping the function output into a print               
function. this way I can see exactly what its spitting out into the code in real time. and if it's not to my liking I can refine                 
and tweak it as I see fit.                                
 
The main thing, and the most important thing to fix at that, is getting it integrated into the pathfinding functionality.                       
I was supposed to have it done by now, but one thing led to another as these things go. Another thing I'm not quite happy with                  
is how I have rendering setup. Currently it references the maze map every frame and draws from that. This is hurting performance                
to the point I can't really work on it outside of my home pc. This is because it's going over every single item in the chunk of the                          
map that the player is in. I'd like to have it only reference the map upon entering a room and store the cords of each needed to sprite                       
in a variable. that way it can iterate over the map once per room and then iterate over the necessary material skipping the dead space in the map.                            
