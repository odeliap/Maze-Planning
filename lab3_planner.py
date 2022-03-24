# -------------------------------------------
# Libraries
import pyhop

def planner(position_walls, r, c, gr, gc):
    # -------------------------------------------
    # Set start state
    start = pyhop.State('start')
    start.position = (r, c)
    start.walls = position_walls[start.position]
    start.E_wall = position_walls[start.position]['E']
    start.W_wall = position_walls[start.position]['W']
    start.N_wall = position_walls[start.position]['N']
    start.S_wall = position_walls[start.position]['S']
    start.goal = (gr, gc)
    start.visited = []
    start.visited.append(start.position)
    start.exit = False

    # -------------------------------------------
    # Set goal state
    goal = pyhop.State('goal')
    goal.position = (1, 1)
    goal.walls = position_walls[goal.position]
    goal.E_wall = position_walls[goal.position]['E']
    goal.W_wall = position_walls[goal.position]['W']
    goal.N_wall = position_walls[goal.position]['N']
    goal.S_wall = position_walls[goal.position]['S']

    # -------------------------------------------
    # Operators

    def move_north(state, a):
        if state.N_wall == 1:
            prev_position = state.position
            new_row = prev_position[0] - 1
            col = prev_position[1]
            if (new_row, col) not in state.visited:
                state.position = (new_row, col)
                state.visited.append((new_row, col))
                state.E_wall = position_walls[state.position]['E']
                state.W_wall = position_walls[state.position]['W']
                state.N_wall = position_walls[state.position]['N']
                state.S_wall = position_walls[state.position]['S']
                return state
            else:
                return False
        else:
            return False

    def move_south(state, a):
        if state.S_wall == 1:
            prev_position = state.position
            new_row = prev_position[0] + 1
            col = prev_position[1]
            if (new_row, col) not in state.visited:
                state.position = (new_row, col)
                state.visited.append((new_row, col))
                state.E_wall = position_walls[state.position]['E']
                state.W_wall = position_walls[state.position]['W']
                state.N_wall = position_walls[state.position]['N']
                state.S_wall = position_walls[state.position]['S']
                return state
            else:
                return False
        else:
            return False

    def move_east(state, a):
        if state.E_wall == 1:
            prev_position = state.position
            new_col = prev_position[1] + 1
            row = prev_position[0]
            if (row, new_col) not in state.visited:
                state.position = (row, new_col)
                state.visited.append((row, new_col))
                state.E_wall = position_walls[state.position]['E']
                state.W_wall = position_walls[state.position]['W']
                state.N_wall = position_walls[state.position]['N']
                state.S_wall = position_walls[state.position]['S']
                return state
            else:
                return False
        else:
            return False

    def move_west(state, a):
        if state.W_wall == 1:
            prev_position = state.position
            new_col = prev_position[1] - 1
            row = prev_position[0]
            if (row, new_col) not in state.visited:
                state.position = (row, new_col)
                state.visited.append((row, new_col))
                state.E_wall = position_walls[state.position]['E']
                state.W_wall = position_walls[state.position]['W']
                state.N_wall = position_walls[state.position]['N']
                state.S_wall = position_walls[state.position]['S']
                return state
            else:
                return False
        else:
            return False

    pyhop.declare_operators(move_north, move_south, move_east, move_west)
    print('')
    pyhop.print_operators()

    # -------------------------------------------
    # Methods

    def go_north(state, a):
        if state.N_wall == 1:
            return [('move_north', a)]
        else:
            return False

    def go_south(state, a):
        if state.S_wall == 1:
            return [('move_south', a)]
        else:
            return False

    def go_east(state, a):
        if state.E_wall == 1:
            return [('move_east', a)]
        else:
            return False

    def go_west(state, a):
        if state.W_wall == 1:
            return [('move_west', a)]
        else:
            return False

    pyhop.declare_methods('go', go_north, go_south, go_east, go_west)

    def solve_maze(state, a):
        if (state.position[0] == state.goal[0]) and (state.position[1] == state.goal[1]):
            return []
        else:
            return [('go', a), ('solve', a)]

    pyhop.declare_methods('solve', solve_maze)

    # -------------------------------------------
    # Test

    plan = pyhop.pyhop(start, [('solve', 'start')], verbose=1)
    return plan