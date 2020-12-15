"""
Space Doggo Game:
This project uses the code from
https://arcade.academy/examples/starting_template.html
as a, well, starting template, and from there features have been added 1 by 1.
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Doggo"
SPRITE_SCALING_PLAYER = 0.5


class MyGame(arcade.Window):
    """
    Main application class.
    """

    # Here we basically declare what is going to be in the game
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        # If you have sprite lists, you should create them here,
        # and set them to None

        # https://arcade.academy/examples/sprite_collect_coins.html
        # declare our player_list and set it to None
        self.player_list = None

        self.player_sprite = None

    # Here we basically decide what the game will be like when it starts
    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here

        # Sprite lists
        # https://arcade.academy/examples/sprite_collect_coins.html
        # Here we make the player_list list able to handle Sprite resources in a list
        # https://arcade.academy/_modules/arcade/sprite_list.html
        self.player_list = arcade.SpriteList()

        # https://arcade.academy/examples/sprite_collect_coins.html
        # https://arcade.academy/resources.html#resources-images-animated-characters-female-adventurer
        # I used the jpg of Jake the Dog from this web page:
        # https://pnghut.com/png/E9C6k1euM1/jake-the-dog-finn-human-pixel-art-puppy-adventure-time-transparent-png
        # it was created by a user named Ardenvin and posted on pnghut. Thank you Ardenvin.
        self.player_sprite = arcade.Sprite("jakeTheDog.png",
                                           SPRITE_SCALING_PLAYER)

        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50

        # actually add player_sprite to player_list, since it
        # probably won't show up without doing this
        self.player_list.append(self.player_sprite)


    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # https://arcade.academy/examples/sprite_collect_coins.html
        # right, as I said above, we're drawing the player_list, not
        # the player_sprite, hence player_sprite needs to be added to
        # player_list
        self.player_list.draw()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass




def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()