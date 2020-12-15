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
MOVEMENT_SPEED = 2.0


# Here we add a new class, called Player, with heavy help from here:
# https://arcade.academy/examples/sprite_move_keyboard_better.html
class Player(arcade.Sprite):

    def update(self):

        # this code moves our Jake
        self.center_y += self.change_y
        self.center_x += self.change_x

        # this code keeps Jake trapped within the game screen
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT -1
        elif self.bottom < 0:
            self.bottom = 0


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

        # code block below basically is for tracking arrow keys being pressed
        # but it's only the variables, this part doesn't actually do anything
        # other than pacify the compiler since creating variables on the fly
        # in the code below, well, doesn't fly
        # code gotten from here:
        # https://arcade.academy/examples/sprite_move_keyboard_better.html
        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

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
        # code copied from here:
        # https://arcade.academy/examples/sprite_move_keyboard_better.html
        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED

        # Call update to move the sprite
        # If using a physics engine, call update player to rely on physics engine
        # for movement, and call physics engine here.
        # Jared Note: So, we created an update function in the player class, right?
        # it seems the line below iterates through all the members of the player_list
        # and calls each of their update functions
        self.player_list.update()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        """Called whenever a key is pressed. """
        # code copied from here:
        # https://arcade.academy/examples/sprite_move_keyboard_better.html

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        # code copied from here:
        # https://arcade.academy/examples/sprite_move_keyboard_better.html

        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False




def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()