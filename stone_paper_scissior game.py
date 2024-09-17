import random

# Function to get the user's choice
def User_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice! Please enter rockpaper/scissors: ").lower()
    return choice

# Function to get the computer's choice
def Computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game():
    user_choice = User_choice()
    computer_choice = Computer_choice()
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Main loop to play multiple rounds and track scores
def play_again():
    user_score = 0
    computer_score = 0

    while True:
        play_game()
        if 'You win' in determine_winner:
            user_score += 1
        elif 'Computer wins' in determine_winner:
            computer_score += 1

        print(f"Scores -> You: {user_score}, Computer: {computer_score}")
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play_again()
