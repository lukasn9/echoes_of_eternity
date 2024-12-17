from text_printing import text_printing
from input_listener import continue_listener
from clear_terminal import clear
from random import randint
import sys

global STEALTH_SUCCESS_CHANCE
global STRENGTH_SUCCESS_CHANCE
global INTELLECT_SUCCESS_CHANCE
global GENERAL_SUCCESS_CHANCE

def chapter_start():
    clear()
    print("CHAPTER 1")
    chapter_intro = ["A loud bang wakes you, and you rush to the window to see monstrous creatures attacking the city.", "Suddenly, an old scholar bursts into your room, telling you that only you can save the world.", "He hands you a map showing the locations of three stolen shards needed to stop the chaos.", "The task is dangerous, but the world's survival depends on you."]
    text_printing(chapter_intro)
    continue_listener()

def part_1(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    clear()
    print("PART 1: Escape from the City")
    text =  ["As you rush out of your house, you find three possible paths to escape the city:", "1. Sneak past the monsters unnoticed (Stealth)", "2. Fight your way through the monsters (Strength)", "3. Escape through the city's sewage system (Intellect)"]
    text_printing(text, False)
    ans = str(input("Which path will you choose? (1/2/3): "))
    clear()

    match ans:
        case "1":
            if randint(0, 100) <= STEALTH_SUCCESS_CHANCE:
                text = ["You decided to sneak past the monsters.", "The monsters are too busy fighting the city guards to notice you.", "You successfully escape the city."]
                text_printing(text)
                continue_listener()
            else:
                text = ["You decided to sneak past the monsters.", "You make a noise, and the monsters spot you.", "You try to run, but the monsters catch you, and you have to try to fight them."]
                text_printing(text)
                fight_monsters(GENERAL_SUCCESS_CHANCE)
        case "2":
            if randint(0, 100) <= STRENGTH_SUCCESS_CHANCE:
                text = ["You decided to fight your way through the monsters.", "With your strength, you defeat the monsters.", "You successfully escape the city."]
                text_printing(text)
                continue_listener()
            else:
                text = ["You decided to fight your way through the monsters.", "The monsters are too strong, and you are overwhelmed.", "You were killed in the battle."]
                text_printing(text)
                game_over(part_1)
        case "3":
            if randint(0, 100) <= INTELLECT_SUCCESS_CHANCE:
                text = ["You decided to escape through the city's sewage system.", "You navigate the sewage system, but come across a locked gate.", "Thankfully, you remembered how to lockpick and open it with ease.", "You successfully escape the city."]
                text_printing(text)
                continue_listener()
            else:
                text = ["You decided to escape through the city's sewage system.", "You navigate the sewage system, but come across a locked gate.", "You try to open the gate, but fail to do so.", "The monsters catch up to you and you have to fight them."]
                text_printing(text)
                fight_monsters(GENERAL_SUCCESS_CHANCE)
        case _:
            print("Invalid choice. Please try again.")
            print()
            part_1()

def part_2():
    text = ["You have successfully escaped the city.", "You are now on your way to find the three stolen shards to save the world.", "Your journey is just beginning..."]
    text_printing(text)
    continue_listener()

def fight_monsters(GENERAL_SUCCESS_CHANCE):
    text = ["You have killed all of the monsters in your way.", "Except one.", "You have to fight the last monster to escape the city."]
    text_printing(text)
    clear()
    print()

    hp = 100
    enemy_hp = 40

    while True:
        if hp <= 0:
            text = ["You have been killed by the monster."]
            text_printing(text)
            game_over(part_1)
        elif enemy_hp <= 0:
            text = ["You have defeated the monster.", "You successfully escape the city."]
            text_printing(text)
            break
        print("FIGHT: Monster")
        print("Your HP: 100/100")
        print("Monster's HP: 40/40")
        print("1. Attack")
        print("2. Defend")
        print("3. Run")
        cmd = str(input("Choose your action: "))

        if cmd == "1":
            text = ["You attack the monster.", "The monster takes 10 damage."]
            text_printing(text)
            enemy_hp -= 10
            text = ["The monster attacks you.", "You take 5 damage."]
            text_printing(text)
            hp -= 5
        elif cmd == "2":
            text["You defend against the monster's attack."]
            text_printing(text)
        elif cmd == "3":
            if randint(0, 100) <= GENERAL_SUCCESS_CHANCE:
                clear()
                text = ["You manage to run away from the monster.", "You successfully escape the city."]
                text_printing(text)
                continue_listener()
                part_2()
            else:
                text = ["You try to run, but the monster catches you.", "The monster attacks you.", "You take 10 damage."]
                text_printing(text)
                hp -= 10

def game_over(func):
    print("Game Over!")
    print("Would you like to try again?")
    cmd = str(input("Y/N: "))

    if cmd.lower() == "y":
        print("Restarting game...")
        func()
    else:
        sys.exit()

def chapter1(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    chapter_start()
    part_1(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)