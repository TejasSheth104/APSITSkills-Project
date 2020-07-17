import random

while True:
    print('-1 to exit')
    guess = input('Enter a Number - ')
    try:
        guess = int(guess)
    except:
        print()
        break

    rand_no = random.randint(1, 10)
    if guess == rand_no:
        print('BANG ON..! YOU GUESSED IT RIGHT')
    elif guess > rand_no:
        if guess - rand_no <= 3:
            print('Guess is Higher in range of 3.')
        else:
            print('Guess is Higher in Outside the range of 3.')
    elif guess < rand_no:
        if rand_no - guess <= 3:
            print('Guess is Lower in range of 3.')
        else:
            print('Guess is Lower in Outside the range of 3.')
    print(rand_no)


# # # need to import random library
# # notify the user if their number is too high too low or close
# # number shld be in range 0 to 20
# # 1 end

# # 1st Mini-project
# import random


# def level():
#     val = ''
#     print('Press 1. for EASY')
#     print('Press 2. for MEDIUM')
#     print('Press 3. for EXTREME')
#     val = input('Choose Difficulty: ')
#     try:
#         val = int(val)
#     except:
#         print('Try Again.')
#         exit(0)
#     if val == 1:
#         val = 10    # 6
#         return val
#     elif val == 2:
#         val = 5     # 4
#         return val
#     elif val == 3:
#         val = 3     # 2
#         return val


# rand_no = random.randint(1, 100)
# attempt = int(level())
# while attempt > 0:
#     print('You hav:', attempt, 'Attempts')
#     if attempt == 1:
#         print('Last Shot at GLORY...')
#     guess = input('Guess the Number: ')
#     try:
#         guess = int(guess)
#     except:
#         print('Try Again.')
#         exit(0)
# # can use try and except, else traceback
#     if guess == rand_no:
#         print('BANG ON..! YOU GUESSED IT RIGHT')
#         print('Total Attempts Remaining:', attempt - 1)
#         break
#     elif (guess > rand_no) and (guess <= 100):
#         compute = guess - rand_no
#         if compute <= 3:
#             print('high & close')
#         else:
#             print('high')
#     elif (guess < rand_no) and (guess >= 1):
#         compute = rand_no - guess
#         if compute <= 3:
#             print('low & close ')
#         else:
#             print('low')
#     else:
#         print('Out of Range \n')
#         break
#     attempt -= 1
#     if attempt == 0:
#         print('Out of Attempts...OOPS!')
#         print('Number was:', rand_no, '\n')

# print('Exit')
