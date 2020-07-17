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
            value = 6    
            return value
        elif select == 2:
            value = 4
            return value
        elif select == 3:
            value = 2
            return value

def guess_game():
    while True:
        print('RANGE -> 1 TO 100')
        rand_no = random.randint(1, 100)
        attempt = int(level())
        if attempt == 0:
            break
        while attempt > 0:
            print('\tYou hav:', attempt, 'Attempts Left')
            if attempt == 1:
                print('\t...LAST ATTEMPT!...')
            guess = input('Guess the Number: ')
            try:
                guess = int(guess)
            except:
                print('\tINVALID CHOICE.\n\tTRY AGAIN.\n')
                continue

            if guess == rand_no:
                print('\tBANG ON..! YOU GUESSED IT RIGHT')
                print('Total Attempts Remaining:', attempt - 1)
                break
            elif (guess > rand_no) and (guess <= 100):
                compute = guess - rand_no
                if compute <= 3:
                    print('\tHIGH BUT CLOSE')
                else:
                    print('\tHIGH')
            elif (guess < rand_no) and (guess >= 1):
                compute = rand_no - guess
                if compute <= 3:
                    print('\tLOW BUT CLOSE')
                else:
                    print('\tCLOSE')
            else:
                print('\tOUT OF RANGE.\n\tTRY AGAIN.')
                break
            attempt = attempt - 1
            if attempt == 0:
                print('Out of Attempts...OOPS!')
                print('\tNumber was:', rand_no, '\n')

# uncomment to run the code.
# guess_game()

