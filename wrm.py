import pyglet
from character import Character
from physicalobject import PhysicalObject
import window
import resources
import bins
import trash
from random import randint

window = window.Window()
main_batch = window.states[2].batch # GameScene

# main game objects
bins = bins.Bin(x=window.width//2,y=80, batch=main_batch)
trash_obj = trash.Trash(x=window.width//2, y=window.height, batch=main_batch)

# Set up top labels
score_label = pyglet.text.Label(text="Score: 0", x=10, y=window.height - 20, batch=main_batch)
level_label = pyglet.text.Label(text="WRM: It's a Game!",
                                x=window.width - 100, y=window.height - 20, anchor_x='center', batch=main_batch)
trash_objects = [trash_obj]
trash_label = pyglet.text.Label(text=trash_obj.name,
                    x=100, y=window.height - 20,
                    batch=main_batch, font_size=8)
# Set up the game over label offscreen
game_over_label = pyglet.text.Label(text="GAME OVER",
                                    x=window.width/2, y=-300, anchor_x='center',
                                    batch=main_batch, font_size=48)
restart_button = pyglet.sprite.Sprite(img=resources.restart_button,x=window.width/2,y=-300,batch=main_batch)
game_objects = [bins] + trash_objects

count = 0
score = 0
lives = 4
life = resources.life
# earth sprite lives counter top right corner
lives_sprites = [pyglet.sprite.Sprite(img=life, \
                        x=window.width - life.width - 35*i - 30,\
                        y=window.height - life.height - 30, batch=main_batch) \
                        for i in range(lives)]

event_stack_size = 0

def game_over():
    global event_stack_size, game_over_label
    # Clear the event stack of any remaining handlers from other levels
    while event_stack_size > 0:
        window.pop_handlers()
        event_stack_size -= 1

    # add event to listen to reset button press
    window.push_handlers(on_mouse_press)
    game_over_label.y = window.height/2
    restart_button.y = game_over_label.y -100

def reset_level():
    # pass
    global score, count, lives, lives_sprites, game_objects
    score = 0
    score_label.text = "Score: " + str(score)
    count = 0
    lives = 4
    for obj in game_objects:
        if isinstance(obj, trash.Trash):
            obj.delete()
    game_objects = [bins] + [trash.Trash(x=window.width//2, y=window.height, batch=main_batch)]
    game_over_label.y = -300
    restart_button.y = -300
    lives_sprites = [pyglet.sprite.Sprite(img=life, \
                            x=window.width - life.width - 35*i - 30,\
                            y=window.height - life.height - 30, batch=main_batch) \
                            for i in range(lives)]
    # remove event to listen to restart button
    window.pop_handlers()

def reset_button(x, y, button, modifiers):
    if x < restart_button.x + restart_button.width/2 and x > restart_button.x - restart_button.width/2 \
            and y < restart_button.y + restart_button.height/2 and y > restart_button.y - restart_button.height/2:
        return True
    else:
        return False


def check_lowest(obj):
    if isinstance(obj, trash.Trash):
        return obj.y
    else: # obj is bin
        return window.height+50
#
def update(dt):
    global lives, lives_sprites,event_stack_size, count
    if window.current_state == 2: # Game Scene
        global score
        for obj in game_objects:
            obj.update(dt)
            # if isinstance(obj, trash.Trash):
            #     y_pos.append(obj.y)
            if obj.y < 10:
                obj.dead = True
                score -= 1
                # obj.collides_with = lambda x: False
                # obj.check_bounds = lambda : None
                if obj.collides_with(obj) != False: # else we already lost a life
                    lives -= 1
                    if lives_sprites != []:
                        lives_sprites[-1].delete()
                        lives_sprites = lives_sprites[:-1]
                        
        # lowest_trash = min(game_objects, key=lambda obj: obj.y if isinstance(obj, trash.Trash))
        lowest_trash = min(game_objects, key=check_lowest)
        for handler in lowest_trash.event_handlers:
            window.push_handlers(handler)
            event_stack_size += 1

            # for handler in obj.event_handlers:
            #     window.push_handlers(handler)
            #     event_stack_size += 1
            # score -= obj.wrapped
            # score_label.text = "Score: " + str(score)
            # print(obj.y)
            """ Why wont score update?
                Trying to reduce score if trash touches grounds
             """
            # if obj.y < 10:
            #     obj.dead = True
            #     score -= 1
            #     # obj.collides_with = lambda x: False
            #     # obj.check_bounds = lambda : None
            #     if obj.collides_with(obj) != False: # else we already lost a life
            #         lives -= 1
            #         if lives_sprites != []:
            #             lives_sprites[-1].delete()
            #             lives_sprites = lives_sprites[:-1]



        # handle collisions with trash
        for obj in game_objects:
            if obj.collides_with(bins):
                if bins.bin_type == obj.bin_type:
                    obj.handle_collision_with(bins) # obj.dead = True
                else:
                    # a sort of flag that lets us know it was the wrong bin
                    obj.collides_with = lambda x: False
                    # obj.check_bounds = lambda : None
                    # so lives aren't continually lost every frame the wrong bin interacts with trash
                    lives -= 1
                    if lives_sprites != []:
                        lives_sprites[-1].delete()
                        lives_sprites = lives_sprites[:-1]
        if lives == 0:
            game_over()
            # reset_level()

        for handler in bins.event_handlers:
            window.push_handlers(handler)
            event_stack_size += 1

        # Get rid of dead objects
        for to_remove in [obj for obj in game_objects if obj.dead]:
            # Remove the object from any batches it is a member of
            to_remove.delete()

            # Remove the object from our list
            game_objects.remove(to_remove)

            # Bump the score if the game isn't over
            if lives > 0:
                score += 1
                score_label.text = "Score: " + str(score)

        # adjust speed trash falls after so much trash is created
        if count == 5:
            pyglet.clock.unschedule(add_trash)
            pyglet.clock.schedule_interval(add_trash,6)
            count += 1
        elif count == 10:
            pyglet.clock.unschedule(add_trash)
            pyglet.clock.schedule_interval(add_trash, 5)
            count += 1
        elif count == 15:
            pyglet.clock.unschedule(add_trash)
            pyglet.clock.schedule_interval(add_trash, 4)
            count += 1
        elif count == 20:
            pyglet.clock.unschedule(add_trash)
            pyglet.clock.schedule_interval(add_trash, 3)
            count += 1
        elif count == 30:
            pyglet.clock.unschedule(add_trash)
            pyglet.clock.schedule_interval(add_trash, 2)
            count += 1
        elif count == 50:
            pyglet.clock.unschedule(add_trash)
            pyglet.clock.schedule_interval(add_trash, 1)
            count += 1

def add_trash(dt):
    global game_objects
    global trash_label
    global count

    x_pos = randint(300,window.width-300)
    if window.current_state == 2: # Game Scene
        new_trash = trash.Trash(x=x_pos, y=window.height, batch=main_batch)
        # increase speed trash falls based on score
        if score > 30:
            new_trash.dy = randint(40,80)
        elif score > 20:
            new_trash.dy = randint(40,70)
        elif score > 15:
            new_trash.dy = randint(30,60)
        elif score > 10:
            new_trash.dy = randint(30, 60)
        elif score > 5:
            new_trash.dy = randint(30,60)

        # add trash to game objects
        game_objects.append(new_trash)

        trash_label.text = new_trash.name

        # change rate new trash appears based on how many new trash have been added
        count += 1

@window.event
def on_draw():
    window.clear()

# @window.event
def on_mouse_press(x, y, button, modifiers):
    if reset_button(x, y, button, modifiers):
        reset_level()

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.clock.schedule_interval(add_trash,7)
pyglet.app.run()
