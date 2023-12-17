
import time
start_time = time.time()

file = open('day4/input.txt', 'r')
lines = file.readlines()

#line = 'Card   1: 17 15  5 75 36 13 16 66 92 39 | 13 92 16  5 87 78 15 94 21 48 30 62 70 41  3 39 22 17 77 58 75 52 83 34 24'

def card_line2successes(line):
    line2 = line[10:].replace('\n','')
    line2 = line2.split('|')
    winning_nums = line2[0].split(' ')
    winning_nums = set([value for value in winning_nums if value != ''])
    my_nums = line2[1].split(' ')
    my_nums = set([value for value in my_nums if value != ''])
    game_successes = len(my_nums.intersection(winning_nums))
    return(game_successes)

total_scratchcard_score = 0
for card_iter, line in enumerate(lines):
    game_successes = card_line2successes(line)
    game_score = 1 * (2 ** (game_successes -1) )
    if(game_score==0.5):
        game_score = 0
    #print(game_score)
    total_scratchcard_score = total_scratchcard_score + game_score

runtime = round( (time.time() - start_time) * 1000 ,4)
print("day4 - task1 - result {} - {} ms".format(total_scratchcard_score, runtime) )

# part2
# tot up number of originals and copies - always 1 of each card
start_time = time.time()

scratchcard_copies = [1] * len(lines)
for card_iter, line in enumerate(lines):
    #card_iter = 2
    #line = lines[card_iter]
    game_successes = card_line2successes(line)
    copies_of_card_total = scratchcard_copies[card_iter]
    scratchcard_copies [card_iter + 1 : card_iter + 1 + game_successes] = [x+copies_of_card_total for x in scratchcard_copies [card_iter + 1 : card_iter + 1 + game_successes] ]
    #print(scratchcard_copies)

runtime = round( (time.time() - start_time) * 1000 ,4)
print("day4 - task2 - result {} - {} ms".format(sum(scratchcard_copies), runtime) )
