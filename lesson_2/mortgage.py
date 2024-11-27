# Formula for monthly car payment
# m = p * (j / (1 - (1 + j) ** (-n)))
# m = monthly payment
# p = loan amount
# j = monthly interest rate
# n = loan duration in months

# INPUT:
# loan amount, annual percentage rate, duration
# OUTPUT:
# monthy payment

# Monthly interest rate = APR / 12
# Duration in months = Duration (years) * 12

# START
# GET loan amount
# GET annual percentage rate in form 0.x (ex 0.5)
# GET duration in years
# SET duration_months = duration in years * 12
# SET monthly_interest_rate = APR / 12
# SET m = p * (j / (1 - (1 + j) ** (-n))) substitute values in
# PRINT m
# END
def calculate_monthly_payment(loan, interest, duration):
    return loan * (interest / (1 - (1 + interest) ** (-duration)))


def prompt(message):
    print(f'=> {message}')


def validate_number(number_str):
    while True:
        try:
            float(number_str)
        except (ValueError, TypeError):
            prompt('Please enter a valid number:')
        else:
            break


prompt('Enter loan amount:')
loan_amount = input()
prompt('Enter annual percentage rate: (ex: 0.5 = 50%)')
apr = input()
prompt('Enter duration of loan in years:')
duration_years = input()

validate_number(loan_amount)
validate_number(apr)
validate_number(duration_years)

loan_amount = float(loan_amount)
duration_months = float(duration_years) * 12
monthly_interest = float(apr) / 12

monthy_payment = calculate_monthly_payment(loan_amount,
                                           monthly_interest,
                                           duration_months)
prompt(f'Your monthly payment is {monthy_payment:.2f}$')
