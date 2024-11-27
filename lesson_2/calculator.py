def prompt(message):
    print(f'=> {message}')


def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    return False


prompt('Welcome to Calculator!')

prompt("What's the first number?")
number_1 = input()
while invalid_number(number_1):
    prompt('Error, please input a valid number')
    number_1 = input()

prompt("What's the second number?")
number_2 = input()
while invalid_number(number_2):
    prompt('Error, please input a valid number')
    number_2 = input()

prompt('What operation would you like to perform?\n'
       '1: Addition  2: Subtraction  3: Multiplication  4: Division')
operation = input()
while operation not in ['1', '2', '3', '4']:
    prompt('Error, please input a number between 1-4')
    operation = input()

match operation:
    case '1':
        output = int(number_1) + int(number_2)
    case '2':
        output = int(number_1) - int(number_2)
    case '3':
        output = int(number_1) * int(number_2)
    case '4':
        output = int(number_1) / int(number_2)

print(f'The output is {output}')
