import random

print("Welcome to the Guess A Number Game!")

choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_continue = True
#number_of_tries = 0
user_choice = 0
computer_number = random.choice(choices)

def user_input():
    global user_choice #when trying to use a global variable in a try block
    try:
        user_choice = int(
            input(
                f"Chose a number between {choices[0]} and {choices[len(choices)-1]}.\n"
            ))
        if user_choice not in choices:
            raise ValueError("Invalid choice")
    except ValueError:
        print(
            "You typed an invalid value. Please chose a number between 1 and 10."
        )
def response():
    #print(user_choice)
    #print(computer_number)
    #print(number_of_tries)
    if user_choice == computer_number:
        print(f"Congratulations! You guessed the number in {number_of_tries} tries")
    elif user_choice < computer_number:
        print("Too low!")
    else:
        print("Too high!")
while to_continue:
    number_of_tries = 0
    computer_number = random.choice(choices)
    # print(computer_number)
    while user_choice != computer_number:
        try:
            user_input()
        except ValueError:
            continue
        else:
            number_of_tries += 1
            response()
    to_continue = input("Do you want to play again? Type 'y' for yes or 'n' for no.\n").lower(
        ) == "y"
print("Thank you for playing!")
quit(0)
