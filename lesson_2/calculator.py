import json
# Open the JSON file for reading
with open('messages.json', 'r') as file:
    data = json.load(file)


def prompt(message):
    print(f'=> {message}')


def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False


def calculate():
    prompt(data[language]['ask_first_number'])
    number_1 = input()
    while invalid_number(number_1):
        prompt(data[language]['error_number'])
        number_1 = input()

    prompt(data[language]['ask_second_number'])
    number_2 = input()
    while invalid_number(number_2):
        prompt(data[language]['error_number'])
        number_2 = input()

    prompt(data[language]['ask_operation'])
    operation = input()
    while operation not in ['1', '2', '3', '4']:
        prompt(data[language]['error_number_list'])
        operation = input()

    match operation:
        case '1':
            output = float(number_1) + float(number_2)
        case '2':
            output = float(number_1) - float(number_2)
        case '3':
            output = float(number_1) * float(number_2)
        case '4':
            output = float(number_1) / float(number_2)

    prompt(f"{data[language]['output']} {output}")


prompt('en: English, spa: Spanish')
language = input()  # Could do more input validation here
prompt(data[language]['welcome'])
while True:
    calculate()
    prompt(data[language]['ask_retry'])
    try_again = input()
    while try_again not in ['y', 'n']:
        prompt(data[language]['error_retry'])
        try_again = input()
    if try_again == 'n':
        break
