#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd
def sun(x,y):
    rad =50
    for _ in range(10):
        sd.circle(sd.get_point(x,y), rad, sd.COLOR_YELLOW, width = 7)
        rad-=5

