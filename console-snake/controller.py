import time
from pynput import keyboard
from snake.environment import Environment

class PlayerController:

    def __init__(self, env:Environment):
        self.env = env
        self.env.bind_controller(self)
        self.input_listener = keyboard.Listener(on_press=self._on_press)
        self.input_listener.start()
        
        self.target_direction = None

    def _on_press(self, key):
        new_direction = None
        try:
            if key.char == 'w':
                new_direction = self.env.snake.direction.up
            elif key.char == 's':
                new_direction = self.env.snake.direction.down
            elif key.char == 'a':
                new_direction = self.env.snake.direction.left
            elif key.char == 'd':
                new_direction = self.env.snake.direction.right
            elif key.char == 'q':
                self.env.snake.is_alive = False
        except AttributeError:
            if key == keyboard.Key.up:
                new_direction = self.env.snake.direction.up
            elif key == keyboard.Key.down:
                new_direction = self.env.snake.direction.down
            elif key == keyboard.Key.left:
                new_direction = self.env.snake.direction.left
            elif key == keyboard.Key.right:
                new_direction = self.env.snake.direction.right
            elif key == keyboard.Key.esc:
                self.env.snake.is_alive = False
        except Exception as e:
            raise e
        finally:
            self.target_direction = new_direction