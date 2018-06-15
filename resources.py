import pyglet
import os

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

def resize(image, factor):
    image.width = image.width*factor
    image.height = image.height*factor

# Tell pyglet where to find the resources
pyglet.resource.path = ['assets/']
pyglet.resource.reindex()

button = pyglet.resource.image("img.png")
center_image(button)

help_button = pyglet.resource.image("help.png")
center_image(help_button)

main_menu_button = pyglet.resource.image("main.png")
center_image(main_menu_button)

restart_button = pyglet.resource.image("res.png")
center_image(restart_button)

# Load the main resources and get them to draw centered
bins = pyglet.resource.image("bins.png")
resize(bins,1/2)
center_image(bins)

paper_bin = pyglet.resource.image("paper_bin.png")
resize(paper_bin,1/2)
center_image(paper_bin)

bcp_bin = pyglet.resource.image("bcp_bin.png")
resize(bcp_bin,1/2)
center_image(bcp_bin)

compost_bin = pyglet.resource.image("compost_bin.png")
resize(compost_bin,1/2)
center_image(compost_bin)

landfill_bin = pyglet.resource.image("landfill_bin.png")
resize(landfill_bin,1/2)
center_image(landfill_bin)

life = pyglet.resource.image('earth.png')
resize(life,1/4)
# center_image(lives)

trash = {
    'paper' : [],
    'bcp' : [],
    'compost' : [],
    'landfill' : []
}
""" paper/cardboard """
# cardboard_box = pyglet.resource.image("paper/cardboard_box.png")
# resize(cardboard_box,1/9)
# center_image(cardboard_box)
paper_items = [f for f in os.listdir(os.getcwd() + '/assets/paper/') if f.endswith('.png')]
for item in paper_items:
    image = pyglet.resource.image('paper/' + item)
    trash['paper'].append((item, image))
    center_image(image)

""" bcp """
# plastic_bottle = pyglet.resource.image("bcp/plastic_bottle.png")
# resize(plastic_bottle, 1/9)
# center_image(plastic_bottle)
bcp_items = [f for f in os.listdir(os.getcwd() + '/assets/bcp/') if f.endswith('.png')]
print(bcp_items)
for item in bcp_items:
    image = pyglet.resource.image('bcp/' + item)
    trash['bcp'].append((item, image))
    center_image(image)

""" compost """
# pizza_box = pyglet.resource.image("compost/pizza_box.png")
# resize(pizza_box,1/9)
# center_image(pizza_box)
compost_items = [f for f in os.listdir(os.getcwd() + '/assets/compost/') if f.endswith('.png')]
print(compost_items)
for item in compost_items:
    image = pyglet.resource.image('compost/' + item)
    trash['compost'].append((item, image))
    center_image(image)

""" landfill """
# plastic_bag = pyglet.resource.image("landfill/plastic_bag.png")
# resize(plastic_bag, 1/5)
# center_image(plastic_bag)
landfill_items = [f for f in os.listdir(os.getcwd() + '/assets/landfill/') if f.endswith('.png')]
print(landfill_items)
for item in landfill_items:
    image = pyglet.resource.image('landfill/' + item)
    trash['landfill'].append((item, image))
    center_image(image)

# trash = {
#     'paper' : [cardboard_box],
#     'bcp' : [plastic_bottle],
#     'compost' : [pizza_box],
#     'landfill' : [plastic_bag]
# }
