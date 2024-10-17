import curses

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Hello, World!")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
