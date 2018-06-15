from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import pyglet
import os

print(os.getcwd())

def create_image(text, name='img',W=12,H=12,background_color=(73, 109, 137, 200),fill_color=(0,0,0,0)):
    """ Convert text to image for use as sprite """
    # create box
    img = Image.new('RGBA', (W, H) ,color = background_color)
    d = ImageDraw.Draw(img)
    # fnt = ImageFont.truetype("Acme-Regular.ttf", 20)
    # add and center text
    w,h = d.textsize(text)
    # d.textsize = 50,60
    # d.text(((W-w)/2,(H-h)/2), text, fill = fill_color, font=fnt)
    d.text(((W-w)/2,(H-h)/2), text, fill = fill_color)
    path = 'assets/' + name + '.png'
    img.save(path, 'PNG')
    return path

create_image(text='Start',W=80,H=30)
create_image(text='Help',name='help',W=80,H=30)
create_image(text='Main Menu',name='main',W=80,H=30)
create_image(text='Restart',name='res',W=80,H=30)
