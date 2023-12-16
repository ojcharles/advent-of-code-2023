# day2 - task1 - result 2176 - 5.9433 ms
# day2 - task2 - result 63700 - 14.0369 ms
import time
import re

start_time = time.time()

def task1():
    # which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
    file = open('day2/input.txt', 'r')
    lines = file.readlines()
    legal_game_id_sum = 0
    for game_id, line in enumerate(lines):
        red_cubes = re.findall('[0-9]{1,2}(?= red)',line)
        red_cubes = list(map(int, red_cubes))
        red_illegal = any(i > 12 for i in red_cubes)
        if red_illegal:
            continue

        green_cubes = re.findall('[0-9]{1,2}(?= green)',line)
        green_cubes = list(map(int, green_cubes))
        green_illegal = any(i > 13 for i in green_cubes)
        if green_illegal:
            continue

        blue_cubes = re.findall('[0-9]{1,2}(?= blue)',line)
        blue_cubes = list(map(int, blue_cubes))
        blue_illegal = any(i > 14 for i in blue_cubes)
        if blue_illegal:
            continue
        # remaining must be legal games - +1 as enumerate starts at 1
        legal_game_id_sum = legal_game_id_sum + game_id + 1

    runtime = round( (time.time() - start_time) * 1000 ,4)
    print("day2 - task1 - result {} - {} ms".format(legal_game_id_sum, runtime) )


def task2():
    # in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
    file = open('day2/input.txt', 'r')
    lines = file.readlines()
    sum_of_power_of_cubes = 0
    for game_id, line in enumerate(lines):
        red_cubes = re.findall('[0-9]{1,2}(?= red)',line)
        red_cubes = list(map(int, red_cubes))
        red_min = max(red_cubes)

        green_cubes = re.findall('[0-9]{1,2}(?= green)',line)
        green_cubes = list(map(int, green_cubes))
        green_min = max(green_cubes)

        blue_cubes = re.findall('[0-9]{1,2}(?= blue)',line)
        blue_cubes = list(map(int, blue_cubes))
        blue_min = max(blue_cubes)

        power_of_cubes = red_min * green_min * blue_min
        sum_of_power_of_cubes = sum_of_power_of_cubes + power_of_cubes

    runtime = round( (time.time() - start_time) * 1000 ,4)
    print("day2 - task2 - result {} - {} ms".format(sum_of_power_of_cubes, runtime) )

if __name__ == '__main__':
    task1()
    task2()