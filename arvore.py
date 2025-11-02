import time
import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_tree():
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m']  # Cores ANSI
    reset = '\033[0m'

    tree = [
        "        *        ",  # Estrela
        "       ***       ",
        "      *****      ",
        "     *******     ",
        "    *********    ",
        "   ***********   ",
        "  *************  ",
        " *************** ",
        "       |||       "
    ]

    while True:
        clear()
        for i, line in enumerate(tree):
            if i == 0:
                print('\033[93m' + line + reset)  # Estrela amarela
            else:
                colored_line = ''
                for char in line:
                    if char == '*':
                        colored_line += random.choice(colors) + '*' + reset
                    else:
                        colored_line += char
                print(colored_line)
        time.sleep(0.5)

draw_tree()