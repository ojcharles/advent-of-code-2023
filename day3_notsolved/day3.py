import time

start_time = time.time()
file = open('day3/input.txt', 'r')
lines = file.readlines()
num_col = len(lines[0]) + 2
num_lines = len(lines)

# approach will be:
# 1 -  to identify contiguous integers along a line, concatenate, and keep track of position, done per line
# 2 - then see if any illegal characters within 1 char around inc diagonal

# PADDING - add a pre and post line , as well as padding all lines by one char
lines = ['.'+line+'.' for line in lines]
lines.insert(0,'.' * num_col)
lines.append('.' * num_col)

part_number_list = []
# skip padding lines
for line_index in range(1,num_lines+1):
    part_start_pos = 0
    part_end_pos = 0
    for x, c in enumerate(lines[line_index]):
        if(not c.isdigit() and part_start_pos == 0):
            continue
        if(c.isdigit()):
            if(part_start_pos == 0):
                part_start_pos = x
                part_end_pos = x
            else:
                part_end_pos = x
        if(not c.isdigit() and part_start_pos != 0):
            # now we have a number
            current_int_value = int(lines[line_index][part_start_pos:part_end_pos+1])
            #print('Assesing ' + str(part_start_pos) + ' '+ str(part_end_pos) + ' ' + str(current_int_value))
            #is it legitimate? - surrounded by a characters
            current_int_legal = False
            # define a bounding box
            for bb_line_index in [line_index-1, line_index, line_index + 1]:
                for bb_x, bb_char in enumerate(lines[bb_line_index][part_start_pos-1:part_end_pos+2]):
                    if bb_char not in ['0','1','2','3','4','5','6','7','8','9','.']:
                        current_int_legal = True
            if current_int_legal == True:
                part_number_list.append(current_int_value)
                print(current_int_value)
            #print(str(current_int_value) + ' ' + str(current_int_legal) )
            part_start_pos = 0
            part_end_pos = 0

part_numbers_sum = sum(part_number_list)
runtime = round( (time.time() - start_time) * 1000 ,4)
print("day3 - task1 - result {} - {} ms".format(part_numbers_sum, runtime) )

