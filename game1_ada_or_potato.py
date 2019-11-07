import arcade
import random


# Define constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Ada or Potato"
GAME_SPEED = 1/60
TIMER_MAXIMUM = 100

#Preload images
IMAGE_ADA=arcade.load_texture("images/ada.png")
IMAGE_POTATO=arcade.load_texture("images/potato.png")

class Potato(arcade.Sprite):
    phase: str
    timer: int

    def __init__(self):
        super().__init__()
        self.phase = 'waiting'
        self.timer = 0
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 2
        self.texture=IMAGE_POTATO

    def update_timer(self):
        if self.timer < TIMER_MAXIMUM:
            self.timer += 1
        else:
            self.timer = 0


    def update_angle(self):
        self.angle = 0

    def update(self):
        self.update_timer()
        self.update_angle()


class Ada(arcade.Sprite):
    phase: str
    timer: int

    def __init__(self):
        super().__init__()
        self.phase = 'waiting'
        self.timer = 0
        self.center_x = WINDOW_WIDTH/2
        self.center_y = WINDOW_HEIGHT/2
        self.texture=IMAGE_ADA

    def update_timer(self):
        if self.timer < TIMER_MAXIMUM:
            self.timer += 1
        else:
            self.timer = 0

    def update_angle(self):
        self.angle = 0

    def update(self):
        self.update_timer()
        self.update_angle()


class AdaOrPotato(arcade.Window):
    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.logo_list = None

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)
        self.logo_list = arcade.SpriteList()
        self.logo_list.append(Ada())
        self.logo_list.append(Potato())

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        random.choice(self.logo_list).draw()

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        self.logo_list.update()
        if self.timer==0:
            on_draw()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        points=0
        if self.logo_list=="Ada":
            points+=1
        else:
            points-=1
        print(points)


def main():
    window = AdaOrPotato()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
