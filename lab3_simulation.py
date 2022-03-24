from pyamaze import maze, COLOR, agent
from lab3_planner import planner

# -------------------------------------------
# Functions
def plan_to_path(plan_list):
    path = ''
    for plan in plan_list:
        action = plan[0]
        direction = action.split('_')[1][0].upper()
        path += direction
    return path

# -------------------------------------------
# Initialize maze
r, c = 15, 15
m=maze(r, c)
m.CreateMaze(theme=COLOR.light, saveMaze=True, loopPercent=100)
position_walls = m.maze_map

a = agent(m, footprints=True)
plan = planner(position_walls, r, c, 1, 1)
path = plan_to_path(plan)

a2 = agent(m, x=r, y=1, footprints=True, shape='arrow')
plan2 = planner(position_walls, r, 1, 1, 1)
path2 = plan_to_path(plan2)

m.tracePath({a:path})
m.tracePath({a2:path2})
m.run()

print(m.maze_map)