from clear_terminal import clear
from input_listener import continue_listener
from text_printing import text_printing
from random import randint
import sys

def chapter_start():
    clear()
    print("CHAPTER 3")
    chapter_intro = ["Visions of the remaining shards fill your mind, each guarded by forces more dangerous than the last.", "But a shadowy figure lingers in your vision, whispering ominous words:", "The balance tilts.", "Beware the cost of power, for the more you claim, the greater the sacrifice.", "The temple fades into the distance as your journey continues toward the next shard."]
    text_printing(chapter_intro)
    continue_listener()
    clear()

    text = ["Guided by the vision from the first shard, you find yourself near a jungle.", "The second shard lies hidden within the depths of the jungle, protected by a tribe of shadowy beings called the Nyxaeri.", "These mysterious guardians test not only your courage but your willingness to confront darkness, both in the world and within yourself."]
    text_printing(text)
    continue_listener()
    clear()

def part_1(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    text = ["The air grows cooler as you approach the jungle.", "A heavy mist clings to the ground, obscuring the trail ahead.", "Strange whispers echo around you, though you see no one."]
    text_printing(text)
    continue_listener()
    clear()

    pos_answers = ["1", "2", "3", "follow", "walk", "wait", "follow the marked trail", "walk straight into the jungle", "wait and observe movements in the jungle"]
    while True:
        clear()
        text = ["Choose your method of entry:", "1. Follow the marked trail.", "2. Walk straight into the jungle.", "3. Wait and observe movements in the jungle."]
        text_printing(text, False)
        ans = str(input("Which option will you choose? (1/2/3): "))
        clear()

        if ans.strip().lower() in pos_answers:
            if ans == "1" or ans == "follow" or ans == "follow the marked trail":
                text = ["You follow the trail, the path winding deeper into the jungle.", "The mist grows thicker, the shadows darker.", "The whispers grow louder, more insistent."]
                text_printing(text)
                continue_listener()
                clear()

                pos_answers = ["1", "2", "hide", "sneak", "hide from the warrior", "sneak past the warrior"]
                while True:
                    clear()
                    text = ["Suddenly, you hear rustling in a bush near you.", "A Nyaxeri warrior steps out.", "You have to make a quick decision.", "You have two options:", "1. Hide", "2. Sneak past the warrior (Stealth)"]
                    text_printing(text, False)
                    ans = str(input("Which option will you choose? (1/2): "))
                    clear()

                    if ans.strip().lower() in pos_answers:
                        if ans == "1" or ans == "hide" or ans == "hide from the warrior":
                            text = ["You quickly hide behind a tree, your breath held.", "The warrior looks around but doesn't see you.", "You wait until the warrior moves on before continuing on your path."]
                            text_printing(text)
                            continue_listener()
                            clear()
                            break
                        elif ans == "2" or ans == "sneak" or ans == "sneak past the warrior":
                            if randint(1, 100) <= STEALTH_SUCCESS_CHANCE:
                                text = ["You try to sneak past the warrior, your footsteps silent.", "The warrior doesn't notice you, and you continue on your path."]
                                text_printing(text)
                                continue_listener()
                                clear()
                                break
                            else:
                                text = ["You try to sneak past the warrior, but you step on a twig.", "The warrior hears you and turns to face you.", "You decide it's best not to fight and let the warrior take you to their village."]
                                text_printing(text)
                                continue_listener()
                                clear()
                                break
                    else:
                        print("Invalid choice. Please try again.")
                        print()
                        continue_listener()
                text = ["You try to approach the village quietly, but the Nyaxeri warriors notice you.", "They immediately imprison you."]
                text_printing(text)
                continue_listener()
                clear()
                break
            elif ans == "2" or ans == "walk" or ans == "walk straight into the jungle":
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["You walk straight into the jungle, the mist growing thicker around you.", "The shadows deepen, and the whispers grow louder.", "You walk for what seems like hours, the path winding deeper into the jungle.", "Finally, you see a small village in the distance.", "You decide to approach the village."]
                    text_printing(text)
                    continue_listener()
                    clear()

                    text = ["As you approach the village, you see a group of Nyaxeri warriors standing guard.", "They immediately notice you and imprison you."]
                    text_printing(text)
                    continue_listener()
                    clear()
                    break
                else:
                    text = ["You walk straight into the jungle, the mist growing thicker around you.", "The shadows deepen, and the whispers grow louder.", "You walk for hours to no avail.", "You got lost in the jungle and never found your way out.", "You died."]
                    text_printing(text)
                    continue_listener()
                    clear()
                    game_over(part_1, [STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE])
            elif ans == "3" or ans == "wait" or ans == "wait and observe movements in the jungle":
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["You wait and observe movements in the jungle.", "You see a Nyaxeri warrior patrolling the area.", "You wait until the warrior passes and then continue on your path."]
                    text_printing(text)
                    continue_listener()
                    clear()

                    text = ["The mist grows thicker, the shadows darker.", "The whispers grow louder, more insistent.", "Finally, you see a small village in the distance.", "You decide to approach the village."]
                    text_printing(text)
                    continue_listener()
                    clear()

                    text = ["As you approach the village, you see a group of Nyaxeri warriors standing guard.", "They immediately notice you and imprison you."]
                    text_printing(text)
                    continue_listener()
                    clear()
                    break
                else:
                    text = ["You wait and observe movements in the jungle.", "You see a Nyaxeri warrior patrolling the area.", "You wait for the warrior to pass by.", "Suddenly, you feel a warm breath on your neck.", "A second warrior is standing right behind you.", "You decide it's best not to fight and let the warriors take you to their village."]
                    text_printing(text)
                    continue_listener()
                    clear()
                    break
        else:
            print("Invalid choice. Please try again.")
            print()
            continue_listener()

def part_2():
    text = ["You find yourself imprisoned in a dark, damp cell.", "The Nyaxeri warriors watch you closely, their eyes filled with suspicion.", "You know you must find a way to escape before it's too late."]
    text_printing(text)
    continue_listener()
    clear()

    text = ["You look around the cell, searching for a way out.", "You see a small window above your bed, blocked by iron bars.", "You also notice a loose stone in the wall near the door."]
    text_printing(text)
    continue_listener()

    pos_answers = ["1", "2", "window", "stone", "check out the window", "check out the loose stone in the wall"]
    while True:
        clear()
        text = ["What do you do:", "1. Check out the window.", "2. Check out the loose stone in the wall."]
        text_printing(text, False)
        ans = str(input("Which option will you choose? (1/2): "))
        clear()

        if ans.strip().lower() in pos_answers:
            if ans == "1" or ans == "window" or ans == "check out the window":
                text = ["You check out the window.", "You notice a small opening in the bars, just big enough for you to squeeze through.", "You decide to wait until nightfall to make your escape."]
                text_printing(text)
                continue_listener()
                clear()

                text = ["Night falls, and the Nyaxeri warriors grow lax in their guard.", "You make your escape through the window and into the jungle.", "You run as fast as you can, the sounds of pursuit growing fainter behind you.", "You finally reach the edge of the jungle and see the second shard in the distance."]
                text_printing(text)
                continue_listener()
                clear()
                break
            elif ans == "2" or ans == "stone" or ans == "check out the loose stone in the wall":
                text = ["You check out the loose stone in the wall.", "You push the stone aside and find a hidden passage behind it.", "You decide to wait until nightfall to make your escape."]
                text_printing(text)
                continue_listener()
                clear()

                text = ["Night falls, and the Nyaxeri warriors grow lax in their guard.", "You make your escape through the window and into the jungle.", "You run as fast as you can, the sounds of pursuit growing fainter behind you.", "You finally reach the edge of the jungle and see the second shard in the distance."]
                text_printing(text)
                continue_listener()
                clear()
                break
        else:
            print("Invalid choice. Please try again.")
            print()
            continue_listener()

def part_3(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    text = ["You come to a massive chasm spanned by a bridge of twisting shadows.", "The bridge feels alive, shifting beneath your feet as you step onto it.", "In the center of the bridge, a spectral figure appears—a warden of the Nyxaeri.", "The warden speaks in a voice that echoes through your mind:", "To claim the shard, you must prove your worth.", "Choose your path wisely, for the bridge will test your strength and intellect."]
    text_printing(text)
    continue_listener()
    clear()

    pos_answers = ["1", "2", "3", "fight", "riddle", "shard", "fight the warden", "solve the warden's riddle", "use the first shard to light the path"]
    while True:
        clear()
        text = ["You have three options:", "1. Fight the warden (Strength).", "2. Solve the warden's riddle (Intellect).", "3. Use the first shard to light the path."]
        text_printing(text, False)
        ans = str(input("Which option will you choose? (1/2/3): "))
        clear()

        if ans.strip().lower() in pos_answers:
            if ans == "1" or ans == "fight" or ans == "fight the warden":
                if randint(1, 100) <= STRENGTH_SUCCESS_CHANCE:
                    text = ["You decide to fight the warden, your muscles tensed for battle.", "The warden is a formidable opponent, but you manage to defeat it.", "The bridge shudders, and the shadows part, revealing the second shard."]
                    text_printing(text)
                    continue_listener()
                    clear()
                    break
                else:
                    text = ["You decide to fight the warden, your muscles tensed for battle.", "The warden is a formidable opponent, and you are no match for it.", "The warden strikes you down, and you fall into the chasm below.", "You died."]
                    text_printing(text)
                    continue_listener()
                    clear()
                    game_over(part_3, [STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE])
            elif ans == "2" or ans == "riddle" or ans == "solve the warden's riddle":
                if randint(1, 100) <= INTELLECT_SUCCESS_CHANCE:
                    text = ["You decide to solve the warden's riddle, your mind sharp and focused.", "The warden nods in approval, and the shadows part, revealing the second shard."]
                    text_printing(text)
                    continue_listener()
                    clear()
                    break
                else:
                    text = ["You decide to solve the warden's riddle, your mind sharp and focused.", "But the riddle proves too difficult, and the warden strikes you down.", "You fall into the chasm below.", "You died."]
                    text_printing(text)
                    continue_listener()
                    clear()
                    game_over(part_3, [STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE])
            elif ans == "3" or ans == "shard" or ans == "use the first shard to light the path":
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["You decide to use the first shard to light the path.", "The shard glows brightly, illuminating the bridge and dispelling the shadows.", "The warden nods in approval, and the shadows part, revealing the second shard."]
                    text_printing(text)
                    continue_listener()
                    clear()
                    break
                else:
                    text = ["You decide to use the first shard to light the path.", "But the shard flickers and dies, leaving you in darkness.", "The warden strikes you down, and you fall into the chasm below.", "You died."]
                    text_printing(text)
                    continue_listener()
                    clear()
                    game_over(part_3, [STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE])
        else:
            print("Invalid choice. Please try again.")
            print()
            continue_listener()

def part_4():
    text = ["You reach the second shard, its power pulsing beneath your fingertips.", "As you claim it, a vision fills your mind—a dark figure, wreathed in shadows, watching you from afar.", "The figure's eyes burn with malice, and you know that your journey is far from over."]
    text_printing(text)
    continue_listener()
    clear()

def game_over(func, args_list=None):
    print("Game Over!")
    print("Would you like to try again?")
    cmd = str(input("Y/N: "))

    if cmd.lower() == "y":
        func(*args_list)
    else:
        sys.exit()

def chapter3(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    clear()
    chapter_start()
    part_1(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)
    part_2()
    part_3(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)
    part_4()