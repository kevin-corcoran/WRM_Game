import resources
import physicalobject

class Trash(physicalobject.PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Character, self).__init__(img=resources.bins, *args, **kwargs)
