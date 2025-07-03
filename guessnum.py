import random
secret_number = random.randint(1, 100)
guess_count = 0
user_guess = int(input("Guess the number between 1 and 100: "))
guess_count += 1

while user_guess != secret_number:
        if user_guess > secret_number:
            print("Too high")
        elif user_guess < secret_number:
            print("Too low")
        user_guess = int(input("Try again: "))
        guess_count += 1
    
print(f"You guessed it in {guess_count} guesses!")

best_score = None

if best_score is None or guess_count < best_score:
    best_score = guess_count
    print(f"New best score: {best_score} guesses!")
else:
    print(f"You didnt beat your best score of: {best_score} guesses.")
    
play_again = input("Play again? (y/n): ")
if play_again.lower() == "y":
    print(input("Guess the number between 1 and 100: "))
else:
    print("Thanks for playing!")


