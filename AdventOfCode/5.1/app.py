def is_uppercase(character):
    if character == character.upper():
        return True


data = open("Input.txt").read()
not_found = True
while not_found:
    for position in range(0, data.__sizeof__()):
        if data[position] == data[position].upper():
            if data[position + 1] == data[position].lower():
                print("hej")
        elif data[position + 1] == data[position].upper():
            print("hoj")
