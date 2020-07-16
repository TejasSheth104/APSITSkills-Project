# Write a Python program to test whether a passed letter is a vowel or not.

import string

def vowel_consonant():
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    alphabets = string.ascii_lowercase

    while True:
        print('\nEnter \'-1\' to QUIT.')
        letter = input('Enter a letter - ')
    
        if letter == '-1':
            print('\tTHANK YOU.\n\tRETURNING TO MAIN MENU.\n')
            break
        elif (len(letter) != 1) or (letter not in alphabets):
            print('\t1 LETTER EXCEPTED\n\tTRY AGAIN.\n')
            continue
    
        letter = letter.lower()
        if letter in vowels:
            print('Letter', letter.upper(), '- is a VOWEL')
        elif letter in consonants:
            print('Letter', letter.upper(), '- is NOT a VOWEL')
        else:
            print('\tInValid INPUT.\n\tTRY AGAIN.\n')
            continue

# uncomment to run the code.
# vowel_consonant()
