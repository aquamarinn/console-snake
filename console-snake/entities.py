import random
from collections import deque
from enum import Enum

class Snake:

    class directions(Enum):
        up = -1
        down = 1
        left = -2
        right = 2

    def __init__(self, env:'Environment'):
        self.env = env

    def spawn(self, length:int=3):
        '''
            spawns the snake in a random position in the env; facing a random direction
        '''
        self.is_alive = True
        self.length = length if length >= 3 else 3
        self.positions = deque([], self.length)
        
        self.x = random.randint(self.length+3, self.env.width-self.length-3)
        self.y = random.randint(self.length+3, self.env.height-self.length-3)
        
        self.positions.append((self.x, self.y))
        self.direction = random.choice(list(self.directions)) # current direction

    @property
    def head(self):
        return self.positions[-1]

    def move(self):
        '''
            moves the snake in the direction it's facing
        '''
        
        if self.direction == self.directions.up:
            self.y -= 1
        elif self.direction == self.directions.down:
            self.y += 1
        elif self.direction == self.directions.left:
            self.x -= 1
        elif self.direction == self.directions.right:
            self.x += 1
        else:
            raise Exception(f'invalid snake direction: {self.curr_direction}')

        self.positions.append((self.x, self.y))

    def turn(self, direction:Enum):
        if direction != self.direction and self.direction.value+direction.value != 0:
            self.direction = direction

    def eat(self, amount):
        self.length += amount
        self.positions = deque(list(self.positions), self.length)

class Food:

    class types(Enum):
        small = 1
        big = 3

    def __init__(self, env:'Environment'):
        self.env = env

    @property
    def position(self):
        return (self.x, self.y)

    def spawn(self, x:int, y:int, value:int=1):
        self.x = x
        self.y = y
        self.value = value
        self.type = self.types.big if value == 5 else self.types.small