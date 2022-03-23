from pyamaze import maze, COLOR, agent
import pyhop

r, c = 10, 10

# -------------------------------------------
# Initialize maze
m=maze(r, c)
m.CreateMaze(theme=COLOR.light, saveMaze=True)
a = agent(m, footprints=True)
m.tracePath({a:m.path})
m.run()

def plan_to_path(plan_list):
    path = ''
    for plan in plan_list:
        action = plan[0]
        direction = action.split('_')[1][0].upper()
        path += direction
    return path

