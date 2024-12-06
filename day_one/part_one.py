def get_difference_sum_of_two_location_ids(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
        split_lines = []
        for line in lines:
            line_ids = [id.strip() for id in line.split()]
            split_lines.append(line_ids)

    col1 = []
    col2 = []

    for ids in split_lines:
        col1.append(int(ids[0]))
        col2.append(int(ids[1]))

    col1.sort()
    col2.sort()

    difference_sum = 0

    while col1 and col2:
        diff = abs(col1.pop(0) - col2.pop(0))
        difference_sum += diff
    
    return difference_sum

print(get_difference_sum_of_two_location_ids("input.txt"))