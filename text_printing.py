from time import sleep

def text_printing(text, newline=True):
    for line in text:
        for i in range(len(line)):
            print(line[i], end="", flush=True)
            sleep(0.015)
        print("")
    if newline:
        print()