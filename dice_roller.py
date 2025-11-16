import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘",
    ),
}

print("*** ASCII Dice Roller + Guess Game ***\n")

while True:
    play = input("Do you want to play? (yes / no): ").lower()

    if play == "no":
        print("Goodbye!")
        break

    elif play != "yes":
        print("Please type 'yes' or 'no'.\n")
        continue

    # Ask guess
    guess = input("Guess the dice number (1-6): ")

    if not guess.isdigit() or not (1 <= int(guess) <= 6):
        print("Invalid guess! Enter a number 1-6.\n")
        continue

    guess = int(guess)

    # Roll the dice
    roll = random.randint(1, 6)
    print(f"\nYou rolled: {roll}")

    for line in DICE_ART[roll]:
        print(line)

    # Check correctness
    if guess == roll:
        print(" CONGRATULATIONS! You guessed correctly! \n")
    else:
        print(f" Wrong guess! You guessed {guess}. Try again!\n")
