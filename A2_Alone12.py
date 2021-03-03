from collections import Counter


def print_each_storm(prev_list_func):
    if len(prev_list_func) == 0:
        prev_list_func = values_on_line  # 儲存第一筆資料
    if int(prev_list_func[6]) >= int(values_on_line[6]):
        print_list_func = prev_list_func
    else:
        print_list_func = prev_list_func = values_on_line
    if values_on_line[2] == 'L' and int(values_on_line[6]) >= 64:
        print_list_func.append("Y")
    return print_list_func


def sum_storm(count):
    year_tuple = []
    cat1 = cat2 = cat3 = cat4 = cat5 = 0
    for a_tuple in count:
        year_tuple.append(a_tuple[0][4:8])
        msw = int(a_tuple[3])
        if 64 <= msw <= 82:
            cat1 += 1
        elif 83 <= msw <= 95:
            cat2 += 1
        elif 96 <= msw <= 112:
            cat3 += 1
        elif 113 <= msw <= 136:
            cat4 += 1
        elif msw >= 137:
            cat5 += 1
    print(Counter(year_tuple))


with open('Atlantic.txt', 'r') as f:
    prev_list = print_list = counter_list = []
    i = 1
    for line in f:  # reads ONLY ONE line from the file, and stops when hits end of file.

        line = line.replace('\n', '')
        values_on_line = [x.strip() for x in
                          line.split(',')]  # Split string at spaces into list of "words" which are number strings.

        if str(values_on_line[0])[:2] == 'AL':
            storm_line_num = int(str(values_on_line[2]))
            storm_id = values_on_line[0]
            storm_id = storm_id + ' ' + values_on_line[1] if values_on_line[1] != 'UNNAMED' else storm_id
            i = 1

            continue

        # read values_on_line[2] 行的資料（作為一個）storm
        if i < storm_line_num:
            print_list = print_each_storm(prev_list)
        elif i == storm_line_num:
            print_list = print_each_storm(prev_list)
            # print
            input_list = storm_id, print_list[0], print_list[1], print_list[6], print_list[-1]
            print(input_list)
            counter_list.append(input_list)
            prev_list = print_list = []
        i += 1
#sum_storm(counter_list)

with open('Pacific.txt', 'r') as f:
    prev_list = print_list = counter_list = []
    i = 1
    for line in f:  # reads ONLY ONE line from the file, and stops when hits end of file.

        line = line.replace('\n', '')
        values_on_line = [x.strip() for x in
                          line.split(',')]  # Split string at spaces into list of "words" which are number strings.

        if str(values_on_line[0])[:2] == 'EP':
            storm_line_num = int(str(values_on_line[2]))
            storm_id = values_on_line[0]
            storm_id = storm_id + ' ' + values_on_line[1] if values_on_line[1] != 'UNNAMED' else storm_id
            i = 1
            continue

        # read values_on_line[2] 行的資料（作為一個）storm
        if i < storm_line_num:
            print_list = print_each_storm(prev_list)
        elif i == storm_line_num:
            print_list = print_each_storm(prev_list)

            # print
            input_list = storm_id, print_list[0], print_list[1], print_list[6], print_list[-1]
            print(input_list)
            counter_list.append(input_list)
            prev_list = print_list = []
        i += 1