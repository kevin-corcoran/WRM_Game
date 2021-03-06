import pyglet
import util
# from . import util

class PhysicalObject(pyglet.sprite.Sprite):
    """A sprite with physical properties such as velocity"""

    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)

        # Velocity
        self.velocity_x, self.velocity_y = 0.0, 0.0

        # Flags to toggle collision with bullets
        self.reacts_to_bullets = True
        self.is_bullet = False

        # Flag to remove this object from the game_object list
        self.dead = False

        # List of new objects to go in the game_objects list
        self.new_objects = []

        # Tell the game handler about any event handlers
        # Only applies to things with keyboard/mouse input
        self.event_handlers = []

        self.wrapped = 0

    def update(self, dt):
        """This method should be called every frame."""

        # Update position according to velocity and time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        # Wrap around the screen if necessary
        # self.check_bounds()

    def check_bounds(self):
        """Use the classic Asteroids screen wrapping behavior"""
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = 1024 + self.image.width / 2
        max_y = 668 + self.image.height / 2
        if self.x < min_x:
            self.x = max_x
            self.wrapped = 1
        if self.y < min_y:
            self.y = max_y
            self.wrapped = 1
        if self.x > max_x:
            self.x = min_x
            self.wrapped = 1
        if self.y > max_y:
            self.y = min_y
            self.wrapped = 1

    def collides_with(self, other_object):
        """Determine if this object collides with another"""

        # Ignore bullet collisions if we're supposed to
        # if not self.reacts_to_bullets and other_object.is_bullet:
        #     return False
        # if self.is_bullet and not other_object.reacts_to_bullets:
        #     return False

        # Calculate distance between object centers that would be a collision,
        # assuming square resources
        collision_distance = self.image.height * 0.5  \
                             + other_object.image.height * 0.5

        # Get distance using position tuples
        actual_distance = util.distance(self.position, other_object.position)

        return (actual_distance <= collision_distance)

    def handle_collision_with(self, other_object):
        if other_object.__class__ is not self.__class__:
            self.dead = True
        # print('bang!')
