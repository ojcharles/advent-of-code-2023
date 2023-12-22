import re
import math
from numba import jit
##### Task 1
DIGITS = r"\d+"
def read_input(path: str) -> list:
    with open(path) as f:
        return [line.strip() for line in f if not line.isspace()]

lines = read_input('day6/input.txt')
times = list(map(int, re.findall(DIGITS, lines[0])))
records = list(map(int, re.findall(DIGITS, lines[1])))


def inputs2numwins(times: list, records: list) -> list:
    number_of_ways_to_win = []
    for iter in range(len(times)):
        iter_win_nums = 0
        time = times[iter]
        dist = records[iter]
        for t_iter in range(0,time+1):
            speed = t_iter
            time_left = time - t_iter
            dist_covered = speed * time_left
            #print(f'{iter}: time held:{t_iter} - dist covered {dist_covered}')
            if dist_covered >= dist:
                iter_win_nums +=1
        number_of_ways_to_win.append(iter_win_nums)
    return(number_of_ways_to_win)

nwins = inputs2numwins(times, records)
print(math.prod(nwins))


##### Task2
times = [int("".join(re.findall(DIGITS, lines[0])))]
records = [int("".join(re.findall(DIGITS, lines[1])))]
nwins = inputs2numwins(times, records)
print(math.prod(nwins))
