import arcade


# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLACK
GAME_TITLE = "Ada or Potato"
GAME_SPEED = 1/60
TIMER_MAXIMUM = 100

#Preload images
IMAGE_ADA=arcade.load_texture("images/ada.png", scale=.75)
IMAGE_POTATO=arcade.load_texture("images/potato.png", scale=.2)


class AlternatingImages(arcade.Sprite):
    phase: str
    timer: int

    def __init__(self):
        super().__init__()
        self.phase = 'ada'
        self.timer = 0
        self.center_x = WINDOW_WIDTH / 2
        self.center_y = WINDOW_HEIGHT / 2
        self.texture = IMAGE_ADA

    def update_timer(self):
        if self.timer < TIMER_MAXIMUM:
            self.timer += 1
        else:
            self.timer = 0
            self.switch_image()

    def update(self):
        self.update_timer()

    def switch_image(self):
        if self.texture==IMAGE_ADA:
            self.texture=IMAGE_POTATO
            self.phase='potato'
        else:
            self.texture=IMAGE_ADA
            self.phase='ada'

    def current_value(self):
        if self.texture=="IMAGE_ADA":
            return 1
        else:
            return -1


class AdaOrPotato(arcade.Window):
    sprite_list: []
    points: int

    def __init__(self):
        """ Initialize variables """
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.sprite_list = None
        self.points=None

    def setup(self):
        """ Setup the game (or reset the game) """
        self.points=0 #still initialize here so you can reset without calling constructor again
        arcade.set_background_color(BACKGROUND_COLOR)
        self.sprite_list = arcade.SpriteList()
        self.sprite_list.append(AlternatingImages())

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.sprite_list.draw()
        arcade.draw_text(str(self.points), 10, 50, arcade.color.WHITE, 20)

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""
        self.sprite_list.update()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):

        if self.sprite_list[0].phase == "ada":
            self.points += 1
        else:
            self.points -= 1

        for sprite in self.sprite_list:
            if sprite.collides_with_point([x,y]):
                self.points+=sprite.get_current_value()

def main():
    window = AdaOrPotato()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
