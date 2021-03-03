
def print_func(loc):
    prev_list = print_list = []
    i = 1
    for line in f:  # reads ONLY ONE line from the file, and stops when hits end of file.
        line = line.replace('\n', '')
        values_on_line = [x.strip() for x in line.split(',')]

        if str(values_on_line[0])[:2] == loc:
            storm_line_num = int(str(values_on_line[2]))
            storm_id = values_on_line[0]
            storm_id = storm_id + ' ' + values_on_line[1] if values_on_line[1] != 'UNNAMED' else storm_id
            i = 1
            continue

        if i < storm_line_num:
            if len(prev_list) == 0:
                prev_list = values_on_line
            if int(prev_list[6]) >= int(values_on_line[6]):
                print_list = prev_list
            else:
                print_list = prev_list = values_on_line
            if values_on_line[2] == 'L' and int(values_on_line[6]) >= 64:
                print_list.append("Y")
        elif i == storm_line_num:
            if len(prev_list) == 0:
                prev_list = values_on_line
            if int(prev_list[6]) >= int(values_on_line[6]):
                print_list = prev_list
            else:
                print_list = prev_list = values_on_line
            if values_on_line[2] == 'L' and int(values_on_line[6]) >= 64:
                print_list.append("Y")
            # print
            input_list = storm_id, print_list[0], print_list[1], print_list[6], print_list[-1]
            print('ID: {:>20} Date: {:>8} Time: {:>4} Maximum sustained wind: {:>3} Landfall: {}'.format(storm_id,
                                                                                                         print_list[0],
                                                                                                         print_list[1],
                                                                                                         print_list[6],
                                                                                                         print_list[
                                                                                                             -1]))
            counter_list.append(input_list)
            prev_list = print_list = []
        i += 1


def add_count(storm_dict, year, msw):
    storm_dict[year][0] += 1

    if 64 <= msw <= 82:
        storm_dict[year][1] += 1

    elif 83 <= msw <= 95:
        storm_dict[year][2] += 1

    elif 96 <= msw <= 112:
        storm_dict[year][3] += 1

    elif 113 <= msw <= 136:
        storm_dict[year][4] += 1

    elif msw >= 137:
        storm_dict[year][5] += 1


def sum_storm(count):
    cat1 = cat2 = cat3 = cat4 = cat5 = 0
    storm_dict = {}

    for a_tuple in count:
        year = a_tuple[0][4:8]
        msw = int(a_tuple[3])

        if year in storm_dict:
            add_count(storm_dict, year, msw)
        else:
            storm_dict[year] = []
            storm_dict[year].append(0)
            storm_dict[year].append(cat1)
            storm_dict[year].append(cat2)
            storm_dict[year].append(cat3)
            storm_dict[year].append(cat4)
            storm_dict[year].append(cat5)
            add_count(storm_dict, year, msw)
    print('\nYear Storms Cat1 Cat2 Cat3 Cat4 Cat5')
    for key, value in storm_dict.items():
        print('{:.4} {:>6} {:>4} {:>4} {:>4} {:>4} {:>4}'.format(key, value[0], value[1], value[2], value[3], value[4],
                                                                 value[5]))


with open('Atlantic.txt', 'r') as f:
    counter_list = []
    print_func('AL')

with open('Pacific.txt', 'r') as f:
    print_func('EP')
