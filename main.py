import random

def ask_number(min_number,max_number):
    number_int = 0
    while number_int == 0:
        number_str = input(f"What is the magic number (between {min_number} and {max_number})? ")
        try:
            number_int = int(number_str)
        except:
            print("Error: Please enter a number, please retry")
        else:
            if number_int < min_number or number_int > max_number:
                print(f"Error: please enter a number between {min_number} and {max_number}")
    return number_int

def random_number(min_number,max_number):
    random_n = random.randint(min_number,max_number)
    return random_n

min_number=0
max_number=10
number = 0
lifes = 4
magic_number = random_number(min_number,max_number)
while lifes != 0:
    number = ask_number(min_number,max_number)
    if int(number) == magic_number:
        print("You won the game")
        break
    elif int(number) > magic_number:
        print(f"The magic number is lower")
        lifes -= 1
    elif int(number) < magic_number:
        print(f"The magic number is greater")
        lifes -= 1
if lifes == 0:
    print("game over!!!!")
