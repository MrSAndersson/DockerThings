import string


def is_uppercase(character):
    if character == character.upper():
        return True


def collapse(new_data):
    new_position = 0
    data = ""

    while True:
        data = new_data

        if new_position != 0:
            new_data = data[:new_position]
        else:
            new_data = ""

        for position in range(new_position, len(data) - 1):
            if position == len(data) - 2:
                new_data += data[position:]
                break
            if data[position] == data[position + 1]:
                new_data += data[position]
            elif data[position].lower() == data[position + 1] or data[position].upper() == data[position + 1]:
                new_data += data[position + 2:]
                break
            else:
                new_data += data[position]

        if (position == len(data) - 2):
            break
        if 0 < position:
            new_position = position - 1
    return new_data


def remove_unit(data, unit):
    out_data = ""
    for char in data:
        if char.lower() != unit:
            out_data += char
    return out_data


data = open("Input.txt").read()

for unit in string.ascii_lowercase:
    cleaned_data = remove_unit(data, unit)
    collapsed_data = collapse(cleaned_data)
    if 'shortest_count' in locals():
        if len(collapsed_data) < shortest_count:
            shortest_count = len(collapsed_data)
            shortest_unit = unit
    else:
        shortest_count = len(collapsed_data)
        shortest_unit = unit

print('String is: {} units long by removing unit: {}'.format(
    shortest_count, shortest_unit))
