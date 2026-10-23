# algorithm comparision

for this im going to be compairing A* and D* both are path finding algorythms but they acomplish there jobs in difrent ways
the main difrence that jumps out to me is that A* works from the starting point to the end point and D* works from the revrese, starting at the end and working its way to the start.

A* works by taking the distance between point a and b this can be done in a number of ways for how i plan to make this game it will be the horizontal and virtical distance. it takes this value and ands it to peramiter G which is the given cost to move to the square and that gives us F which is the value that determines if it moves to a square or not, it repeats this untill it reches its target.

conversly D* is allot more complex,