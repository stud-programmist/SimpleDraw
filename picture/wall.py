#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd

def draw_wall(wall_width, wall_height, brick_width, brick_height, wall_start_x, wall_start_y, color):

    sd.line(start_point=sd.get_point(wall_start_x, 200), end_point=sd.get_point(wall_start_x+wall_width, 200), color=(255, 140, 0) , width=200)
    sd.line(start_point=sd.get_point(wall_start_x, 350), end_point=sd.get_point(wall_start_x+wall_width, 350), color=(255, 140, 0) , width=205)
    

    border_line__left_start = sd.get_point(wall_start_x, wall_start_y)
    border_line_left_end = sd.get_point(wall_start_x, wall_start_y + wall_height)
    sd.line(border_line__left_start, border_line_left_end, color)  # Левая граница

    border_line_right_end = sd.get_point(wall_start_x + wall_width, wall_start_y + wall_height)
    border_line_right_start = sd.get_point(wall_start_x + wall_width, wall_start_y)
    sd.line(border_line_left_end, border_line_right_end, color)    # Верхняя граница
    sd.line(border_line_right_start, border_line_right_end, color)     # Правая граница

    for horizontal_line in range(wall_start_y, wall_height + wall_start_y, brick_height):
        start_line_point = sd.get_point(wall_start_x, horizontal_line)
        end_line_point = sd.get_point(wall_width + wall_start_x, horizontal_line)
        sd.line(start_line_point, end_line_point, color)

        if (horizontal_line + brick_height) % (brick_height * 2):
            x_shift = brick_width / 2
        else:
            x_shift = 0

        for vertical_line in range(wall_start_x, wall_width + wall_start_x, brick_width):
            start_line_point = sd.get_point(vertical_line + x_shift, horizontal_line)
            end_line_point = sd.get_point(vertical_line + x_shift, horizontal_line + brick_height)
            sd.line(start_line_point, end_line_point, color)

def draw_window(left_bottom, right_top, color):
    sd.rectangle(left_bottom, right_top, color)


def vector(vector_start, length, angle):
    v = sd.get_vector(vector_start, angle, length)
    return v.end_point

def draw_roof(point, length, angle):
    
        end_point = vector(point, length, angle)
        angle -=360/3
        
        sd.line(start_point=point, end_point=end_point, color=sd.COLOR_RED, width=120)
        point = end_point

