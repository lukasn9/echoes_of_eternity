from clear_terminal import clear
from input_listener import continue_listener
from text_printing import text_printing
from random import randint
import sys

def chapter_start():
    clear()
    print("CHAPTER 5")
    chapter_intro = ["To Be Continued ..."]
    text_printing(chapter_intro)

def chapter5(STEALTH_SUCCESS_CHANCE, STRENGTH_SUCCESS_CHANCE, INTELLECT_SUCCESS_CHANCE, GENERAL_SUCCESS_CHANCE):
    chapter_start()