import curses
import time


doors = """


                          Make a choice by a mouse click.



                    +                                       +
                    |\                                     /|
                    | \                                   / |
                    |  +-------+                 +-------+  |
                    |  |       |                 |       |  |
                    |  |       |                 |       |  |
                    |  |       |                 |       |  |
                    |  |       |                 |       |  |
                    |  |       |                 |       |  |
                    |  |       |                 |       |  |
--------------------|  +-------+-----------------+-------+  |-------------------
                    | /                                   \ |
                    |/                                     \|
                    +                                       +


               +-------------------------------------------------+
               |                                                 |
               |  When Stanley came to a set of two open doors,  |
               |        he entered the door on his left.         |
               |                                                 |
               +-------------------------------------------------+

"""

left = """
               +-------------------------------------------------+
               | Yet, there was not a single person here either. |
               | Feeling a wave of disbelief, Stanley decided to |
               | go up to his boss’s office hoping he might find |
               |                 an answer there.                |
               +-------------------------------------------------+
"""

right = """
               +-------------------------------------------------+
               |   This was not the correct way to the meeting   |
               |    room, and Stanley knew it prefectly well.    |
               |    Perhaps he wanted to stop by the employee    |
               |         lounge first, just to admire it.        |
               +-------------------------------------------------+
"""

floor = "--------------------|  +-------+-----------------+-------+  |-------------------"

timer = 100

def main(win: curses.window):
    global timer
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    rows, cols = win.getmaxyx()
    print(rows, cols)
    curses.resize_term(41, 81)
    win.resize(41, 81)
    win.clear()
    win.keypad(1)
    rows, cols = win.getmaxyx()
    print(rows, cols)

    syms = "бӬѮѼѦѬѢҊҖҨԆ҂ϾϿΨϞϘΩϗƛæټ©¿¶☆★"
    for idx, sym in enumerate(syms):
        x = idx % 8
        y = idx // 8
        win.addstr(1 + y * 2, 1 + 4 * x, f"+---+")
        win.addstr(2 + y * 2, 1 + 4 * x, f"| {sym} |")
        win.addstr(3 + y * 2, 1 + 4 * x, f"+---+")

    win.addstr(11, 1, "Can you see all the symbols above\n with the boxes aligned properly?")
    win.addstr(14, 1, "Press any key to continue...")
    win.getch()

    win.nodelay(1)
    curses.mousemask(curses.REPORT_MOUSE_POSITION | curses.ALL_MOUSE_EVENTS)

    win.clear()
    win.addstr(0, 0, doors)
    win.refresh()

    while True:
        win.addstr(17, 0, floor, curses.color_pair(1 + (timer // 5) % 2))
        ch = win.getch()
        timer -= 1
        if timer == 0:
            break
        win.addstr(10, 1, f"Timer: [{timer}]")
        if ch == curses.KEY_MOUSE:
            # win.clear()
            m0, mx, my, mz, bstd = curses.getmouse()
            win.addstr(1, 0, f"[DEBUG: {ch} - {mx}, {my}]")
            if 25 <= mx <= 33 and 10 <= my <= 17:
                win.clear()
                win.addstr(my, mx, "*LEFT")
                win.addstr(18, 0, left)
                win.refresh()
                break
            elif 50 <= mx <= 58 and 10 <= my <= 17:
                win.clear()
                win.addstr(my, mx, "*RIGHT")
                win.addstr(18, 0, right)
                win.refresh()
                break
            win.refresh()
        elif ch==-1:
            win.addstr(0,0,f"[DEBUG: {ch}, time={time.time()}]")
            win.refresh()
        elif ch == ord('q'):
            break
        else:
            win.addstr(1,0,f"[DEBUG: {ch}, {chr(ch)}]")
            win.refresh()

        curses.napms(100)

    if timer == 0:
        win.addstr(2, 35, "Timed out.")
    win.addstr(4, 28, "Press any key to exit...")
    curses.mousemask(0)
    win.nodelay(0)
    win.getch()

curses.wrapper(main)
