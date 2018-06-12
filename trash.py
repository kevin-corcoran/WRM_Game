import resources
import physicalobject
from random import randint

class Trash(physicalobject.PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Trash, self).__init__(img=resources.trash['bcp'][0],*args, **kwargs)
        self.dy = randint(20,50)
        self.bins = ['paper','bcp','compost','landfill']
        self.random_trash()

    def update(self, dt):
        self.y -= self.dy * dt

    def random_trash(self):
        # bins = ['paper','bcp','compost','landfill']
        self.bin_type = self.bins[randint(0,len(self.bins) - 1)]
        # print(self.bin_type)
        self.bin = resources.trash[self.bin_type]
        self.image = self.bin[randint(0, len(self.bin) - 1)]
        # self.image = random_bin_trash
        # self.image = resources.trash[bins[randint(0,3)]][0]
        # self.image = resources.trash['compost'][0]
