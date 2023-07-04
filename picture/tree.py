#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import simple_draw as sd

def rand_delta(number, percent=50, is_positive=False):
    if is_positive:
        rand = sd.random_number(0, percent * 10) / 1000
    else:
        rand = sd.random_number(-percent * 10, percent * 10) / 1000

    return number * rand

def branch_width_color(length):
    if length > 50:
        width = 4
        color = (139, 69, 19)
    elif length > 30:
        width = 3
        color = (139, 69, 19)
        #color = (128, 128, 0)
    elif length > 15:
        width = 2
        color = (139, 69, 19)
        #color = (128, 128, 0)
        #color = (107, 142, 35)
    elif length < 15:
        width = 1
        color = (128, 128, 0)
        #color = (107, 142, 35)
        #color = (124, 252, 0)

    return width, color


def draw_branches(start_point, start_angle, branch_length, width=1, color=(139, 69, 19)):

    if branch_length < 8:
        return

    width, color = branch_width_color(branch_length)

    start_point = sd.vector(start_point, start_angle, branch_length, color, width)
    delta = int(20 + rand_delta(30, percent=40))
    branch_length *= (.75 + rand_delta(0.75, percent=20, is_positive=True))
    shift_angle = start_angle + delta
    draw_branches(start_point, shift_angle, branch_length, width, color)

    shift_angle = start_angle - delta
    draw_branches(start_point, shift_angle, branch_length, width, color)
