import resources
import physicalobject
from random import randint
from pyglet.window import key

class Trash(physicalobject.PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Trash, self).__init__(img=resources.trash['bcp'][0][1],*args, **kwargs)
        self.dy = randint(20,30)
        self.bins = ['paper','bcp','compost','landfill']
        self.random_trash()
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]


    def update(self, dt):
        self.y -= self.dy * dt
        # self.check_bounds()

    def random_trash(self):
        # bins = ['paper','bcp','compost','landfill']
        self.bin_type = self.bins[randint(0,len(self.bins) - 1)]
        print(self.bin_type)
        self.bin = resources.trash[self.bin_type]
        rand_int = randint(0, len(self.bin) - 1)
        self.image = self.bin[rand_int][1]
        self.name = self.bin[rand_int][0]
        self.name = self.name[:-4] # remove .png suffix
        self.name = self.name.replace('_', ' ')

    def collides_with(self, other_object):
        # so trash only falls into top of bin (with some padding)
        return super(Trash, self).collides_with(other_object) and \
            not (self.y + self.height*.9< other_object.y + other_object.height/2)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.dy = 350
            # print(self.dy)
        # print('name', self.name)
        # self.name = str(self.image)
        # self.image = random_bin_trash
        # self.image = resources.trash[bins[randint(0,3)]][0]
        # self.image = resources.trash['compost'][0]
