import random

#added input validation
def get_valid_input(prompt, data_type=int):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value.")

def play_game():
    print("Hello, what is your name?")
    name = input()

    while True:
        secretNumber = random.randint(1, 20)
        print("Well, " + name + ", I am thinking of a number between 1 and 20.")

        for guessesTaken in range(1, 7):
            guess = get_valid_input("Take a guess: ")

            if guess < secretNumber:
                print("Your guess is too low.")
            elif guess > secretNumber:
                print("Your guess is too high.")
            else:
                print("Good job, " + name + "! You guessed my number between 1 and 20 in " + str(guessesTaken) + " guesses.")
                break

        if guess != secretNumber:
            print("Nope. The number I was thinking of was " + str(secretNumber))
#added play again option
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
