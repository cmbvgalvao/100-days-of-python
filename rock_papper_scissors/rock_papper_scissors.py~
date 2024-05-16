import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("Welcome to the Rock, Paper, Scissors Game!")
to_continue = True
while to_continue:
    try:
        user_choice = int(
            input(
                "What do you choose? Type 1 for Rock, 2 for Paper, or 3 for Scissors.\n"
            ))
        if user_choice not in [1, 2, 3]:
            raise ValueError("Invalid choice")
    except ValueError:
        print(
            "You typed an invalid value. Please type 1 for Rock, 2 for Paper, or 3 for Scissors."
        )
        continue
    computer_choice = random.randint(1, 3)
    if user_choice == 1:
        print(rock)
    elif user_choice == 2:
        print(paper)
    elif user_choice == 3:
        print(scissors)
    print("Computer chose:")
    if computer_choice == 1:
        print("You chose:")
        print(rock)
    elif computer_choice == 2:
        print("You chose:")
        print(paper)
    elif computer_choice == 3:
        print("You chose:")
        print(scissors)
    if user_choice == 1 and computer_choice == 3:
        print("You win!")
    elif user_choice == 2 and computer_choice == 1:
        print("You win!")
    elif user_choice == 3 and computer_choice == 2:
        print("You win!")
    elif user_choice == computer_choice:
        print("It's a draw!")
    else:
        print("You lose!")
    to_continue = input(
        "Do you want to play again? Type 'y' for yes or 'n' for no.\n").lower(
        ) == "y"
print("Quitting. Thank you for playing!")
quit(0)
