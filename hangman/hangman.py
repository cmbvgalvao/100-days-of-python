import random
from hangman_art import stages
from hangman_words import word_list
from tools import clear_terminal




def game():
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    display = ['_'] * word_length
    end_of_game = False
    lives = len(stages) - 1
    guessed_letters= set()
    
    clear_terminal()
    print("Guess the following word:")
    print(f"{' '.join(display)}\n")

    while not end_of_game:
        #Try to get the users input. If the user's input is not an alphabetical value or it has already been guessed, try again.
        try:
            guess = input("Guess a letter: ").lower()
            if not guess.isalpha() or len(guess) != 1:
                raise ValueError("You typed an invalid value. Please chose a single letter")
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
                continue
        except ValueError as e:
            print(e)
            continue
        
        clear_terminal()
        guessed_letters.add(guess)
            
        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print(f"{' '.join(display)}\n")
        
        if guess not in chosen_word:
            lives -= 1
            #print(lives)
            
        print(f"Letters guessed:\n{' '.join(sorted(guessed_letters))}")    
        print(f"{stages[lives]}\n")
        
        if lives == 0:
            end_of_game = True
            print("You lose...")
            print(f"The word was {chosen_word}")
            
        elif "_" not in display:
            end_of_game = True
            print("You win!")
