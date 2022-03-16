# -------------------------------------------
# Libraries

from pyamaze import maze, COLOR, agent
import pyhop

r, c = 3, 3

# -------------------------------------------
# Initialize maze
m=maze(r, c)
m.CreateMaze(theme=COLOR.light)
print(m.maze_map)
m.run()
# map of position -> E, W, N, S
position_walls = m.maze_map

# -------------------------------------------
# Set start state
start = pyhop.State('start')
start.position = (r, c)
start.walls = position_walls[start.position]
start.E_wall = position_walls[start.position]['E']
start.W_wall = position_walls[start.position]['W']
start.N_wall = position_walls[start.position]['N']
start.S_wall = position_walls[start.position]['S']

# -------------------------------------------
# Set goal state
goal = pyhop.State('goal')
goal.position = (1, 1)
goal.walls = position_walls[goal.position]
goal.E_wall = position_walls[goal.position]['E']
goal.W_wall = position_walls[goal.position]['W']
goal.N_wall = position_walls[goal.position]['N']
goal.S_wall = position_walls[goal.position]['S']