from text_printing import text_printing
from input_listener import continue_listener
from clear_terminal import clear
from random import randint
import sys
from .chapter2 import chapter2

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

    while True:
        text =  ["As you rush out of your house, you find three possible paths to escape the city:", "1. Sneak past the monsters unnoticed (Stealth)", "2. Fight your way through the monsters (Strength)", "3. Escape through the city's sewage system (Intellect)"]
        text_printing(text, False)
        ans = str(input("Which path will you choose? (1/2/3): "))
        clear()

        pos_answers = ["1", "2", "3", "sneak", "fight", "escape", "stealth", "strength", "intellect"]
        if ans.strip().lower() in pos_answers:
            break
        else:
            print("Invalid choice. Please try again.")
            print()
            continue_listener()
            clear()

    match ans:
        case "1" | "sneak" | "stealth":
            if randint(0, 100) <= STEALTH_SUCCESS_CHANCE:
                text = ["You decided to sneak past the monsters.", "The monsters are too busy fighting the city guards to notice you.", "You successfully escape the city."]
                text_printing(text)
                continue_listener()
            else:
                text = ["You decided to sneak past the monsters.", "You make a noise, and the monsters spot you.", "You try to run, but the monsters catch you, and you have to try to fight them."]
                text_printing(text)
                fight_monsters(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)
        case "2" | "fight" | "strength":
            if randint(0, 100) <= STRENGTH_SUCCESS_CHANCE:
                text = ["You decided to fight your way through the monsters.", "With your strength, you defeat the monsters.", "You successfully escape the city."]
                text_printing(text)
                print()
                continue_listener()
            else:
                text = ["You decided to fight your way through the monsters.", "The monsters are too strong, and you are overwhelmed.", "You were killed in the battle."]
                text_printing(text)
                print()
                game_over(part_1, [STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE])
        case "3" | "escape" | "intellect":
            if randint(0, 100) <= INTELLECT_SUCCESS_CHANCE:
                text = ["You decided to escape through the city's sewage system.", "You navigate the sewage system, but come across a locked gate.", "Thankfully, you remembered how to lockpick and open it with ease.", "You successfully escape the city."]
                text_printing(text)
                print()
                continue_listener()
            else:
                text = ["You decided to escape through the city's sewage system.", "You navigate the sewage system, but come across a locked gate.", "You try to open the gate, but fail to do so.", "The monsters catch up to you and you have to fight them."]
                text_printing(text)
                print()
                continue_listener()
                fight_monsters(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)
    part_2(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)

