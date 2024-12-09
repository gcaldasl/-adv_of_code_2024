def check_if_each_sequence_is_valid(sequence):
    if not sequence or len(sequence) == 1:
        return True

    is_increasing = sequence[0] < sequence[1]

    for i in range(len(sequence) - 1):
        diff = sequence[i + 1] - sequence[i]

        if not (0 < abs(diff) <= 3):
            return False

        if is_increasing and sequence[i] >= sequence[i + 1]:
            return False
        elif not is_increasing and sequence[i] <= sequence[i + 1]:
            return False

    return True

def check_with_damp(sequence):
    if check_if_each_sequence_is_valid(sequence):
        return True

    for i in range(len(sequence)):
        damped_sequence = sequence[:i] + sequence[i + 1:]
        if check_if_each_sequence_is_valid(damped_sequence):
            return True

    return False

def check_red_nose_reactor(input_file):
  with open(input_file, 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    array_of_nums = [list(map(int, line.split())) for line in lines]

  return sum(1 for seq in array_of_nums if check_with_damp(seq))

print(check_red_nose_reactor('input.txt'))