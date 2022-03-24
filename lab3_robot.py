import time

from pycreate2 import Create2
from lab3_planner import planner

# -----------------------------------------------------
# main

maze_map = {(1,1): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (1,2): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (1,3): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (1,4): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (1,5): {'E': 0, 'W': 0, 'N': 0, 'S': 1}, (1,6): {'E': 0, 'W': 0, 'N': 0, 'S': 0},
            (2,1): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (2,2): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (2,3): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (2,4): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (2,5): {'E': 0, 'W': 0, 'N': 1, 'S': 1}, (2,6): {'E': 0, 'W': 0, 'N': 0, 'S': 0},
            (3,1): {'E': 1, 'W': 0, 'N': 0, 'S': 0}, (3,2): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (3,3): {'E': 1, 'W': 1, 'N': 0, 'S': 1}, (3,4): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (3,5): {'E': 0, 'W': 1, 'N': 1, 'S': 1}, (3,6): {'E': 0, 'W': 0, 'N': 0, 'S': 0},
            (4,1): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (4,2): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (4,3): {'E': 0, 'W': 0, 'N': 1, 'S': 1}, (4,4): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (4,4): {'E': 0, 'W': 0, 'N': 1, 'S': 0}, (4,6): {'E': 0, 'W': 0, 'N': 0, 'S': 0},
            (5,1): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (5,2): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (5,3): {'E': 0, 'W': 0, 'N': 1, 'S': 0}, (5,4): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (5,5): {'E': 0, 'W': 0, 'N': 0, 'S': 0}, (5,5): {'E': 0, 'W': 0, 'N': 0, 'S': 0}}

def go_straight(bot):
    bot.drive_direct(100, 100)
    time.sleep(2.7)

def turn_right(bot):
    bot.drive_direct(-183, 183)
    time.sleep(1.0)

def turn_left(bot):
    bot.drive_direct(183, -183)
    time.sleep(1.0)

if __name__ == "__main__":
    port = '/dev/tty.usbserial-DN0266RJ'
    # instantiate bot
    bot = Create2(port=port)
    # start bot in safe mode
    bot.start()
    bot.safe()

    plan = planner(maze_map, 5, 3, 1, 5)
    print(plan)

    current_direction = 'N'

    for action in plan:
        task = action[0]
        if task == 'move_north':
            print('moving north')
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
            print('moving east')
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
            print('moving south')
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
            print('moving west')
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

    # instantiate song
    song = [72, 12, 20, 24, 67, 12, 20, 24, 64, 24, 69, 16, 71, 16, 69, 16, 68, 24, 70, 24, 68, 24, 67, 12, 65, 12, 67,
            48]
    song_num = 3
    bot.createSong(song_num, song)

    time.sleep(0.1)

    how_long = bot.playSong(song_num)

    bot.drive_stop()

    time.sleep(how_long)