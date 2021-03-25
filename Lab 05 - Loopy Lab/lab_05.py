import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = 0  # Instead of zero, calculate the proper x location using 'column'
            y = 0  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    for row in range(30):
        for column in range(30):
            x = 305 + 10 * column
            y = 5 + 10 * row
            if column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_3():
    # Use the modulus operator and an if/else statement to select the color.
    # Don't use multiple 'if' statements.
    s = 600
    h = 0
    for row in range(30):
        for column in range(30):
            x = s + 5 + column*10  # Instead of zero, calculate the proper x location using 'column'
            y = h + 5 + row*10 # Instead of zero, calculate the proper y location using 'row'
            if (row %2 == 0):
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_4():
    # Use the modulus operator and just one 'if' statement to select the color.
    base_x = 900
    base_y = 0
    for row in range(30):
        for column in range(30):
            x = base_x + 5 + row * 10   # Instead of zero, calculate the proper x location using 'column'
            y = base_y + 5 + column * 10  # Instead of zero, calculate the proper y location using 'row'
            if (row % 2 == 0 and column % 2 == 0):
                color = arcade.color.WHITE
            else:
                color = arcade.color.BLACK
            arcade.draw_rectangle_filled(x, y, 5, 5, color)


def draw_section_5():
    # Do NOT use 'if' statements to complete 5-8. Manipulate the loops instead.
    beginning = 15
    for row in range(305, 599, 10):
        for column in range(beginning, 301, 10):
            x = column  # Instead of zero, calculate the proper x location using 'column'
            y = row  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
        beginning += 10


def draw_section_6():
    pass


def draw_section_7():
    pass


def draw_section_8():
    base_x = 900
    base_y = 300
    for row in range(30):
        for column in range(29 - row, 30):
            x = base_x + 5 + row * 10
            y = base_y + 5 + column * 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()
main()
