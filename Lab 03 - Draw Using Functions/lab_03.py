import arcade
from math import pi, sin, cos
arcade.open_window(1000, 800, "Paisaje")
arcade.set_background_color(arcade.color.BLIZZARD_BLUE)
arcade.start_render()
def draw_montanas():
        arcade.draw_triangle_filled(390, 100, 890, 100, 655, 460, arcade.color.DIM_GRAY)
        arcade.draw_triangle_filled(-10, 100, 490, 100, 255, 460, arcade.color.GRAY)
        arcade.draw_triangle_filled(655, 460, 610, 400, 695, 400, arcade.color.BABY_POWDER)
        arcade.draw_triangle_filled(173, 350, 335, 340, 255, 460, arcade.color.BABY_POWDER)
def draw_suelo():
    arcade.draw_lrtb_rectangle_filled(0, 1500, 100, 0, arcade.color.BUD_GREEN)
    arcade.draw_lrtb_rectangle_filled(0, 1500, 50, 0, arcade.color.CHARLESTON_GREEN)
    arcade.draw_lrtb_rectangle_filled(0, 1500, 60, 50, arcade.color.GRAY)

def draw_butterfly(x, y, color_rgb):
    """float*5, tuple-->mariposa
    OBJ: dibujar mariposa con parámetros"""
    arcade.draw_ellipse_filled(x, y, 15, 30, color_rgb, -30)
    arcade.draw_ellipse_filled(x, y - 10, 15, 30 - 10, color_rgb)
    arcade.draw_ellipse_filled(x + 20, y, 15, 30, color_rgb, 30)
    arcade.draw_ellipse_filled(x + 20, y - 10, 15, 30 - 10, color_rgb)

def draw_flower(x, y, rgb_color):
    """float*4,tuple-->flor
    OBJ: dibujar una flor"""
    arcade.draw_ellipse_filled(x-7, y, 12, 9, rgb_color)
    arcade.draw_ellipse_filled(x, y+5, 12, 9, rgb_color)
    arcade.draw_ellipse_filled(x+7, y, 12, 9, rgb_color)
    arcade.draw_ellipse_filled(x, y-5, 12, 9, rgb_color)
    arcade.draw_ellipse_filled(x, y, 12, 9, arcade.color.CHROME_YELLOW)


# Draw the tree
def draw_tree(x,y):
         arcade.draw_rectangle_filled(x, y, 20, 70, arcade.color.DONKEY_BROWN)
         arcade.draw_circle_filled(x, y+70, 45, arcade.color.DARK_MOSS_GREEN)
#Ejemplos
#draw_tree(50,50)
#draw_tree(200,200)



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
    # Asta de bandera
    arcade.draw_ellipse_filled(x, y-285, x-440, y-305, arcade.color.LIGHT_GRAY)
    arcade.draw_ellipse_outline(x, y-285, x-440, y-305, arcade.color.BLACK, 2)
    arcade.draw_lrtb_rectangle_outline(x-5, x+5, y+165, y-280, arcade.color.BLACK, 3)
    arcade.draw_lrtb_rectangle_filled(x-4, x+4, y+164, y-285, arcade.color.LIGHT_GRAY)
    # Cuadro de bandera
    arcade.draw_lrtb_rectangle_filled(x, x+240, y+160, y, arcade.color.RED)
    arcade.draw_lrtb_rectangle_outline(x, x+240, y+160, y, arcade.color.BLACK, 2)
    # Estrellas
    draw_star(x+40, y+110, 25, 10, arcade.color.YELLOW)
    draw_star(x+75, y+135, 10, 4, arcade.color.YELLOW, pi/10)
    draw_star(x+95, y+120, 10, 4, arcade.color.YELLOW, -pi/10)
    draw_star(x+95, y+95, 10, 4, arcade.color.YELLOW)
    draw_star(x+75, y+80, 10, 4, arcade.color.YELLOW, pi/10)

