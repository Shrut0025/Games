print("Welcome To HangMan Game")
print("Wish You All The Best!")
import random 
word_list = ['you','me','us','good','life','happy','ever','after']
chosen_word = random.choice(word_list)
display=[]

for i in range(len(chosen_word)):
    display += '_'  
print(display)    

game_over = False
lives = 6

while not game_over :
    guessed_letter = input("Enter the guessed letter : ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter :
            display[position] = guessed_letter
    print(display)

    if guessed_letter not in chosen_word:
        lives -=1 
        print(f"{lives} lives left")
        if lives == 0:
            game_over = True  
            print("You LOSE!!")

    if '_' not in display:
        game_over = True
        print("You WIN!!!")        