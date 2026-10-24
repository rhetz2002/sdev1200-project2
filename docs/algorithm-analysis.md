# algorithm comparison               
             
For this I'm going to be comparing A* and D* both are path finding algorithms but they accomplish there jobs in different ways.           
             
The main difference that jumps out to me is that A* works from the starting point to the end point and D* works from the reverse, Starting at the end and working its way to the start.

A* works by taking the distance between point a and b, this can be done in a number of ways. For how I plan to make this game it will be the sum of the horizontal and vertical distance. It then takes this value and adds it to parameter G which is the given cost to move to the square. This gives us F which is the value that determines if it moves to a square or not, it repeats this until it reaches its target.

D* is similar to A* but as i mentioned it works backwards from the goal to the starting point. From what i understand it uses a similar process to gauge cost of pathing but it checks for changes in the environment in the proccess, like an obstacle in the path. If an obstacle is in the way it re-does the proccess finding a new path.

When comparing the two across correctness, performance, and complexity to implement, in my opinion both are fairly equal in there correctness as both find the most optimal path forward, the main difference here is correcting course for a changing environment. D* is more cost effective in performance but that doesn't matter in this use case. implementation complexity is a big one as D* is a pain to implement. I've been having issues finding proper documentation on D* as its largely been replaced by D* lite but i do know its implementation is allot more complex than A* 

I'm going to be using A* for this project as its more simple to implement and more for beginner projects like this. A* is ok with static environments like this will be. I'd use D* if the layout was more complex/changing ie a more complex game
