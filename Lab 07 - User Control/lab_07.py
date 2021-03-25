""" Lab 7 - User Control """

import arcade
from math import pi, sin, cos

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

# funcion para dibujar un conjunto de lineas rodeadas a un circulo
def draw_sunlight(center_x, center_y, inner_radio, outer_radio, n_lines = 20):
    rotation = 0
    for i in range(n_lines):
        inner_x = center_x + inner_radio * cos(rotation)
        inner_y = center_y + inner_radio * sin(rotation)
        outer_x = center_x + outer_radio * cos(rotation)
        outer_y = center_y + outer_radio * sin(rotation)
        arcade.draw_line(inner_x, inner_y, outer_x, outer_y, arcade.color.ORANGE, 2)
        rotation += pi * 2 / n_lines

# funcion para dibujar una estrella de 5 puntas
def draw_star(center_x, center_y, inner_radio, outer_radio, color, rotation=0):
    point_list = []
    for i in range(5):
        point_list.append( (center_x + inner_radio * sin(rotation), center_y + inner_radio * cos(rotation)) )
        rotation += pi/5
        point_list.append( (center_x + outer_radio * sin(rotation), center_y + outer_radio * cos(rotation)) )
        rotation += pi/5
    arcade.draw_polygon_filled(point_list, color)

# funcion para dibujar una bandera
def draw_bandera(x, y): #500 335
    """ left_x, bottom_y """
    arcade.draw_ellipse_filled(x, y-285, x-440, y-305, arcade.color.LIGHT_GRAY)
    arcade.draw_ellipse_outline(x, y-285, x-440, y-305, arcade.color.BLACK, 2)
    arcade.draw_lrtb_rectangle_outline(x-5, x+5, y+165, y-280, arcade.color.BLACK, 3)
    arcade.draw_lrtb_rectangle_filled(x-4, x+4, y+164, y-285, arcade.color.LIGHT_GRAY)

    arcade.draw_lrtb_rectangle_filled(x, x+240, y+160, y, arcade.color.RED)
    arcade.draw_lrtb_rectangle_outline(x, x+240, y+160, y, arcade.color.BLACK, 2)
    draw_star(x+40, y+110, 25, 10, arcade.color.YELLOW)
    draw_star(x+75, y+135, 10, 4, arcade.color.YELLOW, pi/10)
    draw_star(x+95, y+120, 10, 4, arcade.color.YELLOW, -pi/10)
    draw_star(x+95, y+95, 10, 4, arcade.color.YELLOW)
    draw_star(x+75, y+80, 10, 4, arcade.color.YELLOW, pi/10)

class Star:
    def __init__(self, center_x, center_y, outer_radio, inner_radio, color, change_x = 0, change_y = 0, rotation=0.0):
        self.center_x = center_x
        self.center_y = center_y
        self.outer_radio = outer_radio
        self.inner_radio = inner_radio
        self.color = color
        self.change_x = change_x
        self.change_y = change_y
        self.rotation = rotation

        self.bump_sound = arcade.load_sound("bump.mp3")

    def set_position(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.center_x < self.outer_radio:
            self.center_x = self.outer_radio
            arcade.play_sound(self.bump_sound)
            self.change_x = 0

        elif self.center_x > SCREEN_WIDTH - self.outer_radio:
            self.center_x = SCREEN_WIDTH - self.outer_radio
            arcade.play_sound(self.bump_sound)
            self.change_x = 0

        elif self.center_y < self.outer_radio:
            self.center_y = self.outer_radio
            arcade.play_sound(self.bump_sound)
            self.change_y = 0

        elif self.center_y > SCREEN_HEIGHT - self.outer_radio:
            self.center_y = SCREEN_HEIGHT - self.outer_radio
            arcade.play_sound(self.bump_sound)
            self.change_y = 0

    def set_movement(self, change_x, change_y):
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        self.update()
        point_list = []
        rotation = self.rotation
        for i in range(5):
            point_list.append((self.center_x + self.outer_radio * sin(rotation), self.center_y + self.outer_radio * cos(rotation)))
            rotation += pi / 5
            point_list.append((self.center_x + self.inner_radio * sin(rotation), self.center_y + self.inner_radio * cos(rotation)))
            rotation += pi / 5
        arcade.draw_polygon_filled(point_list, self.color)

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self, image: Star):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.background_color
        self.image = image;

        self.click_sound = arcade.load_sound("click.mp3")

    def on_draw(self):
        arcade.start_render()
        self.image.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.image.set_movement(0, MOVEMENT_SPEED)
        elif key == arcade.key.DOWN:
            self.image.set_movement(0, -MOVEMENT_SPEED)
        elif key == arcade.key.LEFT:
            self.image.set_movement(-MOVEMENT_SPEED, 0)
        elif key == arcade.key.RIGHT:
            self.image.set_movement(MOVEMENT_SPEED, 0)

    def on_key_release(self, key, modifiers):
        self.image.set_movement(0, 0)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.image.set_position(x, y)
            arcade.play_sound(self.click_sound)


def main():
    star = Star(400, 300, 25, 10, arcade.color.YELLOW)
    window = MyGame(star)
    arcade.set_background_color((0, 60, 80))
    arcade.run()


main()
