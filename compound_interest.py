import unittest

def ci(amount: float, rate: float, months: float):
    years = months / 12  
    interest_earned = amount * (1 + rate / (12 * 100)) ** (12 * years) - amount
    return interest_earned  

if __name__ == "__main__":
    amount = input("Please enter your amount: ")
    rate = input("Please enter the rate: ")
    months = input("How many months will the money compound: ")

    try:
        amount = float(amount)
        rate = float(rate)
        months = float(months)

        print("You entered:", amount, rate, months)
        
        interest_earned = ci(amount, rate, months)
        print(f'You will earn: ${interest_earned:.2f}')
    except ValueError:
        print("Error: All inputs must be numbers.")
