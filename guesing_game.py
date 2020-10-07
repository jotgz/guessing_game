import random
import os

choice_list = list(range(1,21))
random_choice = random.choice(choice_list)
guess_counter = 0


def game(): 
    '''
    Grab user input and compare to random choice

    Verifies that user input matches random choice
    '''

    # Clears output for new game
    def clear():
        os.system( 'cls' )

    global choice_list
    global random_choice
    global guess_counter

    user_guess = int(input('Guess a number from 1 - 20 '))

    if user_guess < random_choice:
        guess_counter += 1
        print('Number too low, go higher!')
        game()

    elif user_guess > random_choice:
        guess_counter +=1
        print('Number too high, go lower!')
        game()

    elif user_guess == random_choice:
        guess_counter += 1
        if guess_counter == 1:
            print('Congratulations!! You got in on your first try')
        else: 
            print(f'You guessed the number in {guess_counter} tries! Play again for a better score!')
            random_choice = random.choice(choice_list)
            guess_counter = 0

            verify = input('Do you want to play again? Type Y or N').upper()
            if verify == 'Y':
                print('Let\'s play again!')  
                clear()             
                game()
            else:
                print('Thanks for playing!!!')

game()
