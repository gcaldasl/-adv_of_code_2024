import re

## TRIED TO DO WITH PURE DSA, FAILED MISERABLY, resorted to regex.
def extract_truthy_multiplications_from_input(input_text):
    unlisted_text = "".join(input_text)
    matches = re.findall(r"mul\((\d+),(\d+)\)", unlisted_text)

    return matches

def read_only_valid_multiplications(input_file):
    with open(input_file, 'r') as f:
        full_text = [text.strip() for text in f.readlines()]

    values_list = extract_truthy_multiplications_from_input(full_text)

    total_multiplication = 0

    for number in values_list:
        total_multiplication += int(number[0]) * int(number[1])

    return total_multiplication

print(read_only_valid_multiplications('input.txt'))