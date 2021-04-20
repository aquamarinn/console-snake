from snake import Environment, GUI, PlayerController

if __name__ == '__main__':
    try:
        env = Environment()
        gui = GUI(env)
        controller = PlayerController(env)

        running, _ = env.reset()
        while running:
            running, snake_pos = env.step()
            print('running', running)
    finally:
        try:
            gui._terminate_curses()
        except NameError:
            pass
        except Exception as e:
            raise e