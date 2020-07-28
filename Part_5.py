# Write a Python Game ->
# Guess the NUmber and Check your Luck.

import random

def level():
    while True:
        print('\n\t5. Guessing the Number Game')
        print('\nEnter \'-1\' to GO BACK.')
        print('1. EASY')
        print('2. MEDIUM')
        print('3. EXTREME')
        try:
            select = int(input('Choose Difficulty - '))
        except:
            # if user enters anything other than an integer, the below message pops up
            print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
            continue
        if select == -1:
            # exit condition
            print('\tTHANK YOU.\n\tRETURNING TO MAIN MENU.\n')
            value = 0
            # return value
        elif select == 1:
            value = 7    
            # return value
        elif select == 2:
            value = 5
            # return value
        elif select == 3:
            value = 3
            # return value
        else:
            print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
            continue
        return value


def guess_game():
    while True:
        rand_no = random.randint(1, 100)
        attempt = int(level())
        if attempt == 0:
            break
        print('\nRANGE -> 1 TO 100\n')
        # explaining the terms used in the program ahead.
        print('\tGuess is HIGH BUT CLOSE -> Guessed Number is Higher than Expected but in range of 5.')
        print('\tGuess is HIGH \t\t-> Guessed Number is Higher than Expected but in range of 20.')
        print('\tGuess is TOO HIGH \t-> Guessed Number is Higher than Expected but beyond the range of 20.')
        print('\tGuess is LOW BUT CLOSE  -> Guessed Number is Lower than Expected but in range of 5.')
        print('\tGuess is LOW \t\t-> Guessed Number is Lower than Expected but in range of 20.')
        print('\tGuess is TOO LOW \t-> Guessed Number is Lower than Expected but beyond the range of 20.')
        while attempt > 0:
            print('\n\tYou have:', attempt, 'Attempts Left\n')
            if attempt == 1:
                # to alert the user
                print('\t...LAST ATTEMPT!...\n')
            try:
                guess = int(input('Guess the Number -  '))
            except:
                # if user enters anything other than an integer, the below message pops up
                print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
                continue
            if guess < 1 or guess > 100:
                print('\tOUT OF RANGE.\n\tTRY AGAIN.')
                continue
            if guess == rand_no:
                print('\n\tBANG ON..! YOU GUESSED IT RIGHT')
                print('\tTotal Attempts Remaining:', attempt - 1)
                break
            elif (guess > rand_no) and (guess <= 100):
                compute = guess - rand_no
                if compute <= 5:
                    print('\tGuess is HIGH BUT CLOSE')
                elif compute <= 20:
                    print('\tGuess is HIGH')
                else:
                    print('\tGuess is TOO HIGH')
            elif (guess < rand_no) and (guess >= 1):
                compute = rand_no - guess
                if compute <= 5:
                    print('\tGuess is LOW BUT CLOSE')
                elif compute <= 20:
                    print('\tGuess is LOW')
                else:
                    print('\tGuess is TOO LOW')
            
            attempt = attempt - 1
            if attempt == 0:
                print('\nOut of Attempts...OOPS!')
                print('\tNumber was ->', rand_no)

# uncomment to run the code.
# guess_game()