import arcade
from math import pi, sin, cos

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

# inicializar la ventana y poner a dibujar
arcade.open_window(800, 600, "Drawing Example")
arcade.set_background_color(arcade.color.CYAN)
arcade.start_render()

# dibujar suelo
arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, (100,60,45))
arcade.draw_line(0, 150, 800, 150, arcade.color.BLACK, 2)

# dibujar sol y su entorno
arcade.draw_circle_filled(100, 500, 40, arcade.color.ORANGE)
arcade.draw_circle_outline(100, 500, 40, arcade.color.BLACK, 2)
draw_sunlight(100, 500, 50, 70)

# dibujar asta de bandera
"""
arcade.draw_ellipse_filled(500, 50, 60, 30, arcade.color.LIGHT_GRAY)
arcade.draw_ellipse_outline(500, 50, 60, 30, arcade.color.BLACK, 2)
arcade.draw_lrtb_rectangle_outline(495, 505, 500, 55, arcade.color.BLACK, 3)
arcade.draw_lrtb_rectangle_filled(496, 504, 499, 50, arcade.color.LIGHT_GRAY)
"""
# dibujar bandera
draw_bandera(500, 335)


# fin de dibujar
arcade.finish_render()
arcade.run()