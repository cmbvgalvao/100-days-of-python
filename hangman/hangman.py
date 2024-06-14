import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
end_of_game = False
lives = len(stages) - 1

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')
print(f"{logo}\n")
for _ in range(word_length):
    display.append("_")

print(f"{' '.join(display)}\n")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}\n")
    
    if guess not in chosen_word:
        lives -= 1
        
    print(stages[lives])
    
    if lives == 0:
        end_of_game = True
        print("You lose...")
        print(f"The word was {chosen_word}")
        
    elif "_" not in display:
        end_of_game = True
        print("You win!")