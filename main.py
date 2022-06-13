import random

loop = bool()
loop = True

while loop:
   
    user_action = input("Enter a choice (R, P, S): ")
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
 
    if user_action in possible_actions:
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
            loop = True
        elif user_action == "R":
            if computer_action == "S":
                print("Player (Rock) : CPU (Scissors)=> You win!")
                loop = False
            else:
                print("Player (Rock) : CPU (Paper)=> CPU wins.")
                loop = False
        elif user_action == "P":
            if computer_action == "R":
                print("Player (Paper) : CPU (Rock)=> You win!")
                loop = False
            else:
                print("Player (Paper) : CPU (Scissors)=> CPU wins.")
                loop = False
        elif user_action == "S":
            if computer_action == "P":
                print("Player (Scissors) : CPU (Paper)=> You win!")
                loop = False
            else:
                print("Player (Scissor) : CPU (Rock)=> CPU wins.")
                loop = False
    
    else:
        print(f"\nERROR: Option selected incorrect! Please replay\n")
        continue
