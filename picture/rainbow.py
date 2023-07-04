#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

def rb():
    point = sd.get_point(900, -100)
    r = 1090
    st = 20
    for i in range(len(rainbow_colors)):
        sd.circle(center_position=point, radius=r, color=rainbow_colors[i], width=20)
        r-=st
