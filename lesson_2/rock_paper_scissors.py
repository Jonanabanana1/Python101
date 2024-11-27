import random

VALID_CHOICES = ['rock', 'paper', 'scissors']


def display_result(choice, computer_choice):
    if ((choice == 'rock') and (computer_choice == 'scissors') or
        (choice == 'paper') and (computer_choice == 'rock') or
            (choice == 'scissors') and (computer_choice == 'paper')):
        prompt('You win!')
    elif ((choice == 'rock') and (computer_choice == 'paper') or
          (choice == 'paper') and (computer_choice == 'scissors') or
            (choice == 'scissors') and (computer_choice == 'rock')):
        prompt('Computer wins!')
    else:
        prompt("It's a tie!")


def prompt(message):
    print(f'=> {message}')


def get_user_choice():
    prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
    choice = input().lower()

    while choice not in VALID_CHOICES:
        prompt(f"Please pick a valid choice: {', '.join(VALID_CHOICES)}")
        choice = input().lower()
    return choice


while True:
    choice = get_user_choice()
    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {choice}')
    prompt(f'Computer chose {computer_choice}')

    display_result(choice, computer_choice)

    prompt('Would you like to continue? (y/n)')
    retry = input().lower()
    while True:
        if retry.startswith('y') or retry.startswith('n'):
            break
        prompt('Please enter a valid response: (y/n)')
        retry = input().lower()
    if retry.startswith('n'):
        break
