import random

def play_game():
    while True:
        print("\nWelcome to Rock, Paper, Scissors!")
        print("Choose your move: rock, paper, or scissors")

        # Get user input
        user_choice = input("Enter your choice: ").lower()

        # Generate computer's choice
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Compare choices and determine winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!")
        else:
            print("You lose!")

        # Display result
        print(f"You chose {user_choice}, and the computer chose {computer_choice}")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
