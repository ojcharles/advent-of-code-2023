# day1 - task1 - result 53921 - 8.1532 ms
# day1 - task2 - result 54676 - 8.8811 ms
# a - treat as single string
'''
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
'''

from re import findall
import time

def string2int_sum(string) -> int:
    int_list = findall('[0-9]', string)
    num_ints = len(int_list)
    if num_ints == 1:
        int_sum = int(int_list[0] + int_list[0])
    else:
        int_sum = int( int_list[0] + int_list[num_ints-1] )
    return(int_sum)

def intstr2int(line: str) -> str:
    #line = 'eightseventhree7lfqpnclxnnineninemgkjtqksrdone'
    intstr2int_dict = {'eightwo': '82', 'eighthree': '83', 
                       'oneight':'18', 'twone':'21', 'threeight':'38', 'fiveight':'58', 'nineight':'98',
                       'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for intstr, int in intstr2int_dict.items():
        line = line.replace(intstr, int)
    return(line)

def task1():
    start_time = time.time()
    int_sum_across_lines = 0
    file = open('day1/input.txt', 'r')
    lines = file.readlines()
    for line in lines:
        line_intsum = string2int_sum(line)
        int_sum_across_lines = int_sum_across_lines + line_intsum
    runtime = round( (time.time() - start_time) * 1000 ,4)
    print("day1 - task1 - result {} - {} ms".format(int_sum_across_lines, runtime) )

def task2():
    start_time = time.time()
    int_sum_across_lines = 0
    file = open('day1/input.txt', 'r')
    lines = file.readlines()
    mystr = '\t'.join([line.strip() for line in lines])
    mystr = intstr2int(mystr)
    lines = mystr.split('\t')
    for line in lines:
        line_intsum = string2int_sum(line)
        int_sum_across_lines = int_sum_across_lines + line_intsum
    runtime = round( (time.time() - start_time) * 1000 ,4)
    print("day1 - task2 - result {} - {} ms".format(int_sum_across_lines, runtime) )

if __name__ == '__main__':
    task1()
    task2()