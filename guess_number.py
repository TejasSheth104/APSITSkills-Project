import random

def level():
    while True:
        print('\nEnter \'-1\' to QUIT.')
        print('Press 1. for EASY')
        print('Press 2. for MEDIUM')
        print('Press 3. for EXTREME')
        select = input('Choose Difficulty - ')
        try:
            select = int(select)
        except:
            print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
            continue
        if select == -1:
            # exit condition
            print('\tTHANK YOU.\n\tRETURNING TO MAIN MENU.\n')
            value = 0
            return value
        if select == 1:
            value = 7    
            return value
        elif select == 2:
            value = 5
            return value
        elif select == 3:
            value = 3
            return value

def guess_game():
    while True:
        rand_no = random.randint(1, 100)
        attempt = int(level())
        if attempt == 0:
            break
        print('\nRANGE -> 1 TO 100\n')
        print('\tGuess is HIGH BUT CLOSE -> Guessed Number is Higher than Expected but in range of 5.')
        print('\tGuess is HIGH -> \tGuessed Number is Higher than Expected but in range of 20.')
        print('\tGuess is TOO HIGH -> \tGuessed Number is Higher than Expected but beyond the range of 20.')
        print('\tGuess is LOW BUT CLOSE -> Guessed Number is Lower than Expected but in range of 5.')
        print('\tGuess is LOW -> \tGuessed Number is Lower than Expected but in range of 20.')
        print('\tGuess is TOO LOW -> \tGuessed Number is Lower than Expected but beyond the range of 20.')
        while attempt > 0:
            print('\n\tYou have:', attempt, 'Attempts Left\n')
            if attempt == 1:
                print('\t...LAST ATTEMPT!...\n')
            guess = input('Guess the Number -  ')
            try:
                guess = int(guess)
            except:
                print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
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
            else:
                print('\tOUT OF RANGE.\n\tTRY AGAIN.')
                break
            attempt = attempt - 1
            if attempt == 0:
                print('\nOut of Attempts...OOPS!')
                print('\tNumber was ->', rand_no)

# uncomment to run the code.
guess_game()

