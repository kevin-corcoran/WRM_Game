import pyglet
from character import Character
from physicalobject import PhysicalObject
import window
import resources

window = window.Window()
main_batch = window.states[1].batch # GameScene

bins = Character(x=window.width//2,y=80, batch=main_batch)

# testing - should be in a trash.py? with a trash class randomly dropping trash?
bottle = PhysicalObject(img=resources.bottle,x=window.width//2, y=window.height, batch=main_batch)
bottle.velocity_y = -20
# Set up top labels
score_label = pyglet.text.Label(text="Score: 0", x=10, y=window.height - 20, batch=main_batch)
level_label = pyglet.text.Label(text="WRM: It's a Game!",
                                x=window.width - 100, y=window.height - 20, anchor_x='center', batch=main_batch)

# Set up the game over label offscreen
game_over_label = pyglet.text.Label(text="GAME OVER",
                                    x=400, y=-300, anchor_x='center',
                                    batch=main_batch, font_size=48)
game_objects = [bins, bottle]


def update(dt):
    for obj in game_objects:
        obj.update(dt)

    # for wall in wall_sprites:
    #     if char.collides_with(wall):
    #         char.handle_collision_with(wall)

for handler in bins.event_handlers:
    window.push_handlers(handler)

@window.event
def on_draw():
    window.clear()
    # char.draw()
    # main_batch.draw()
pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
