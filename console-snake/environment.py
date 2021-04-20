import time
import random
from .entities import Snake, Food
class Environment:

    game_speed = 0.2

    def __init__(self, width:int=32, height:int=12, gui:'GUI'=None):
        self.width = width
        self.height = height
        self.gui = gui
        
    def bind_gui(self, gui:'GUI'):
        self.gui = gui

    def bind_controller(self, controller:'PlayerController'):
        self.controller = controller

    def spawn_snake(self):
        self.snake = Snake(env=self)
        self.snake.spawn()

    def spawn_food(self):
        x = random.randint(0, self.width)
        y = random.randint(0, self.height)

        # to make sure the food dont spawn on top of the snake
        if (x, y) not in list(self.snake.positions):
            value = random.choice([1, 1, 1, 1, 3])
            self.food = Food(self)
            self.food.spawn(x, y, value)
        else:
            self.spawn_food()


    def reset(self):
        self.score = 0

        self.spawn_snake()
        self.spawn_food()
        try:
            self.controller.target_direction = self.snake.direction
        except Exception as e:
            raise e

        return self.snake.is_alive, self.snake.head

    def out_of_bounds_check(self):
        '''
            checks if snake hits boundaries
        '''
        if (self.snake.head[0] < 0 or self.snake.head[0] > self.width or 
            self.snake.head[1] < 0 or self.snake.head[1] > self.height):
            self.snake.is_alive = False

    def food_eat_check(self):
        '''
            checks if snake eats food
        '''
        if self.snake.head == self.food.position:
            self.snake.eat(self.food.value)
            self.score += self.food.value
            self.spawn_food()

    def self_eat_check(self):
        '''
            checks if snake hits self
        '''
        if self.snake.head in list(self.snake.positions)[:-1]:
            self.snake.is_alive = False

    def update_gui(self):
        try:
            self.gui.update()
        except AttributeError:
            pass
        except Exception as e:
            raise e

    def check_input(self):
        try:
            self.snake.turn(self.controller.target_direction)
        except Exception as e:
            raise e

    def step(self):
        self.check_input()
        self.snake.move()

        self.food_eat_check()
        self.out_of_bounds_check()
        self.self_eat_check()

        self.update_gui()

        time.sleep(self.game_speed)

        return self.snake.is_alive, self.snake.head