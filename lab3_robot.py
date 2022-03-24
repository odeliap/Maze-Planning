import time

from pycreate2 import Create2
from lab3_planner import planner

# -----------------------------------------------------
# main

maze_map = {(1,1): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (1,2): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (1,3): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (1,4): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (1,5): {'E': 0, 'W': 0, 'N': 0, 'S': 1}, (1,6): {'E': 0, 'W': 0, 'N': 0, 'S': 0},
            (2,1): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (2,2): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (2,3): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (2,4): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (2,5): {'E': 0, 'W': 0, 'N': 1, 'S': 1}, (2,6): {'E': 0, 'W': 0, 'N': 0, 'S': 0},
            (3,1): {'E': 1, 'W': 0, 'N': 0, 'S': 1}, (3,2): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, (3,3): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, (3,4): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, (3,5): {'E': 0, 'W': 1, 'N': 1, 'S': 1}, (3,6): {'E': 0, 'W': 0, 'N': 0, 'S': 0},
            (4,1): {'E': 1, 'W': 0, 'N': 1, 'S': 0}, (4,2): {'E': 1, 'W': 1, 'N': 1, 'S': 0}, (4,3): {'E': 1, 'W': 1, 'N': 1, 'S': 1}, (4,4): {'E': 1, 'W': 1, 'N': 1, 'S': 0}, (4,5): {'E': 0, 'W': 1, 'N': 1, 'S': 1}, (4,6): {'E': 0, 'W': 0, 'N': 0, 'S': 0},
            (5,1): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (5,2): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (5,3): {'E': 0, 'W': 0, 'N': 1, 'S': 1}, (5,4): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (5,5): {'E': 0, 'W': 0, 'N': 1, 'S': 0}, (5,6): {'E': 0, 'W': 0, 'N': 0, 'S': 0},
            (6,1): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (6,2): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (6,3): {'E': 0, 'W': 0, 'N': 1, 'S': 0}, (6,4): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (6,5): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (6,6): {'E': 0, 'W': 0, 'N': 0, 'S': 0}}

def go_straight(bot):
    bot.drive_direct(30, 30)
    time.sleep(1.0)
    bot.drive_stop()

def turn_right(bot):
    bot.drive_direct(30, -30)
    time.sleep(1.0)
    bot.drive_stop()

def turn_left(bot):
    bot.drive_direct(-30, 30)
    time.sleep(1.0)
    bot.drive_stop()

if __name__ == "__main__":
    port = '/dev/tty.usbserial-DN026A6A'
    # instantiate bot
    bot = Create2(port=port)
    # start bot in safe mode
    bot.start()
    bot.safe()

    plan = planner(maze_map, 6, 3, 1, 5)
    print(plan)

    current_direction = 'N'

    for task in plan[0]:
        if task == 'move_north':
            if current_direction == 'N':
                pass
            elif current_direction == 'E':
                turn_left(bot)
            elif current_direction == 'S':
                turn_right(bot)
                turn_right(bot)
            elif current_direction == 'W':
                turn_right(bot)
            go_straight(bot)
            current_direction = 'N'
        elif task == 'move_east':
            if current_direction == 'N':
                turn_right(bot)
            elif current_direction == 'E':
                pass
            elif current_direction == 'S':
                turn_left(bot)
            elif current_direction == 'W':
                turn_right(bot)
                turn_right(bot)
            go_straight(bot)
            current_direction = 'E'
        elif task == 'move_south':
            if current_direction == 'N':
                turn_right(bot)
                turn_right(bot)
            elif current_direction == 'E':
                turn_right(bot)
            elif current_direction == 'S':
                pass
            elif current_direction == 'W':
                turn_left(bot)
            go_straight(bot)
            current_direction = 'S'
        elif task == 'move_west':
            if current_direction == 'N':
                turn_left(bot)
            elif current_direction == 'E':
                turn_right(bot)
                turn_right(bot)
            elif current_direction == 'S':
                turn_right(bot)
            elif current_direction == 'W':
                pass
            go_straight(bot)
            current_direction = 'W'