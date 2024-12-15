import sys

def game_over():
    print("You died!")
    print("Would you like to try again?")
    cmd = str(input("Y/N: "))

    if cmd.lower() == "y":
        print("Restarting game...")
        main()
    else:
        sys.exit()

def main():
    GENERAL_SUCCESS_CHANCE = 67
    STEALTH_SUCCESS_CHANCE = 33
    FIGHT_SUCCESS_CHANCE = 33
    INTELLECTUAL_SUCCESS_CHANCE = 33

    print("1. Thief (Stealth)")
    print("2. Knight (Fight)")
    print("3. Scholar (Intellectual)")
    ans = str(input("Choose your background: "))

if __name__ == '__main__':
    main()