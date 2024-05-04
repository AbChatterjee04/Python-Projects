import random
def player_guess(x):
    guess_num = random.randint(1,x)
    count = 0
    while True:
        guess = int(input(f'Chose num between 1-{x}: '))

        if guess_num > guess:
            print('Go low')

        elif guess_num < guess:
            print('Go Higher')

        count +=1
    print(f'Yay you got it it\'s {guess_num}, you took {count} chances')

player_guess(100)