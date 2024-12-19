from clear_terminal import clear
from text_printing import text_printing
from input_listener import continue_listener
import sys
from random import randint
from .chapter3 import chapter3

def chapter_start():
    clear()
    print("CHAPTER 2")
    chapter_intro = ["After hours of walking, you finally reach the temple.", "You can feel the presence of the first shard", "As you enter the temple, you wonder what awaits you inside."]
    text_printing(chapter_intro)
    continue_listener()

def part_1(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    clear()
    text = ["You step into a grand hall, where a large door blocks your path.", "Five glowing glyphs with symbols on them float in front of the door.", "The glyphs form a puzzle that requires deep focus to solve."]
    text_printing(text)
    continue_listener()
    clear()

    text = ["You fiddle with the glyphs, trying to figure out the correct order.", "You figure out that once a glyph is in the correct position, it will glow brighter.", "You have to solve the puzzle to proceed."]
    text_printing(text)
    continue_listener()
    clear()

    correct_answer = ["wave", "star", "moon", "sun", "cloud"]
    current_answer = ["sun", "moon", "star", "cloud", "wave"]
    temp = ""
    pos_answers = [1, 2, 3, 4, 5]
    while True:
        if current_answer == correct_answer:
            text = ["The door opens, revealing a dark corridor.", "You step inside, ready to face whatever lies ahead."]
            text_printing(text)
            continue_listener()
            clear()
            break

        for i in range(len(current_answer)):
            if current_answer[i] == correct_answer[i]:
                text = ["The " + current_answer[i] + " glyph is glowing."]
                text_printing(text, False)
            else:
                text = ["The " + current_answer[i] + " glyph is not glowing."]
                text_printing(text, False)
        print()
        continue_listener()
        clear()
        text = ["You have five options:", "1. Pick up the sun glyph.", "2. Pick up the moon glyph.", "3. Pick up the star glyph.", "4. Pick up the cloud glyph.", "5. Pick up the wave glyph."]
        text_printing(text, False)
        ans = str(input("Which option will you choose? (1/2/3/4/5): "))
        clear()

        ans = int(ans)
        if ans in pos_answers:
            match ans:
                case 1:
                    text = [f"You pick up the {current_answer[0]} glyph.", "You can swap it with another glyph."]
                    text_printing(text)
                    continue_listener()
                    while True:
                        clear()
                        text = ["You have four options:", f"1. Switch the {current_answer[0]} glyph with the {current_answer[1]} glyph.", f"2. Switch the {current_answer[0]} glyph with the {current_answer[2]} glyph.", f"3. Switch the {current_answer[0]} glyph with the {current_answer[3]} glyph.", f"4. Switch the {current_answer[0]} glyph with the {current_answer[4]} glyph."]
                        text_printing(text, False)
                        ans = str(input("Which option will you choose? (1/2/3/4): "))
                        clear()

                        ans = int(ans)
                        if ans in pos_answers:
                            match ans:
                                case 1:
                                    text = [f"You switch the {current_answer[0]} glyph with the {current_answer[1]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[0]
                                    current_answer[0] = current_answer[1]
                                    current_answer[1] = temp
                                    break
                                case 2:
                                    text = [f"You switch the {current_answer[0]} glyph with the {current_answer[2]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[0]
                                    current_answer[0] = current_answer[2]
                                    current_answer[2] = temp
                                    break
                                case 3:
                                    text = [f"You switch the {current_answer[0]} glyph with the {current_answer[3]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[0]
                                    current_answer[0] = current_answer[3]
                                    current_answer[3] = temp
                                    break
                                case 4:
                                    text = [f"You switch the {current_answer[0]} glyph with the {current_answer[4]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[0]
                                    current_answer[0] = current_answer[4]
                                    current_answer[4] = temp
                                    break
                        else:
                            print("Invalid choice. Please try again.")
                            continue_listener()
                case 2:
                    text = [f"You pick up the {current_answer[1]} glyph.", "You can swap it with another glyph."]
                    text_printing(text)
                    continue_listener()
                    while True:
                        clear()
                        text = ["You have four options:", f"1. Switch the {current_answer[1]} glyph with the {current_answer[0]} glyph.", f"2. Switch the {current_answer[1]} glyph with the {current_answer[2]} glyph.", f"3. Switch the {current_answer[1]} glyph with the {current_answer[3]} glyph.", f"4. Switch the {current_answer[1]} glyph with the {current_answer[4]} glyph."]
                        text_printing(text, False)
                        ans = str(input("Which option will you choose? (1/2/3/4): "))
                        clear()

                        ans = int(ans)
                        if ans in pos_answers:
                            match ans:
                                case 1:
                                    text = [f"You switch the {current_answer[1]} glyph with the {current_answer[0]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[1]
                                    current_answer[1] = current_answer[0]
                                    current_answer[0] = temp
                                    break
                                case 2:
                                    text = [f"You switch the {current_answer[1]} glyph with the {current_answer[2]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[1]
                                    current_answer[1] = current_answer[2]
                                    current_answer[2] = temp
                                    break
                                case 3:
                                    text = [f"You switch the {current_answer[1]} glyph with the {current_answer[3]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[1]
                                    current_answer[1] = current_answer[3]
                                    current_answer[3] = temp
                                    break
                                case 4:
                                    text = [f"You switch the {current_answer[1]} glyph with the {current_answer[4]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[1]
                                    current_answer[1] = current_answer[4]
                                    current_answer[4] = temp
                                    break
                        else:
                            print("Invalid choice. Please try again.")
                            continue_listener()
                case 3:
                    text = [f"You pick up the {current_answer[2]} glyph.", "You can swap it with another glyph."]
                    text_printing(text)
                    continue_listener()
                    while True:
                        clear()
                        text = ["You have four options:", f"1. Switch the {current_answer[2]} glyph with the {current_answer[0]} glyph.", f"2. Switch the {current_answer[2]} glyph with the {current_answer[1]} glyph.", f"3. Switch the {current_answer[2]} glyph with the {current_answer[3]} glyph.", f"4. Switch the {current_answer[2]} glyph with the {current_answer[4]} glyph."]
                        text_printing(text, False)
                        ans = str(input("Which option will you choose? (1/2/3/4): "))
                        clear()

                        ans = int(ans)
                        if ans in pos_answers:
                            match ans:
                                case 1:
                                    text = [f"You switch the {current_answer[2]} glyph with the {current_answer[0]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[2]
                                    current_answer[2] = current_answer[0]
                                    current_answer[0] = temp
                                    break
                                case 2:
                                    text = [f"You switch the {current_answer[2]} glyph with the {current_answer[1]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[2]
                                    current_answer[2] = current_answer[1]
                                    current_answer[1] = temp
                                    break
                                case 3:
                                    text = [f"You switch the {current_answer[2]} glyph with the {current_answer[3]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[2]
                                    current_answer[2] = current_answer[3]
                                    current_answer[3] = temp
                                    break
                                case 4:
                                    text = [f"You switch the {current_answer[2]} glyph with the {current_answer[4]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[2]
                                    current_answer[2] = current_answer[4]
                                    current_answer[4] = temp
                                    break
                        else:
                            print("Invalid choice. Please try again.")
                            continue_listener()
                case 4:
                    text = [f"You pick up the {current_answer[3]} glyph.", "You can swap it with another glyph."]
                    text_printing(text)
                    continue_listener()
                    while True:
                        clear()
                        text = ["You have four options:", f"1. Switch the {current_answer[3]} glyph with the {current_answer[0]} glyph.", f"2. Switch the {current_answer[3]} glyph with the {current_answer[1]} glyph.", f"3. Switch the {current_answer[3]} glyph with the {current_answer[2]} glyph.", f"4. Switch the {current_answer[0]} glyph with the {current_answer[4]} glyph."]
                        text_printing(text, False)
                        ans = str(input("Which option will you choose? (1/2/3/4): "))
                        clear()

                        ans = int(ans)
                        if ans in pos_answers:
                            match ans:
                                case 1:
                                    text = [f"You switch the {current_answer[3]} glyph with the {current_answer[0]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[3]
                                    current_answer[3] = current_answer[0]
                                    current_answer[0] = temp
                                    break
                                case 2:
                                    text = [f"You switch the {current_answer[3]} glyph with the {current_answer[1]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[3]
                                    current_answer[3] = current_answer[1]
                                    current_answer[1] = temp
                                    break
                                case 3:
                                    text = [f"You switch the {current_answer[3]} glyph with the {current_answer[2]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[3]
                                    current_answer[3] = current_answer[2]
                                    current_answer[2] = temp
                                    break
                                case 4:
                                    text = [f"You switch the {current_answer[3]} glyph with the {current_answer[4]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[3]
                                    current_answer[3] = current_answer[4]
                                    current_answer[4] = temp
                                    break
                        else:
                            print("Invalid choice. Please try again.")
                            continue_listener()
                case 5:
                    text = [f"You pick up the {current_answer[4]} glyph.", "You can swap it with another glyph."]
                    text_printing(text)
                    continue_listener()
                    while True:
                        clear()
                        text = ["You have four options:", f"1. Switch the {current_answer[4]} glyph with the {current_answer[0]} glyph.", f"2. Switch the {current_answer[4]} glyph with the {current_answer[1]} glyph.", f"3. Switch the {current_answer[4]} glyph with the {current_answer[2]} glyph.", f"4. Switch the {current_answer[4]} glyph with the {current_answer[3]} glyph."]
                        text_printing(text, False)
                        ans = str(input("Which option will you choose? (1/2/3/4): "))
                        clear()

                        ans = int(ans)
                        if ans in pos_answers:
                            match ans:
                                case 1:
                                    text = [f"You switch the {current_answer[4]} glyph with the {current_answer[0]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[4]
                                    current_answer[4] = current_answer[0]
                                    current_answer[0] = temp
                                    break
                                case 2:
                                    text = [f"You switch the {current_answer[4]} glyph with the {current_answer[1]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[4]
                                    current_answer[4] = current_answer[1]
                                    current_answer[1] = temp
                                    break
                                case 3:
                                    text = [f"You switch the {current_answer[4]} glyph with the {current_answer[2]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[4]
                                    current_answer[4] = current_answer[2]
                                    current_answer[2] = temp
                                    break
                                case 4:
                                    text = [f"You switch the {current_answer[4]} glyph with the {current_answer[3]} glyph."]
                                    text_printing(text)
                                    temp = current_answer[4]
                                    current_answer[4] = current_answer[3]
                                    current_answer[3] = temp
                                    break
                        else:
                            print("Invalid choice. Please try again.")
                            continue_listener()
        else:
            print("Invalid choice. Please try again.")
            continue_listener()
    part_2(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)

def part_2(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    text = ["Beyond the door lies a glowing bridge suspended over an endless void.", "As you step onto it, the bridge reflects your image, which steps forward to confront you."]
    text_printing(text)
    text = ["Your reflection speaks:", "To claim the Shard of Dawn, you must face yourself.", "Only the worthy may proceed."]
    text_printing(text)
    continue_listener()
    clear()

    pos_answers = ["1", "2", "3", "fight", "reason", "observe", "fight your reflection", "reason with your reflection", "observe and mirror the reflection’s movements"]
    while True:
        clear()
        text = ["You have three options:", "1. Fight your reflection", "2. Try to reason with your reflection (Intellect)", "3. Observe and mirror the reflection’s movements (Stealth)"]
        text_printing(text, False)
        ans = str(input("Which option will you choose? (1/2/3): "))
        clear()

        if ans.strip().lower() in pos_answers:
            if ans == "1" or ans == "fight" or ans == "fight your reflection":
                text = ["You decide to fight your reflection."]
                text_printing(text)
                continue_listener()
                fight_reflection(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)
                break
            elif ans == "2" or ans == "reason" or ans == "reason with your reflection":
                if randint(0, 100) <= INTELLECT_SUCCESS_CHANCE / 2:
                    text = ["You try to reason with your reflection.", "Your reflection listens to you.", "It steps aside, allowing you to pass."]
                    text_printing(text)
                    continue_listener()
                    break
                else:
                    text = ["You try to reason with your reflection.", "Your attempt makes it angry and twice as strong."]
                    text_printing(text)
                    continue_listener()
                    fight_reflection(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE, HP=200)
                    break
            elif ans == "3" or ans == "observe" or ans == "observe and mirror the reflection’s movements":
                if randint(0, 100) <= STEALTH_SUCCESS_CHANCE / 2:
                    text = ["You observe your reflection’s movements.", "You mirror its movements perfectly.", "The reflection steps aside, allowing you to pass."]
                    text_printing(text)
                    continue_listener()
                    break
                else:
                    text = ["You observe your reflection’s movements.", "You fail to mirror its movements.", "The reflection attacks you."]
                    text_printing(text)
                    continue_listener()
                    fight_reflection(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)
                    break
        else:
            print("Invalid choice. Please try again.")
            print()
            continue_listener()

    part_3(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)

def part_3(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    text = ["The final chamber is a vast circular room, its walls covered in ancient murals of the world’s creation.", "At the center, the first shard hovers within a beam of light, protected by a crumbling but still formidable stone guardian."]
    text_printing(text)
    continue_listener()
    text = ["The guardian awakens, its eyes glowing with power.", "It speaks:", "Only the worthy may claim the shard.", "Prove yourself in combat."]
    text_printing(text)
    continue_listener()
    fight_guardian(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)

    text = ["You have defeated the guardian.", "The first shard is finally yours.",  "Just two more to go.", "You set off to find the next shard."]
    text_printing(text)
    continue_listener()

    chapter3(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)

def fight_reflection(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE, HP=100):
    clear()

    hp = 100
    enemy_hp = HP

    while True:
        clear()
        if hp <= 0:
            text = ["You have been killed by the reflection."]
            text_printing(text)
            game_over(part_1)
        elif enemy_hp <= 0:
            text = ["You have defeated the reflection."]
            text_printing(text)
            break
        print("FIGHT: Your Reflection")
        print(f"Your HP: {hp}/100")
        print(f"Reflection's HP: {enemy_hp}/{HP}")
        print("1. Attack")
        print("2. Defend")
        print("3. Run")
        cmd = str(input("Choose your action (1/2/3): "))

        if cmd == "1":
            clear()
            if randint(0, 100) <= STRENGTH_SUCCESS_CHANCE * 0.75:
                text = ["You hit the reflection with all your strength.", "The reflection takes 20 damage."]
                text_printing(text)
                enemy_hp -= 20
                text = ["The reflection attacks you.", "You take 5 damage."]
                text_printing(text)
                hp -= 5
                continue_listener()
            else:
                text = ["You attack the reflection.", "The reflection takes 10 damage."]
                text_printing(text)
                enemy_hp -= 10
                text = ["The reflection attacks you.", "You take 5 damage."]
                text_printing(text)
                hp -= 5
                continue_listener()
        elif cmd == "2":
            clear()
            text["You defend against the reflection's attack."]
            text_printing(text)
            continue_listener()
        elif cmd == "3":
            if randint(0, 100) <= GENERAL_SUCCESS_CHANCE / 2:
                clear()
                text = ["You manage to run away from the reflection.", "You successfully escape the city."]
                text_printing(text)
                continue_listener()
                part_2(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)
            else:
                clear()
                text = ["You try to run, but the reflection catches you.", "The reflection attacks you.", "You take 10 damage."]
                text_printing(text)
                hp -= 10
                continue_listener()

def fight_guardian(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE, HP=300):
    clear()

    hp = 100
    enemy_hp = HP

    while True:
        clear()
        if hp <= 0:
            text = ["You have been killed by the guardian."]
            text_printing(text)
            game_over(part_1)
        elif enemy_hp <= 0:
            text = ["You have defeated the guardian."]
            text_printing(text)
            break
        print("FIGHT: Guardian")
        print(f"Your HP: {hp}/100")
        print(f"Guardian's HP: {enemy_hp}/{HP}")
        print("1. Attack")
        print("2. Defend")
        cmd = str(input("Choose your action (1/2/3): "))

        if cmd == "1":
            clear()
            if randint(0, 100) <= STRENGTH_SUCCESS_CHANCE * 0.75:
                text = ["You hit the guardian with all your strength.", "The guardian takes 20 damage."]
                text_printing(text)
                enemy_hp -= 20
                if randint(0, 100) <= GENERAL_SUCCESS_CHANCE / 0.75:
                    text = ["The guardian attacks you and misses."]
                    text_printing(text)
                    continue_listener()
                else:
                    text = ["The guardian attacks you.", "You take 5 damage."]
                    text_printing(text)
                    hp -= 5
                    continue_listener()
            else:
                text = ["You attack the guardian.", "The guardian takes 10 damage."]
                text_printing(text)
                enemy_hp -= 10
                if randint(0, 100) <= GENERAL_SUCCESS_CHANCE / 0.75:
                    text = ["The guardian attacks you and misses."]
                    text_printing(text)
                    continue_listener()
                else:
                    text = ["The guardian attacks you.", "You take 5 damage."]
                    text_printing(text)
                    hp -= 5
                    continue_listener()
        elif cmd == "2":
            clear()
            text["You defend against the guardian's attack."]
            text_printing(text)
            continue_listener()

def game_over(func, args_list=None):
    print("Game Over!")
    print("Would you like to try again?")
    cmd = str(input("Y/N: "))

    if cmd.lower() == "y":
        func(*args_list)
    else:
        sys.exit()

def chapter2(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    clear()
    chapter_start()
    part_1(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE)