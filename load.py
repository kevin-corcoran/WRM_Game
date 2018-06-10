import pyglet
from random import randint
from . import trash, resources, util

from_bcp = ['trash_bottle.png']
from_landfill = ['plastic_bag.png']
# Tell pyglet where to find the resources
pyglet.resource.path = ['assets/']
pyglet.resource.reindex()
def trash(window_width, window_height, batch=None):
    trash_lst = []
    files = ['bcp','compost','landfill','paper']
    rand_file = randint[0,3]

    trash_image = files[rand_file] + '/' + from_landfill

    trash_sprite = pyglet.resource.image(trash_image)




#
#
# def player_lives(num_icons, batch=None):
#     """Generate sprites for player life icons"""
#     player_lives = []
#     for i in range(num_icons):
#         new_sprite = pyglet.sprite.Sprite(img=resources.player_image,
#                                           x=785 - i * 30, y=585,
#                                           batch=batch)
#         new_sprite.scale = 0.5
#         player_lives.append(new_sprite)
#     return player_lives
#
#
# def asteroids(num_asteroids, player_position, batch=None):
#     """Generate asteroid objects with random positions and velocities, not close to the player"""
#     asteroids = []
#     for i in range(num_asteroids):
#         asteroid_x, asteroid_y = player_position
#         while util.distance((asteroid_x, asteroid_y), player_position) < 100:
#             asteroid_x = random.randint(0, 800)
#             asteroid_y = random.randint(0, 600)
#         new_asteroid = asteroid.Asteroid(x=asteroid_x, y=asteroid_y, batch=batch)
#         new_asteroid.rotation = random.randint(0, 360)
#         new_asteroid.velocity_x, new_asteroid.velocity_y = random.random() * 40, random.random() * 40
#         asteroids.append(new_asteroid)
#     return asteroids
