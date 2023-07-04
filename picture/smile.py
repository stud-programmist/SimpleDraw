#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import simple_draw as sd
def draw_smile(x, y, color):


    start_point = sd.get_point(x, y)
    sd.circle(start_point, 50, color, width = 4)
    #sd.circle(sd.get_point(x-14,y+15), 8, color, width = 3)
    rad, r =8,8
    for _ in range(5):
        sd.circle(sd.get_point(x-14,y+15), rad, sd.COLOR_DARK_GREEN, width = 3)
        rad-=1
    #sd.circle(sd.get_point(x-14,y+15), 2, sd.COLOR_BLACK, width = 3)
        
    #sd.circle(sd.get_point(x+14,y+15), 8, color, width = 3)
    for _ in range(5):
        sd.circle(sd.get_point(x+14,y+15), r, sd.COLOR_DARK_GREEN, width = 3)
        r-=1
    #sd.circle(sd.get_point(x+14,y+15), 2, sd.COLOR_BLACK, width = 3)
    
    #sd.line(sd.get_point(x-25,y-5), sd.get_point(x-10, y-20), color, 2)
    sd.line(sd.get_point(x-30,y-10), sd.get_point(x-15, y-25), color, 2)
    #sd.line(sd.get_point(x-9, y-20), sd.get_point(x+9, y-20), color, 2)
    sd.line(sd.get_point(x-14, y-25), sd.get_point(x+14, y-25), color, 2)
    #sd.line(sd.get_point(x+25, y-5), sd.get_point(x+10, y-20), color, 2)
    sd.line(sd.get_point(x+30,y-10), sd.get_point(x+15, y-25), color, 2)
    sd.line(sd.get_point(x,y+10), sd.get_point(x, y-10), color, 2)
    
    #тело человечка
    sd.line(sd.get_point(500, 230), sd.get_point(500, 260), color, 2)
    sd.line(sd.get_point(470, 230), sd.get_point(500, 260), color, 2)
    sd.line(sd.get_point(530, 230), sd.get_point(500, 260), color, 2)


    

    


    


'''  point_left = sd.get_point(x - 120, y - 100)
    point_right = sd.get_point(x, y)
    sd.ellipse(point_left, point_right, color)
    circle_point = sd.get_point(x - 35, y - 35)
    sd.circle(circle_point, 8, sd.invert_color(color))
    circle_point = sd.get_point(x - 85, y - 35)
    sd.circle(circle_point, 8, sd.invert_color(color))

    points = [
        sd.get_point(x - 85, y - 65),
        sd.get_point(x - 80, y - 70),
        sd.get_point(x - 75, y - 72),
        sd.get_point(x - 65, y - 74),
        sd.get_point(x - 61, y - 74),
        sd.get_point(x - 57, y - 74),
        sd.get_point(x - 47, y - 72),
        sd.get_point(x - 42, y - 70),
        sd.get_point(x - 37, y - 65),

        sd.get_point(x - 42, y - 75),
        sd.get_point(x - 47, y - 79),
        sd.get_point(x - 50, y - 81),
        sd.get_point(x - 57, y - 82),
        sd.get_point(x - 61, y - 82),
        sd.get_point(x - 65, y - 82),
        sd.get_point(x - 72, y - 80),
        sd.get_point(x - 75, y - 78),
        sd.get_point(x - 80, y - 75),
        sd.get_point(x - 85, y - 65),
    ]

    sd.lines(points, sd.invert_color(color))'''