def draw_casa_nubes():

    # Tejado
    arcade.draw_triangle_filled(146, 400, 454, 400, 300, 502, (0, 0, 0))
    arcade.draw_triangle_filled(150, 400, 450, 400, 300, 500, (252, 0, 0))
    # Casa
    arcade.draw_lrtb_rectangle_filled(147, 453, 400, 100, (0, 0, 0))
    arcade.draw_lrtb_rectangle_filled(150, 450, 400, 100, (130, 108, 79))
    arcade.draw_lrtb_rectangle_filled(175, 240, 370, 305, (255, 255, 255))
    arcade.draw_line(207, 370, 207, 305, (0, 0, 0))
    arcade.draw_line(175, 337, 240, 337, (0, 0, 0))
    # Ventana derecha
    arcade.draw_lrtb_rectangle_filled(360, 425, 370, 305, (255, 255, 255))
    arcade.draw_line(392, 370, 392, 305, (0, 0, 0))
    arcade.draw_line(360, 335, 425, 335, (0, 0, 0))
    # Puerta
    arcade.draw_lrtb_rectangle_filled(247, 353, 218, 100, (0, 0, 0))
    arcade.draw_lrtb_rectangle_filled(250, 350, 215, 100, (107, 89, 65))
    arcade.draw_circle_filled(340, 157, 10, (0, 0, 0))
    # Nube izquierda
    arcade.draw_circle_filled(200, 525, 30, (255, 255, 255))
    arcade.draw_circle_filled(150, 525, 30, (255, 255, 255))
    arcade.draw_circle_filled(175, 540, 30, (255, 255, 255))
    # Nube derecha
    arcade.draw_circle_filled(800, 525, 30, (255, 255, 255))
    arcade.draw_circle_filled(750, 515, 30, (255, 255, 255))
    arcade.draw_circle_filled(775, 540, 30, (255, 255, 255))
    #Nube del centro
    arcade.draw_circle_filled(500, 625, 30, (255, 255, 255))
    arcade.draw_circle_filled(450, 645, 30, (255, 255, 255))
    arcade.draw_circle_filled(475, 640, 30, (255, 255, 255))
    # Chimenea
    arcade.draw_lrtb_rectangle_filled(350, 375, 500, 450, (252, 0, 0))
    # Humo chimenea
    arcade.draw_circle_filled(370, 520, 20, (168, 166, 163))
    arcade.draw_circle_filled(370, 530, 20, (168, 166, 163))
    arcade.draw_circle_filled(385, 530, 20, (168, 166, 163))



def draw_coche(l,h):
    """ int, int --> None
    obj: Dibujar coche de acuerdo a la altura h y a la distancia horizontal l"""
    #REJILLA DE PARABRISAS TRASERO
    arcade.draw_rectangle_filled(370+l, 366+h, 20, 10, arcade.color.BLACK)
    arcade.draw_rectangle_filled(336+l, 356+h, 20, 10, arcade.color.BLACK)
    arcade.draw_rectangle_filled(300+l, 346+h, 20, 10, arcade.color.BLACK)
    arcade.draw_rectangle_filled(268+l, 336+h, 20, 10, arcade.color.BLACK)

    #ALERON
    arcade.draw_rectangle_filled(180+l, 300+h, 10, 50, arcade.color.BLACK)
    arcade.draw_rectangle_filled(160+l, 300+h, 10, 55, arcade.color.BLACK)
    arcade.draw_triangle_filled(130+l, 330+h, 200+l, 320+h, 130+l, 345+h, arcade.color.BLACK)

    #CARROCERIA
    arcade.draw_rectangle_filled(425+l, 260+h, 575, 70, arcade.color.RED)
    arcade.draw_triangle_filled(710+l, 295+h, 250+l, 260+h, 430+l, 350+h, arcade.color.RED)
    arcade.draw_triangle_filled(710+l, 230+h, 150+l, 230+h, 430+l, 385+h, arcade.color.RED)
    arcade.draw_triangle_filled(130+l, 295+h, 150+l, 230+h, 430+l, 385+h, arcade.color.RED)

    #VENTANA Y PICAPORTE
    arcade.draw_triangle_filled(525+l, 310+h, 250+l, 310+h, 420+l, 365+h, arcade.color.WHITE)
    arcade.draw_rectangle_filled(375+l, 300+h, 14, 125, arcade.color.RED)
    arcade.draw_rectangle_filled(400+l, 290+h, 14, 10, arcade.color.BLACK)

    #DIBUJAMOS LAS RUEDAS DELANTE
    arcade.draw_circle_filled(600+l, 250+h, 50, arcade.color.BLACK)
    arcade.draw_circle_filled(600+l, 250+h, 45, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(600+l, 225+h, 20, arcade.color.BLACK)
    arcade.draw_circle_filled(600+l, 275+h, 20, arcade.color.BLACK)
    arcade.draw_circle_filled(575+l, 250+h, 20, arcade.color.BLACK)
    arcade.draw_circle_filled(625+l, 250+h, 20, arcade.color.BLACK)
    arcade.draw_circle_filled(600+l, 250+h, 10, arcade.color.RED)

    #DIBUJAMOS LAS RUEDAS ATRAS
    arcade.draw_circle_filled(200+l, 250+h, 50, arcade.color.BLACK)
    arcade.draw_circle_filled(200+l, 250+h, 45, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(200+l, 225+h, 20, arcade.color.BLACK)
    arcade.draw_circle_filled(200+l, 275+h, 20, arcade.color.BLACK)
    arcade.draw_circle_filled(175+l, 250+h, 20, arcade.color.BLACK)
    arcade.draw_circle_filled(225+l, 250+h, 20, arcade.color.BLACK)
    arcade.draw_circle_filled(200+l, 250+h, 10, arcade.color.RED)

draw_montanas()
draw_bandera(750,310)
draw_suelo()
draw_casa_nubes()
draw_flower(400,100,(153, 186, 221))
draw_flower(335,90,(153, 186, 221))
draw_flower(365,80,(251, 204, 231))
draw_tree(850,100)
draw_coche(275,-180)
draw_tree(50,100)
draw_flower(200,100,(153, 186, 221))
draw_flower(135,90,(153, 186, 221))
draw_flower(165,80,(251, 204, 231))
draw_flower(230,75,(251, 236, 93))
arcade.finish_render()
arcade.run()