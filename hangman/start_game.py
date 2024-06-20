from hangman_art import logo
from tools import clear_terminal
from hangman import game

game_running = True
option = 0

while game_running == True:
    
    clear_terminal()
    while option not in [1, 2]:
        try:
            option = int(input(f"{logo}\n\n\n1- New Game\n2- Quit Game\n"))
            if option not in [1, 2]:
                raise ValueError("Please chose 1 for New Game or 2 for Quit Game.")
        except ValueError as e:
            print(e)
            continue
        
    if option == 1:
        game()
        option = 0
        to_continue = input("Press Enter to go to the Main Menu")
    else:
        print("Thank you for playing Hangman!")
        game_running = False        
        
        