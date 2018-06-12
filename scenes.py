import pyglet
from pyglet.window import key
import resources
# from pyglet_gui.manager import Manager
# from pyglet_gui.buttons import Button
# from character import Character

class SceneTemplate(object):
    """a template with common things used by every scene"""
    def __init__(self, text, width=1024, height=668):
        self.batch = pyglet.graphics.Batch()
        self.text = text
        self.width = width
        self.height = height
        self.label = pyglet.text.Label(
            text=self.text,
            font_name='Arial', font_size=32,
            color=(200, 255, 255, 255), x=32, y=704,
            batch=self.batch)
        # self.label.anchor_x='center'
        # (...)
        # self.current_state = 0

class MainMenuScene(SceneTemplate):
    def __init__(self,text='Main Menu'):
        super(MainMenuScene, self).__init__(text)
        self.batch = pyglet.graphics.Batch()
        self.text = text
        self.label = pyglet.text.Label(
            text=self.text,
            font_name='Arial', font_size=32,
            color=(200, 255, 255, 255), x=self.width/2, y=self.height-60,
            batch=self.batch,
            anchor_x='center')
        # (...)
        self.button = pyglet.sprite.Sprite(img=resources.button,x=self.width/2, y=self.height/2,batch=self.batch)
        # self.button_down = pyglet.sprite.Sprite(img=resources.button_down,x=self.width/2, y=self.height/2,batch=self.batch)

    def on_mouse_press(self, x, y, button, modifiers):
        print(x, y)
        return True

    def start_button(self, x, y, button, modifiers):
        if x < self.button.x + self.button.width/2 and x > self.button.x - self.button.width/2 \
                and y < self.button.y + self.button.height/2 and y > self.button.y - self.button.height/2:
            return True
        # else:
        #     return False

    def on_key_press(self, symbol, modifiers):
        pass
        # print('key')

class GameScene(SceneTemplate):
    def __init__(self,text='GameScene'):
        super(GameScene, self).__init__(text)
        self.batch = pyglet.graphics.Batch()

# class IntroScene(SceneTemplate):
#     def __init__(self):
#         super(IntroScene, self).__init__(text='Introduction')
#         # (...)
#
# class Level1(SceneTemplate):
#     def __init__(self):
#         super(Level1, self).__init__(text='Level 1')
#         # (...)
