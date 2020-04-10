vowels = 'AEIOUYÅÄÖ'
consonants = 'BCDFGHJKLMNPQRSTVWXZ'

vowels_out = ''
consonants_out = ''

with open('input.txt') as file:
    for line in file:
        for char in line:
            if char.upper() in vowels:
                vowels_out += char.upper()
            if char.upper() in consonants:
                consonants_out += char.upper()

vowels_out += '\n'
consonants_out += '\n'

with open('letters.txt', 'w') as outfile:
    outfile.write(vowels_out)
    outfile.write(consonants_out)