def part_2(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    clear()
    text = ["You have successfully escaped the city.", "You are now on your way to find the three stolen shards to save the world.", "Your journey is just beginning..."]
    text_printing(text)
    continue_listener()
    clear()

    text = ["You climb a hill next to the city and look back at the destruction caused by the monsters.", "You see the old scholar who gave you the map standing at the city wall as it collapses.", "You vow to complete the journey and save the world in his memory."]
    text_printing(text)
    continue_listener()
    clear()

    text = ["You look at the map and see the first shard's location marked in the nearby forest.", "You head towards the forest to find the first shard."]
    text_printing(text)
    continue_listener()

    pos_answers = ["1", "2", "3", "forest", "mountain", "bridge", "dense forest path", "mountain path", "damaged bridge"]
    while True:
        clear()
        text = ["As you enter the forest, you  find yourself at a crossroad.", "You see three paths ahead of you:", "1. Dense forest path", "2. Mountain path", "3. Damaged bridge"]
        text_printing(text, False)
        ans = str(input("Which path will you choose? (1/2/3): "))
        clear()

        if ans.strip().lower() in pos_answers:
            break
        else:
            print("Invalid choice. Please try again.")
            print()
            continue_listener()

    match ans:
        case "1" | "forest" | "dense forest path":
            forest_path(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)
        case "2" | "mountain" | "mountain path":
            mountain_path(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)
        case "3" | "bridge" | "damaged bridge":
            bridge_path(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)

def forest_path(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    clear()
    text = ["You enter the dense forest and start walking through it.", "The forest is dark and eerie, but you are determined to find the first shard.", "As you walk deeper into the forest, you hear a growling sound.", "You see a pack of wolves approaching you."]
    text_printing(text)
    continue_listener()

    pos_answers = ["1", "2", "3", "hide", "climb", "scare", "hide behind a rock", "climb up a tree", "scare the wolves away"]
    while True:
        clear()
        text = ["You have three options:", "1. Hide behind a rock (Stealth)", "2. Climb up a tree (Strength)", "3. Scare the wolves away (Intellect)"]
        text_printing(text, False)
        ans = str(input("Which option will you choose? (1/2/3): "))
        clear()

        if ans.strip().lower() in pos_answers:
            break
        else:
            print("Invalid choice. Please try again.")
            print()
            continue_listener()

    clear()
    match ans:
        case "1" | "hide" | "hide behind a rock":
            if randint(0, 100) <= STEALTH_SUCCESS_CHANCE:
                text = ["You hide behind a rock and the wolves pass by without noticing you.", "You successfully escape the wolves and continue through the forest."]
                text_printing(text)
                print()
                continue_listener()
            else:
                text = ["You hide behind a rock, but the wolves find you.", "You have to fight the wolves to escape."]
                text_printing(text)
                print()
                continue_listener()
                fight_wolves(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)
        case "2" | "climb" | "climb up a tree":
            if randint(0, 100) <= STRENGTH_SUCCESS_CHANCE:
                text = ["You climb up a tree and the wolves pass by without noticing you.", "You successfully escape the wolves and continue through the forest."]
                text_printing(text)
                print()
                continue_listener()
            else:
                text = ["You try to climb up the tree, but you slip and fall.", "You break your spine and die."]
                text_printing(text)
                print()
                continue_listener()
                game_over(part_2, [STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE])
        case "3" | "scare" | "scare the wolves away":
            if randint(0, 100) <= INTELLECT_SUCCESS_CHANCE:
                text = ["You scare the wolves away by making loud noises.", "You successfully escape the wolves and continue through the forest."]
                text_printing(text)
                print()
                continue_listener()
            else:
                text = ["You try to scare the wolves away, but they are not afraid of you.", "You have to fight the wolves to escape."]
                text_printing(text)
                print()
                continue_listener()
                fight_wolves(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)

    clear()
    text = ["END OF CHAPTER 1"]
    text_printing(text)
    continue_listener()
    chapter2(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)

def mountain_path(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    clear()
    text = ["You approach the mountain and start climbing it.", "The climb is tough, but you are certain that you can make it.", "As you are almost at the top, you hear the voice of an old lady.", "You look up and see that she is holding a knife, threatening to cut your rope.", "She tells you that you can't pass unless you answer her riddle."]
    text_printing(text)
    continue_listener()

    pos_answers = ["1", "2", "call", "answer", "call her bluff", "answer her riddle"]
    while True:
        clear()
        text = ["You have two options:", "1. Call her bluff", "2. Answer her riddle"]
        text_printing(text, False)
        ans = str(input("Which option will you choose? (1/2): "))
        clear()

        if ans.strip().lower() in pos_answers:
            break
        else:
            print("Invalid choice. Please try again.")
            print()
            continue_listener()

    clear()
    match ans:
        case "1" | "call" | "call her bluff":
            text = ["You call her bluff and continue climbing.", "But the old lady laughs and cuts the rope.", "You fall down the mountain and die."]
            text_printing(text)
            game_over(part_2, [STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE])
        case "2" | "answer" | "answer her riddle":
            pos_answers = ["1", "2", "3", "keyboard", "safe", "puzzle box"]
            while True:
                clear()
                text = ["The old lady asks you the following riddle:", "I have keys but no locks.", "I have space but no room.", "You can enter but not go inside. What am I?", "1. Keyboard", "2. A safe", "3. Puzzle box"]
                text_printing(text, False)
                ans = str(input("What is the answer to the riddle? (1/2/3): "))
                clear()

                if ans.strip().lower() in pos_answers:
                    if ans == "1" or ans == "keyboard":
                        text = ["You answer the riddle with 'Keyboard'.", "The old lady smiles and lets you pass.", "You successfully reach the top of the mountain."]
                        text_printing(text)
                        continue_listener()
                        break
                    else:
                        text = ["You answer the riddle incorrectly.", "The old lady laughs and cuts the rope.", "You fall down the mountain and die."]
                        text_printing(text)
                        game_over(part_2, [STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE])
                else:
                    print("Invalid choice. Please try again.")
                    print()
                    continue_listener()

    clear()
    text = ["You finally reach the top of the mountain.", "You look around and see a temple in the distance.", "You head towards the temple to find the first shard."]
    text_printing(text)
    continue_listener()

    clear()
    text = ["END OF CHAPTER 1"]
    text_printing(text)
    continue_listener()
    chapter2(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)

def bridge_path(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    clear()
    text = ["You approach the damaged bridge and start crossing it.", "You get to the middle of the bridge when you notice a hole in the bridge.", "You have to cross it somehow."]
    text_printing(text)
    print()
    continue_listener()

    pos_answers = ["1", "2", "3", "jump", "search", "give up", "jump over the hole", "search for another way", "give up and go back"]
    while True:
        clear()
        text = ["You have three options:", "1. Jump over the hole", "2. Search for another way", "3. Give up and go back"]
        text_printing(text, False)
        ans = str(input("Which option will you choose? (1/2/3): "))
        clear()

        if ans.strip().lower() in pos_answers:
            if ans == "1" or ans == "jump" or ans == "jump over the hole":
                text = ["You decide to jump over the hole.", "Unfortunately, you fall into the hole and die."]
                text_printing(text)
                print()
                game_over(part_2, [STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE])
                break
            elif ans == "2" or ans == "search" or ans == "search for another way":
                text = ["You decide to try and find another way to cross the hole.", "While searching, you notice a wooden plank nearby.", "You use the plank to cross the hole safely.", "You successfully cross the bridge and continue your journey."]
                text_printing(text)
                print()
                continue_listener()
                break
            elif ans == "3" or ans == "give up" or ans == "give up and go back":
                text = ["You decide to give up and go back."]
                text_printing(text)
                print()
                continue_listener()
                part_2(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)
        else:
            print("Invalid choice. Please try again.")
            print()
            continue_listener()

    clear()
    text = ["END OF CHAPTER 1"]
    text_printing(text)
    continue_listener()
    chapter2(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)

def fight_monsters(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    text = ["You have killed all of the monsters in your way.", "Except one.", "You have to fight the last monster to escape the city."]
    text_printing(text)
    print()
    continue_listener()
    clear()

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
        cmd = str(input("Choose your action (1/2/3): "))

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
                print()
                continue_listener()
                part_2(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)
            else:
                text = ["You try to run, but the monster catches you.", "The monster attacks you.", "You take 10 damage."]
                text_printing(text)
                hp -= 10

def fight_wolves(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    hp = 100
    enemy_hp = 25

    while True:
        clear()
        if hp <= 0:
            text = ["You have been killed by wolves."]
            text_printing(text)
            game_over(part_1)
        elif enemy_hp <= 0:
            text = ["You have defeated the wolves.", "You continue through the forest."]
            text_printing(text)
            break
        print("FIGHT: Wolves")
        print("Your HP: 100/100")
        print("Wolves' HP: 25/25")
        print("1. Attack")
        print("2. Defend")
        print("3. Run")
        cmd = str(input("Choose your action (1/2/3): "))

        if cmd == "1":
            text = ["You attack the wolves.", "The wolves take 10 damage."]
            text_printing(text)
            enemy_hp -= 10
            text = ["The wolves attack you.", "You take 5 damage."]
            text_printing(text)
            hp -= 5
        elif cmd == "2":
            text["You defend against the wolves' attack."]
            text_printing(text)
        elif cmd == "3":
            if randint(0, 100) <= GENERAL_SUCCESS_CHANCE:
                clear()
                text = ["You manage to run away from the wolves.", "You continue through the forest."]
                text_printing(text)
                print()
                continue_listener()
                break
            else:
                text = ["You try to run, but the wolves catch you.", "The wolves attack you.", "You take 10 damage."]
                text_printing(text)
                hp -= 10

def game_over(func, args_list=None):
    print("Game Over!")
    print("Would you like to try again?")
    cmd = str(input("Y/N: "))

    if cmd.lower() == "y":
        func(*args_list)
    else:
        sys.exit()

def chapter1(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    chapter_start()
    part_1(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)