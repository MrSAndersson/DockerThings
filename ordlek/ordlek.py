import os
import random


with open('letters.txt') as file:
    vowels = file.readline()
    consonants = file.readline()

letters = ''

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print('Bokstäver ({}): '.format(len(letters)) + letters)
    print('Vokal (v), konsonant (k) eller omstart (r)?: ', end='')
    choice = input()

    if choice == 'v':
        letters += random.choice(vowels)
    if choice == 'k':
        letters += random.choice(consonants)
    if choice == 'r':
        letters = ''
