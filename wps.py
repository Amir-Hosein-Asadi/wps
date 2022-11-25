import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcom to the speed typing test!")
    stdscr.addstr("\npress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()
    
def wpm_test(stdscr):
    target_text = "hello world this is a test massage!"
    current_text = []
 
    while True:
        key = stdscr.getkey()
        current_text.append(key)
        
        
        stdscr.clear()
        stdscr.addstr(target_text)
        
        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))
            
        stdscr.refresh()    
        
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_RED)
    
    start_screen(stdscr)
    wpm_test(stdscr)
    
wrapper(main)
