import pyglet
from pyglet.window import key
# from character import Character

class SceneTemplate(object):
    """a template with common things used by every scene"""
    def __init__(self, text, width=1024, height=768):
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
