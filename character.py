import pyglet
from pyglet.window import key
import physicalobject
import resources
import math

class Character(physicalobject.PhysicalObject):
    """Physical object that responds to user input"""

    def __init__(self, *args, **kwargs):
        super(Character, self).__init__(img=resources.bins, *args, **kwargs)

        # Create a child sprite to show when the ship is thrusting
        # self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_image, *args, **kwargs)
        # self.engine_sprite.visible = False
        self.dx = 0.0
        self.dy = 0.0

        # Player should not collide with own bullets
        self.reacts_to_bullets = False

        # Tell the game handler about any event handlers
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]

    def update(self, dt):
        # Do all the normal physics stuff
        super(Character, self).update(dt)

        self.y += self.dy * dt
        self.x += self.dx * dt

    def on_key_press(self,symbol,modifiers):
        if symbol == key.UP:
            self.dy = 100.0
        if symbol == key.RIGHT:
            self.dx = 100.0
        if symbol == key.DOWN:
            self.dy = -100.0
        if symbol == key.LEFT:
            self.dx = -100.0

    def on_key_release(self,symbol,modifiers):
        if symbol == key.UP or symbol == key.DOWN:
            self.dy = 0
        if symbol == key.RIGHT or symbol == key.LEFT:
            self.dx = 0

    def fire(self):
        # Note: pyglet's rotation attributes are in "negative degrees"
        angle_radians = -math.radians(self.rotation)

        # Create a new bullet just in front of the player
        ship_radius = self.image.width / 2
        bullet_x = self.x + math.cos(angle_radians) * ship_radius
        bullet_y = self.y + math.sin(angle_radians) * ship_radius
        new_bullet = bullet.Bullet(bullet_x, bullet_y, batch=self.batch)

        # Give it some speed
        bullet_vx = self.velocity_x + math.cos(angle_radians) * self.bullet_speed
        bullet_vy = self.velocity_y + math.sin(angle_radians) * self.bullet_speed
        new_bullet.velocity_x, new_bullet.velocity_y = bullet_vx, bullet_vy

        # Add it to the list of objects to be added to the game_objects list
        self.new_objects.append(new_bullet)

        # Play the bullet sound
        resources.bullet_sound.play()

    def delete(self):
        # We have a child sprite which must be deleted when this object
        # is deleted from batches, etc.
        # self.engine_sprite.delete()
        super(Character, self).delete()

    # def collides_with(self, other_object):
    #     """Determine if this object collides with another"""
    #
    #     # Calculate distance between object centers that would be a collision,
    #     # assuming square resources
    #     collision_distance = self.image.width * 0.5 * self.scale \
    #                          + other_object.image.width * 0.5 * other_object.scale
    #
    #     # Get distance using position tuples
    #     actual_distance = util.distance(self.position, other_object.position)
    #
    #     return (actual_distance <= collision_distance)

    def handle_collision_with(self, obj):
        pass
        # self.x += -self.dx/20
        # self.y += -self.dy/20
        # # if not (self.key_handler[key.UP] or self.key_handler[key.DOWN]):
        # self.dy=0
        # # if not (self.key_handler[key.LEFT] or self.key_handler[key.RIGHT]):
        # self.dx=0
