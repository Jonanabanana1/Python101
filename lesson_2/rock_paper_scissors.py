import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
POSSIBLE_WINS = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['spock', 'paper'],
    'spock': ['scissors', 'rock'],
}


def display_result(local_choice, local_computer_choice):

    if is_winner(local_choice, local_computer_choice):
        prompt(f'You win! {local_choice} beats {computer_choice}')
    elif is_winner(computer_choice, local_choice):
        prompt(f'Computer wins! {computer_choice} beats {local_choice}')
    else:
        prompt("It's a tie!")


def is_winner(winning_choice, losing_choice):
    return losing_choice in POSSIBLE_WINS[winning_choice]


def prompt(message):
    print(f'=> {message}')


def get_user_choice():

    # Set prefixes list to track new prefixes for each valid choice
    # Set prefix_dictionary to correlate prefix with valid choice
    # This is so when we return later we can capture the full choice
    # Iterate through valid choices
    # Set prefix = first character of item in valid_choices
    # If prefix is already in list of prefixes, append next character until it
    # is no longer in list of prefixes (must be unique)
    # If the length of prefix is maxed out (equal to length of item in valid choice) then add a unique character
    # Add unique prefix into prefixes and also into the prefix_dictionary

    prefixes = []
    prefix_dictionary = {}

    for item in VALID_CHOICES:
        prefix = item[0]
        prefix_counter = 1

        while prefix in prefixes:
            if len(prefix) == len(item):
                prefix += '_'
                break
            prefix += item[prefix_counter]
            prefix_counter += 1

        prefixes.append(prefix)
        prefix_dictionary[prefix] = item
    
    prompt(f"Choose one: {', '.join(VALID_CHOICES)}")
    prompt(f"Short command: {', '.join(prefixes)}")
    user_choice = input().lower()

   

    while user_choice not in prefixes and user_choice not in VALID_CHOICES:
        prompt(f"Please pick a valid choice: {', '.join(VALID_CHOICES)}")
        user_choice = input().lower()

    if user_choice in prefixes:
        return prefix_dictionary[user_choice]

    return user_choice


prompt(f'Welcome to {"-".join(VALID_CHOICES).title()}')
player_score = 0
computer_score = 0

while True:
    player_choice = get_user_choice()
    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {player_choice}')
    prompt(f'Computer chose {computer_choice}')

    display_result(player_choice, computer_choice)

    if is_winner(player_choice, computer_choice):
        player_score += 1
    if is_winner(computer_choice, player_choice):
        computer_score += 1

    prompt(f'Player: {player_score}  |  Computer: {computer_score}')

    if player_score == 3:
        prompt('Match is over!\nCongrats on winning the match!')
        break
    if computer_score == 3:
        prompt('Match is over!\nComputer wins the match!')
        break

    prompt('Would you like to continue? (y/n)')
    retry = input().lower()

    while True:
        if retry.startswith('y') or retry.startswith('n'):
            break
        prompt('Please enter a valid response: (y/n)')
        retry = input().lower()

    if retry.startswith('n'):
        prompt('Thanks for playing!')
        break
