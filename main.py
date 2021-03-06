import os
import random
import cursor
from Trail import Trail
from msvcrt import kbhit, getch

def kbin():
    global running
    if kbhit():
        ch = getch().decode('utf-8')
        if ch == 'q':
            running = False

def main():
    global running
    cursor.hide()
    os.system('mode con: cols=30 lines=15')
    os.system("cls")
    width, height = os.get_terminal_size()
    trails = [Trail(width, height, x, random.randrange(1, height)) for x in range(1, width + 1)]
    running = True
    while running:
        for trail in trails:
            trail.draw()
            trail.update()
        kbin()
    Trail.gotoxy(1, height-1)
    cursor.show()
    os.system('mode con: cols=165 lines=42')

if __name__ == '__main__':
    main()
