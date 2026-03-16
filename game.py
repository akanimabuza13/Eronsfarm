import random

def start_game():
    print("Welcome to the Enhanced CLI Game!")
    print("Your goal is to guess the correct number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess (or type 'exit' to quit): ")

        if guess.lower() == 'exit':
            print("Thanks for playing! Goodbye!")
            break
        
        try:
            guess = int(guess)
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    start_game()