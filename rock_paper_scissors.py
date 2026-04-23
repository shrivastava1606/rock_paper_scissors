import random
choices=["rock","paper","scissors"]

def menu():
    print("1. Play")
    print("2. Exit")

def game():
    user=input('enter rock or paper or scissors:').lower()

    if user not in choices:
        print("Invalid choice")
        return
    computer_choice=random.choice(choices)
    print("computer:",computer_choice)
    if user==computer_choice:
        print("Result:Tie") 
    elif (user=="rock" and computer_choice=="scissors") or (user=="scissors" and computer_choice=="paper") or (user=="paper" and computer_choice=="rock"):
        print("YOU WIN")
    else:
        print("COMPUTER WIN")
while True:
    menu()
    choice=input("Enter your choice: ")
    if choice=="1":
        game()
    elif choice=="2":
        print("Exiting...!!")
        break
    else:
        print("Invalid choice. Please try again.")
