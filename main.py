import sys

from prologue import print_prologue
from chapters.chapter1 import chapter1
from input_listener import continue_listener
from clear_terminal import clear

def game_over():
    print("You died!")
    print("Would you like to try again?")
    cmd = str(input("Y/N: "))

    if cmd.lower() == "y":
        main()
    else:
        sys.exit()

def main():
    clear()
    GENERAL_SUCCESS_CHANCE = 67
    STEALTH_SUCCESS_CHANCE = 33
    STRENGTH_SUCCESS_CHANCE = 33
    INTELLECT_SUCCESS_CHANCE = 33

    ROLE = ""

    print("1. Thief (Stealth)")
    print("2. Knight (Strength)")
    print("3. Scholar (Intellect)")
    print("Your background determines your success chance in certain situations.")
    ans = str(input("Choose your background (1/2/3): "))
    ans = ans.strip().lower()

    match ans:
        case "1":
            ROLE = "thief"
            STEALTH_SUCCESS_CHANCE = 67
        case "2":
            ROLE = "knight"
            STRENGTH_SUCCESS_CHANCE = 67
        case "3":
            ROLE = "scholar"
            INTELLECT_SUCCESS_CHANCE = 67
        case _:
            clear()
            print("Invalid choice. Please try again.")
            print()
            continue_listener()
            clear()
            main()

    clear()

    print_prologue()
    continue_listener()
    chapter1(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)

if __name__ == '__main__':
    main()