"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Alexandr Sytko
email: sytko.alex@gmail.com
discord: alex_89608
"""


import random

def generate_secret_number():
    """Generates a random 4-digit number with unique digits."""
    digits = list(range(10))
    random.shuffle(digits)
    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0]  
    return ''.join(map(str, digits[:4]))

def evaluate_guess(secret_number, guess):
    """Evaluates the guess and returns the number of bulls and cows."""
    bulls = sum(1 for i in range(4) if secret_number[i] == guess[i])
    cows = sum(1 for digit in guess if digit in secret_number) - bulls
    return bulls, cows

def main():
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")

    secret_number = generate_secret_number()
    attempts = 0

    while True:
        guess = input("Enter a 4-digit number: ")
        
        if not guess.isdigit() or len(guess) != 4 or len(set(guess)) != 4 or guess[0] == '0':
            print("Please enter a valid 4-digit number with unique digits (not starting with 0).")
            continue
        
        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)
        if bulls == 4:
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            break
        else:
            print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}")

if __name__ == "__main__":
    main()