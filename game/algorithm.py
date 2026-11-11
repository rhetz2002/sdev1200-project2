import heapq
from maze import maze_map


def huristics(start, goal):

    manhattan_dist = abs(start[0] - goal[0]) + abs(start[1] - goal[1])

    return manhattan_dist

def algorithm(room, start, goal,):

    rows, cols = len(room), len(room[0])

    open_heap = [(huristics(start, goal), 0, start)]

    came_from = {}

    g_cost = {start: 0}
    
    closed = set()

    while open_heap:
        
        _, g, current = heapq.heappop(open_heap)

        if current == goal:
            
            path = []
            
            while current != start:
                
                path.append(current)
                
                current = came_from[current]
            
            path.reverse()
            
            return path

        if current in closed:
            continue
        closed.add(current)
        
        for direc_row, direc_col in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nxt = (current[0] + direc_row, current[1] + direc_col)

            if not (0 <= nxt[0] < rows and 0 <= nxt[1] < cols):
                continue
            if room[nxt[0]][nxt[1]] == 1:
                continue
            if nxt in blocked and nxt != goal:
                continue

            new_g = g + 1
            if new_g < g_cost.get(nxt, float('inf')):
                g_cost[nxt] = new_g
                came_from[nxt] = current
                heapq.heappush(open_heap, (new_g + manhattan(nxt, goal), new_g, nxt))

    return None

