import pyhop
from pycreate2 import Create2

# -----------------------------------------------------
# operators

def drive_to_wall(state, a):
    if state.wall[a] == False:
        state.wall[a] = True
        return state
    else: return False

def rotate_from_wall(state, a):
    if state.wall[a] == True:
        state.wall[a] = False
        return state
    else: return False

pyhop.declare_operators(drive_to_wall, rotate_from_wall)
print('')
pyhop.print_operators()


# -----------------------------------------------------
# methods

def go_to_wall(state,a):
    if state.wall == False:
        return [('drive_to_wall',a), ('rotate_from_wall',a)]
    elif state.wall == True:
        return [('rotate_from_wall',a)]
    else: return False

pyhop.declare_methods('go_to_wall', go_to_wall)
print('')
pyhop.print_methods()


state1 = pyhop.State('state1')
state1.wall = False

pyhop.pyhop(state1,[('go_to_wall','bot')],verbose=1)

state2 = pyhop.State('state2')
state2.wall = True

pyhop.pyhop(state2,[('go_to_wall','bot')],verbose=1)


# -----------------------------------------------------
# functions

def get_state(state, bot):
    # get light sensor reading (True/False)
    sensors = bot.get_sensors()
    light_bumpers = sensors.light_bumper

    # if front light sensor(s) are True (i.e. wall detected in front)
    # set wall state to True
    if light_bumpers.front_left or light_bumpers.front_right:
        state.wall = True
    # otherwise set it to False
    else:
        state.wall = False
    return state


def drive_straight(state, bot):
    # while wall is not detected
    while not state.wall:
        # go straight
        bot.drive_direct(50, 50)
        # check for wall
        state = get_state(state, bot)
    # stop once wall detected
    bot.drive_stop()
    return state

def rotate_away(state, bot):
    # while wall is detected
    while state.wall == True:
        # rotate away (turn right)
        bot.drive_direct(-50, 50)
        # check for wall
        state = get_state(state, bot)
    # exit loop once wall not detected
    bot.drive_stop()
    return state

# -----------------------------------------------------
# main

if __name__ == "__main__":
    port = '/dev/tty.usbserial-DN026A6A'
    # instantiate bot
    bot = Create2(port=port)
    # start bot in safe mode
    bot.start()
    bot.safe()

    state = pyhop.State('state')
    wall_state = get_state(state, bot)

    plan = pyhop.pyhop(state,[('go_to_wall','bot')],verbose=3)

    for task in plan[0]:
        if task == 'drive_to_wall':
            state = drive_straight(state, bot)
        elif task == 'rotate_from_wall':
            state = rotate_away(state, bot)
