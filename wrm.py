import pyglet
from character import Character
from physicalobject import PhysicalObject
import window
import resources
import bins
import trash
from random import randint

window = window.Window()
main_batch = window.states[1].batch # GameScene

# bins = Character(x=window.width//2,y=80, batch=main_batch)
bins = bins.Bin(x=window.width//2,y=80, batch=main_batch)

# testing - should be in a trash.py? with a trash class randomly dropping trash?
# bottle = PhysicalObject(img=resources.plastic_bag,x=window.width//2, y=window.height, batch=main_batch)
# bottle.velocity_y = -30

trash_obj = trash.Trash(x=window.width//2, y=window.height, batch=main_batch)
# Set up top labels
score_label = pyglet.text.Label(text="Score: 0", x=10, y=window.height - 20, batch=main_batch)
level_label = pyglet.text.Label(text="WRM: It's a Game!",
                                x=window.width - 100, y=window.height - 20, anchor_x='center', batch=main_batch)
trash_objects = [trash_obj]
# Set up the game over label offscreen
game_over_label = pyglet.text.Label(text="GAME OVER",
                                    x=400, y=-300, anchor_x='center',
                                    batch=main_batch, font_size=48)
game_objects = [bins] + trash_objects

score = 0

def update(dt):
    global score
    for obj in game_objects:
        obj.update(dt)

    """ TODO: change collisions to account for trash.bin [type]
            and characters collides_with function to coincide. """
    # To avoid handling collisions twice, we employ nested loops of ranges.
    # This method also avoids the problem of colliding an object with itself.
    for i in range(len(game_objects)):
        for j in range(i + 1, len(game_objects)):

            obj_1 = game_objects[i]
            obj_2 = game_objects[j]

            # Make sure the objects haven't already been killed
            # if not obj_1.dead and not obj_2.dead:
            if obj_1.collides_with(obj_2):
                obj_1.handle_collision_with(obj_2)
                obj_2.handle_collision_with(obj_1)

    for handler in bins.event_handlers:
        window.push_handlers(handler)

    # Get rid of dead objects
    for to_remove in [obj for obj in game_objects if obj.dead]:
        if to_remove == bins:
            print('...')
        # If the dying object spawned any new objects, add those to the
        # game_objects list later
        # to_add.extend(to_remove.new_objects)

        # Remove the object from any batches it is a member of
        to_remove.delete()
        print(str(to_remove))

        # Remove the object from our list
        game_objects.remove(to_remove)

        # Bump the score if the object to remove is an asteroid
        # if isinstance(to_remove, asteroid.Asteroid):
        score += 1
        score_label.text = "Score: " + str(score)
    # game_objects.append(trash.Trash(x=window.width//2, y=window.height, batch=main_batch))
    # Add new objects to the list
    # game_objects.extend(to_add)
def add_trash(dt):
    global game_objects
    x_pos = randint(30,window.width-30)
    game_objects.append(trash.Trash(x=x_pos, y=window.height, batch=main_batch))
    # return game_objects

@window.event
def on_draw():
    window.clear()
    # char.draw()
    # main_batch.draw()
pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.clock.schedule_interval(add_trash,5)
pyglet.app.run()
