import pyglet
from scenes import *
# import dungeon
import character
class Window(pyglet.window.Window):
    def __init__(self):
        super(Window, self).__init__(width=1024, height=668)
        self.states = [MainMenuScene(), HelpScene(), GameScene()] #, GameOver()]#, IntroScene(), Level1()]  # and so on...
        self.current_state = 0  # later you change it to get the scene you want
        self.set_visible()

    def on_draw(self):
        self.clear()
        self.states[self.current_state].batch.draw()
        # self.char.batch.draw()

    def on_key_press(self, symbol, modifiers):
        state = self.states[self.current_state]
        if hasattr(self.states[self.current_state],"on_key_press"):
            # self.states[self.current_state].on_key_press(symbol, modifiers)
            state.on_key_press(symbol, modifiers) # prints "pause game"
            if state.text == "GameScene":
                if symbol == key.P:
                    new_state = 0
                    new_state = new_state % len(self.states)
                    self.current_state = new_state

        # if symbol == key.R:
        #     self.current_state = 3 # game over

    def on_mouse_press(self, *args):
        state = self.states[self.current_state]
        if hasattr(self.states[self.current_state],"on_mouse_press"):
            state.on_mouse_press(*args)
            if state.text == "Main Menu":
                if state.start_button(*args):
                    new_state = 2
                    new_state = new_state % len(self.states)
                    self.current_state = new_state
                elif state.help_button(*args):
                    new_state = 1
                    self.current_state = new_state
            elif state.text == "Help Scene":
                if state.menu_botton(*args):
                    new_state = 0
                    self.current_state = new_state



        # if symbol == key.W:
        #     new_state = self.current_state + 1
        #     new_state = new_state % len(self.states)
        #     self.current_state = new_state

        # if you want each scene to handle input, you could use pyglet's push_handlers(), or even something like:
        #     self.states[self.current_state].on_key_press(symbol, modifiers)
        # giving them access to the window instance might be needed.
