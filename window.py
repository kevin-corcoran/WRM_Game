import pyglet
from scenes import *
# import dungeon
import character
class Window(pyglet.window.Window):
    def __init__(self):
        super(Window, self).__init__(width=1024, height=668)
        self.states = [MainMenuScene(), GameScene()]#, IntroScene(), Level1()]  # and so on...
        self.current_state = 0  # later you change it to get the scene you want
        self.set_visible()

    def on_draw(self):
        self.clear()
        self.states[self.current_state].batch.draw()
        # self.char.batch.draw()

    def on_key_press(self, symbol, modifiers):
        if hasattr(self.states[self.current_state],"on_key_press"):
            self.states[self.current_state].on_key_press(symbol, modifiers)

    def on_mouse_press(self, *args):
        state = self.states[self.current_state]
        if hasattr(self.states[self.current_state],"on_mouse_press"):
            state.on_mouse_press(*args)
            if state.text == "Main Menu":
                if state.start_button(*args):
                    new_state = self.current_state + 1
                    new_state = new_state % len(self.states)
                    self.current_state = new_state
                


        # if symbol == key.W:
        #     new_state = self.current_state + 1
        #     new_state = new_state % len(self.states)
        #     self.current_state = new_state

        # if you want each scene to handle input, you could use pyglet's push_handlers(), or even something like:
        #     self.states[self.current_state].on_key_press(symbol, modifiers)
        # giving them access to the window instance might be needed.
