import curses
from pynput import keyboard
from snake.environment import Environment

class GUI:

    begin_x = 0
    begin_y = 0

    def __init__(self, env:Environment):
        self.env = env
        self.env.bind_gui(self)

        self.height = env.height + 3
        self.width = env.width + 3

        self._init_curses()

    def _init_curses(self):
        self.stdscr = curses.initscr()
        self.win = curses.newwin(self.height, self.width, self.begin_y, self.begin_x)
        self.win.keypad(True)
        curses.nocbreak()
        curses.noecho()
        curses.curs_set(False)

    def _terminate_curses(self):
        curses.endwin()

    def _draw_snake(self):
        # draw body
        for x, y in list(self.env.snake.positions)[:-1]:
            self.win.addstr(y+1, x+1, '*')
        
        # draw head
        x, y = self.env.snake.head
        direction = self.env.snake.direction
        if direction == self.env.snake.direction.up:
            self.win.addstr(y+1, x+1, '^')
        elif direction == self.env.snake.direction.down:
            self.win.addstr(y+1, x+1, 'V')
        elif direction == self.env.snake.direction.left:
            self.win.addstr(y+1, x+1, '<')
        elif direction == self.env.snake.direction.right:
            self.win.addstr(y+1, x+1, '>')

    def _draw_food(self):
        x, y = self.env.food.position
        food_str = 'o' if self.env.food.type == self.env.food.types.small else '@'
        self.win.addstr(y+1, x+1, food_str)

    def _show_score(self):
        self.win.addstr(0, 1, f'score: {self.env.score}')

    def update(self):
        self.win.clear()
        self.win.border()
        self._draw_snake()
        self._draw_food()
        self._show_score()
        self.win.refresh()

