def is_uppercase(character):
    if character == character.upper():
        return True


new_data = open("Input.txt").read()
new_position = 0
data = ""

while True:
    temp_data = data
    data, matches = new_data, 0

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

print('String is: {}'.format(new_data))
