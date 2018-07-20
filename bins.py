# import pyglet
from pyglet.window import key
import physicalobject
import resources
import math

class Bin(physicalobject.PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Bin, self).__init__(img=resources.paper_bin, *args, **kwargs)

        # Create a child sprite to show when the ship is thrusting
        # self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_image, *args, **kwargs)
        # self.engine_sprite.visible = False
        self.dx = 0.0
        self.bin_type = 'paper'
        # Tell the game handler about any event handlers
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

        self.states = [resources.paper_bin, resources.bcp_bin, resources.compost_bin, resources.landfill_bin]
        self.current_state = 0  # later you change it to get the bin you want
        self.bins = {0: 'paper', 1: 'bcp', 2: 'compost', 3: 'landfill'}
        self.count = 0 # used in on_key_press to solve bug
        self.pressed_keys = []

    def update(self, dt):
        # Do all the normal physics stuff
        # super(Bin, self).update(dt)

        self.x += self.dx * dt

    def on_key_press(self, symbol, modifiers):
        # for some reason this is getting called multiple times.
        # count helps change state only once
        # if symbol == key.SPACE:
        #     print('space')
        # self.count += 1
        # if self.count == 1:
        if symbol == key.D and symbol not in self.pressed_keys:
            new_state = self.current_state + 1
            new_state = new_state % len(self.states)
            self.current_state = new_state
            self.image = self.states[self.current_state]
            self.bin_type = self.bins[self.current_state]
            print('bin_type: ', self.bin_type)
            self.pressed_keys.append(symbol)
            # self.count = 0
        if symbol == key.A and symbol not in self.pressed_keys:
            new_state = self.current_state - 1
            new_state = new_state % len(self.states)
            self.current_state = new_state
            self.image = self.states[self.current_state]
            self.bin_type = self.bins[self.current_state]
            self.pressed_keys.append(symbol)
                # self.count = 0

        if symbol == key.RIGHT:
            self.dx = 250.0
            if self.count == 1:
                self.count = 0
        if symbol == key.LEFT:
            self.dx = -250.0
            if self.count == 1:
                self.count = 0

    def on_key_release(self,symbol,modifiers):
        # self.count = 0
        if symbol == key.A and symbol in self.pressed_keys:
            self.pressed_keys.remove(symbol)
        if symbol == key.D and symbol in self.pressed_keys:
            self.pressed_keys.remove(symbol)
        if symbol == key.RIGHT or symbol == key.LEFT:
            self.dx = 0

    def delete(self):
        # We have a child sprite which must be deleted when this object
        # is deleted from batches, etc.
        # self.engine_sprite.delete()
        super(Bin, self).delete()

    def handle_collision_with(self, obj):
        pass
