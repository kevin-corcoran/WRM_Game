import pyglet
from pyglet.window import key
import resources
import bins
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
        self.button2 = pyglet.sprite.Sprite(img=resources.help_button,x=self.width/2, y=self.height/2-self.button.height-3,batch=self.batch)
        # self.button_down = pyglet.sprite.Sprite(img=resources.button_down,x=self.width/2, y=self.height/2,batch=self.batch)

    def on_mouse_press(self, x, y, button, modifiers):
        # print(x, y)
        pass
        # return True

    def start_button(self, x, y, button, modifiers):
        if x < self.button.x + self.button.width/2 and x > self.button.x - self.button.width/2 \
                and y < self.button.y + self.button.height/2 and y > self.button.y - self.button.height/2:
            return True

    def help_button(self, x, y, button, modifiers):
        if x < self.button.x + self.button2.width/2 and x > self.button2.x - self.button2.width/2 \
                and y < self.button2.y + self.button2.height/2 and y > self.button2.y - self.button2.height/2:
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
        # self.bins = bins.Bin()
        self.paper_bin = pyglet.sprite.Sprite(x=30,y=self.height-80,img=resources.paper_bin,batch=self.batch)
        self.paper_bin.scale = 1/2
        self.bcp_bin = pyglet.sprite.Sprite(x=60,y=self.height-80,img=resources.bcp_bin,batch=self.batch)
        self.bcp_bin.scale = 1/3
        self.compost_bin = pyglet.sprite.Sprite(x=90,y=self.height-80,img=resources.compost_bin,batch=self.batch)
        self.compost_bin.scale = 1/3
        self.landfill_bin = pyglet.sprite.Sprite(x=120,y=self.height-80,img=resources.landfill_bin,batch=self.batch)
        self.landfill_bin.scale = 1/3

        self.bins = [self.paper_bin, self.bcp_bin, self.compost_bin, self.landfill_bin]
        self.current_bin = 0

    def on_key_press(self, symbol, modifiers):
        if symbol == key.P:
            print('pause game')
        if symbol == key.D:
            new_bin = self.current_bin + 1
            new_bin = new_bin % len(self.bins)
            self.bins[self.current_bin].scale = 1/3
            self.bins[new_bin].scale = 1/2
            self.current_bin = new_bin
        if symbol == key.A:
            new_bin = self.current_bin - 1
            new_bin = new_bin % len(self.bins)
            self.bins[self.current_bin].scale = 1/3
            self.bins[new_bin].scale = 1/2
            self.current_bin = new_bin
            # self.bcp_bin.scale = 1/2
            # pass

class HelpScene(SceneTemplate):
    def __init__(self,text='Help Scene'):
        super(HelpScene, self).__init__(text)
        self.batch = pyglet.graphics.Batch()
        self.text = text
        self.label = pyglet.text.Label(
            text='Controls',
            font_name='Arial', font_size=32,
            # color=(200, 255, 255, 255),
            x=self.width/2, y=self.height-60,
            batch=self.batch,
            anchor_x='center')
        self.controls_label = pyglet.text.Label(
            text = 'BCP Guidelines',
            font_size = 20,
            x = self.label.x - self.width/3,
            y = self.label.y - 70,
            batch=self.batch,
            anchor_x='center'
        )
        self.bcp_guide = pyglet.text.HTMLLabel(
            '<font face="Times New Roman" size="4">Hello, <i>world</i></font>',
            x = 500,
            y = 200,
            batch = self.batch
        )
        # self.document = pyglet.text.decode_html('Hello, <b>world</b>',x=500,y=100)

        # (...)
        self.button = pyglet.sprite.Sprite(img=resources.main_menu_button,x=self.width/2, y=self.height/2,batch=self.batch)
        # self.button_down = pyglet.sprite.Sprite(img=resources.button_down,x=self.width/2, y=self.height/2,batch=self.batch)

    def on_mouse_press(self, x, y, button, modifiers):
        # print(x, y)
        pass
        # return True

    def menu_botton(self, x, y, button, modifiers):
        if x < self.button.x + self.button.width/2 and x > self.button.x - self.button.width/2 \
                and y < self.button.y + self.button.height/2 and y > self.button.y - self.button.height/2:
            return True
        else:
            return False

    def on_key_press(self, symbol, modifiers):
        pass
#
# class GameOver(GameScene):
#     def __init__(self,text='Game Over'):
#         super(GameOver, self).__init__(text)
#         game_over_label = pyglet.text.Label(text="GAME OVER",
#                                             x=self.width/2, y=self.height/2, anchor_x='center',
#                                             batch=self.batch, font_size=48)
# class IntroScene(SceneTemplate):
#     def __init__(self):
#         super(IntroScene, self).__init__(text='Introduction')
#         # (...)
#
# class Level1(SceneTemplate):
#     def __init__(self):
#         super(Level1, self).__init__(text='Level 1')
#         # (...)
