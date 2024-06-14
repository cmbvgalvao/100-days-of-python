import random
from hangman_art import stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
end_of_game = False
lives = len(stages) - 1

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

for _ in range(word_length):
    display.append("_")

print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        
    print(stages[lives])
    
    if lives == 0:
        end_of_game = True
        print("You lose...")
        
    elif "_" not in display:
        end_of_game = True
        print("You win!")