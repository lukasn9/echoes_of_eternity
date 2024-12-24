from clear_terminal import clear
from input_listener import continue_listener
from text_printing import text_printing
from random import randint
import sys

def chapter_start():
    clear()
    print("CHAPTER 4")
    chapter_intro = [
        "The shards hum with energy, their pull guiding you toward the Stormlands.", "A desolate expanse ravaged by endless storms lies ahead, hiding an ancient labyrinth.", "Legends speak of the Labyrinth of Lost Echoes, where the final shard is said to rest.", "You brace yourself for the challenges that await."]
    text_printing(chapter_intro)
    continue_listener()
    clear()

def part1(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    text = ["Lightning splits the sky as you enter the Stormlands.", "Jagged cliffs and treacherous paths stretch out before you.", "You must decide how to proceed."]
    text_printing(text)
    continue_listener()
    clear()

    pos_answers = ["1", "2", "3", "path", "canyon", "shard", "follow the narrow path", "cut through the canyon", "use the shard"]
    while True:
        text = [
            "Choose your method of traversing the Stormlands:",
            "1. Follow a narrow but seemingly stable path along the cliffs.",
            "2. Cut through a rocky canyon for shelter from the storms.",
            "3. Use the Shard of Shadows to create a protective veil around yourself."]
        text_printing(text, False)
        ans = input("Which option will you choose? (1/2/3): ").strip().lower()
        clear()

        if ans in pos_answers:
            if ans in ["1", "path", "follow the narrow path"]:
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["You tread carefully along the narrow path, avoiding pitfalls.",
                            "The storms rage around you, but you make it through safely."]
                else:
                    text = ["A sudden surge of wind nearly knocks you off balance.",
                            "You manage to stay on the path, but your supplies are damaged."]
                text_printing(text)
                continue_listener()
                clear()
                break
            elif ans in ["2", "canyon", "cut through the canyon"]:
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["The canyon provides shelter from the worst of the storm.",
                            "You find a hidden cache of supplies, bolstering your inventory."]
                else:
                    text = ["Hostile creatures emerge from the shadows of the canyon.",
                            "You fight them off, but not without injury."]
                text_printing(text)
                continue_listener()
                clear()
                break
            elif ans in ["3", "shard", "use the shard"]:
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["The Shard of Shadows envelops you in a protective veil.",
                            "The storms seem to part in your wake, allowing you to pass unharmed."]
                else:
                    text = ["The shard’s energy flickers, leaving you exposed to the storm.",
                            "You push forward, but the shard’s power is temporarily weakened.",
                            "The storms rage around you, but you make it through in the end."]
                text_printing(text)
                continue_listener()
                clear()
                break
        else:
            print("Invalid choice. Please try again.")
            continue_listener()

def part2(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    text = [
        "The labyrinth looms ahead, its gates sealed by a glowing barrier.",
        "Three pedestals stand before the gates, each bearing an emblem: a flame, a tear, and a sword.",
        "You must find a way to break the barrier and enter."
    ]
    text_printing(text)
    continue_listener()
    clear()

    pos_answers = ["1", "2", "3", "align", "search", "force",
                   "align the shards", "search for another entrance", "brute force the barrier"]

    while True:
        text = [
            "Choose your method of breaking the barrier:",
            "1. Align the shards with the emblems.",
            "2. Search for an alternative entrance.",
            "3. Attempt to brute-force the barrier with your own strength."]
        text_printing(text, False)
        ans = input("Which option will you choose? (1/2/3): ").strip().lower()
        clear()

        if ans in pos_answers:
            if ans in ["1", "align", "align the shards"]:
                text = ["The shards resonate with the emblems, dissolving the barrier.",
                            "Their energy dims slightly, but you can now enter."]
                text_printing(text)
                continue_listener()
                clear()
                break

            elif ans in ["2", "search", "search for another entrance"]:
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["You discover a hidden tunnel leading into the labyrinth.",
                            "It’s narrow and dark, but it avoids the barrier."]
                else:
                    text = ["The tunnel is trapped, and you’re injured as you attempt to enter.", "You push through, determined to reach the other side."]
                text_printing(text)
                continue_listener()
                clear()
                break

            elif ans in ["3", "force", "brute force the barrier"]:
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["You channel all your strength into breaking the barrier.",
                            "The barrier cracks, granting you passage."]
                else:
                    text = ["The barrier resists your strength, its backlash injuring you.", "You finally break through, but at a cost."]
                text_printing(text)
                continue_listener()
                clear()
                break
        else:
            print("Invalid choice. Please try again.")
            continue_listener()

def part3(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    text = [
        "You enter the Whispering Plains, where soft voices seem to call your name.",
        "The air is thick with mystery, and the path ahead is obscured by a shimmering fog.",
        "You must decide how to proceed through this eerie terrain."
    ]
    text_printing(text)
    continue_listener()
    clear()

    pos_answers = ["1", "2", "3", "listen", "ignore", "signal",
                   "listen to the whispers", "ignore the voices", "send a signal"]

    while True:
        text = [
            "Choose your method of navigating the Whispering Plains:",
            "1. Listen closely to the whispers for guidance.",
            "2. Ignore the voices and press forward blindly.",
            "3. Use the Shard of Shadows to send out a signal and reveal the true path."]
        text_printing(text, False)
        ans = input("Which option will you choose? (1/2/3): ").strip().lower()
        clear()

        if ans in pos_answers:
            if ans in ["1", "listen", "listen to the whispers"]:
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["The whispers guide you safely through the fog.",
                            "You emerge unscathed on the other side of the plains."]
                else:
                    text = ["The whispers lead you in circles, wasting precious time.",
                            "You finally find your way, but you are exhausted."]
                text_printing(text)
                continue_listener()
                clear()
                break

            elif ans in ["2", "ignore", "ignore the voices"]:
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["You steel your resolve and march through the fog.",
                            "Despite the whispers, you find your way."]
                else:
                    text = ["Ignoring the voices, you trip over hidden obstacles.",
                            "Your journey through the plains leaves you battered."]
                text_printing(text)
                continue_listener()
                clear()
                break

            elif ans in ["3", "signal", "send a signal"]:
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["The shard’s signal clears the fog, revealing the path ahead.",
                            "You move forward with confidence."]
                else:
                    text = ["The shard’s signal falters, leaving you vulnerable in the fog.",
                            "You stumble through, enduring minor injuries."]
                text_printing(text)
                continue_listener()
                clear()
                break
        else:
            print("Invalid choice. Please try again.")
            continue_listener()

def part4(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    text = [
        "Inside the labyrinth, you encounter the Twisting Corridors, a series of ever-shifting passages.",
        "The walls seem alive, rearranging themselves to confound intruders.",
        "You must use your wits to navigate this disorienting maze."
    ]
    text_printing(text)
    continue_listener()
    clear()

    pos_answers = ["1", "2", "3", "mark", "map", "shard",
                   "mark the walls", "consult a map", "use the shard"]

    while True:
        text = [
            "Choose your method of navigating the Twisting Corridors:",
            "1. Mark the walls as you go to avoid backtracking.",
            "2. Consult an ancient map of the labyrinth you found earlier.",
            "3. Use the Shard of Shadows to illuminate the correct path."
        ]
        text_printing(text, False)
        ans = input("Which option will you choose? (1/2/3): ").strip().lower()
        clear()

        if ans in pos_answers:
            if ans in ["1", "mark", "mark the walls"]:
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["Your markings help you keep track of your path, avoiding dead ends.",
                            "You navigate the corridors successfully."]
                else:
                    text = ["The shifting walls erase your markings, leaving you lost.",
                            "You eventually find your way, but at great cost to your energy."]
                text_printing(text)
                continue_listener()
                clear()
                break

            elif ans in ["2", "map", "consult a map"]:
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["The map reveals the labyrinth’s layout, guiding you through.",
                            "You move forward with renewed confidence."]
                else:
                    text = ["The map is outdated and leads you into traps.",
                            "You struggle to recover, but press on."]
                text_printing(text)
                continue_listener()
                clear()
                break

            elif ans in ["3", "shard", "use the shard"]:
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["The shard’s energy highlights the correct paths, bypassing the traps.",
                            "You navigate the corridors with ease."]
                else:
                    text = ["The shard’s glow dims unexpectedly, leaving you vulnerable.",
                            "You press on, but with heightened caution."]
                text_printing(text)
                continue_listener()
                clear()
                break
        else:
            print("Invalid choice. Please try again.")
            continue_listener()

def part5(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    text = [
        "You step into the Hall of Illusions, where mirrors line the walls.",
        "Reflections shift and change, showing distorted versions of yourself and your journey.",
        "You must confront these illusions to move forward."
    ]
    text_printing(text)
    continue_listener()
    clear()

    pos_answers = ["1", "2", "3", "face", "destroy", "ignore",
                   "face the illusions", "destroy the mirrors", "ignore the reflections"]

    while True:
        text = [
            "Choose your method of dealing with the illusions:",
            "1. Face the illusions and attempt to understand their meaning.",
            "2. Destroy the mirrors to eliminate the source of the illusions.",
            "3. Ignore the reflections and focus on finding the exit."
        ]
        text_printing(text, False)
        ans = input("Which option will you choose? (1/2/3): ").strip().lower()
        clear()

        if ans in pos_answers:
            if ans in ["1", "face", "face the illusions"]:
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["You confront the illusions, gaining insight into your fears and strengths.",
                            "The path ahead becomes clear."]
                else:
                    text = ["The illusions overwhelm you, shaking your resolve.",
                            "You press on, but with lingering doubts."]
                text_printing(text)
                continue_listener()
                clear()
                break

            elif ans in ["2", "destroy", "destroy the mirrors"]:
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["The mirrors shatter, dispelling the illusions.",
                            "The room’s true layout is revealed, allowing you to proceed."]
                else:
                    text = ["The shattered mirrors release a blinding light, disorienting you.",
                            "You recover and find the exit, but not without difficulty."]
                text_printing(text)
                continue_listener()
                clear()
                break

            elif ans in ["3", "ignore", "ignore the reflections"]:
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["You block out the illusions and focus on the path ahead.",
                            "Your determination leads you to the exit."]
                else:
                    text = ["The illusions attempt to distract you, causing you to lose time.",
                            "You find the exit, but at a cost to your morale."]
                text_printing(text)
                continue_listener()
                clear()
                break
        else:
            print("Invalid choice. Please try again.")
            continue_listener()

def part6(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    text = [
        "At the heart of the labyrinth lies the Guardian’s Trial.",
        "A towering figure emerges, its voice resonating through the chamber:",
        "'To claim the shard, you must prove your worth.'",
        "The Guardian readies its challenge."
    ]
    text_printing(text)
    continue_listener()
    clear()

    pos_answers = ["1", "2", "3", "fight", "riddle", "shard",
                   "challenge the guardian in combat", "solve the guardian’s riddle", "use the shard"]

    while True:
        text = [
            "Choose your method of completing the Guardian’s Trial:",
            "1. Challenge the Guardian in combat.",
            "2. Solve the Guardian’s riddle.",
            "3. Use the Shard of Shadows to bypass the trial."
        ]
        text_printing(text, False)
        ans = input("Which option will you choose? (1/2/3): ").strip().lower()
        clear()

        if ans in pos_answers:
            if ans in ["1", "fight", "challenge the guardian in combat"]:
                text = ["You engage the Guardian in a fierce battle and emerge victorious.",
                            "The shard is now within your grasp."]
                text_printing(text)
                continue_listener()
                clear()
                break

            elif ans in ["2", "riddle", "solve the guardian’s riddle"]:
                text = ["You unravel the Guardian’s riddle with ease, impressing it.",
                            "It steps aside, granting you the shard."]
                text_printing(text)
                continue_listener()
                clear()
                break

            elif ans in ["3", "shard", "use the shard"]:
                if randint(1, 100) <= GENERAL_SUCCESS_CHANCE:
                    text = ["The Shard of Shadows envelops the Guardian, rendering it powerless.",
                            "You seize the shard and leave the chamber unopposed."]
                else:
                    text = ["The shard’s power falters, provoking the Guardian’s wrath.", "You narrowly escape, with the shard in hand."]
                text_printing(text)
                continue_listener()
                clear()
                break

def chapter4(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    chapter_start()
    part1(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)
    part2(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)
    part3(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)
    part4(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)
    part5(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)
    part6(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)