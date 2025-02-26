import random 

print("WELCOME TO ROCK PAPER N SCISSORS GAME")
print("\n")
user_choice = int(input("Enter 0 for Rock , 1 for Paper , 2 for Scissors : "))
print(f"You entered {user_choice} .")

if (user_choice >= 3 or user_choice < 0):
    print("Invalid input given . Please try again later")

else:
    comp_choice = random.randint(0,2)
    print(f"Computer entered {comp_choice} .")

    if (user_choice == comp_choice):
        print("That's a draw!")

    elif(user_choice == 0 and comp_choice ==2):
        print("You won. Congrats!") 

    elif(user_choice == 2 and comp_choice ==0):
        print("You loose. Computer wins!")    

    elif (comp_choice > user_choice):
        print("You loose. Computer wins!")

    elif(user_choice > comp_choice):
        print("You won. Congrats!")   
