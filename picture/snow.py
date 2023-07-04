#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd
'''def draw_snow(x,y):
    for _ in range(10):
        sd.snowflake(center=sd.get_point(x, y), length=10, color=sd.COLOR_WHITE, factor_a=0.6)
        x+=10
        y-=1'''

N = 100

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
def draw_snow(x,y):
    snowflakes = {}
    for i in range(N):
        snowflakes[i] = {}
        #snowflakes[i]['x'] = sd.random_number(i * 12, (i + 1) * 12 - 12)
        snowflakes[i]['x'] = x
        snowflakes[i]['y'] = y
        snowflakes[i]['length'] = sd.random_number(5, 15)
        snowflakes[i]['factor_a'] = sd.random_number(1, 8)/10
        snowflakes[i]['factor_b'] = sd.random_number(1, 8)/10
        snowflakes[i]['factor_c'] = sd.random_number(30, 60)
        snowflakes[i]['speed'] = sd.random_number(5, 20)

    flag_of_stop = False

    for _ in range(4):
        sd.start_drawing()
        for i, snowflake_item in snowflakes.items():
            point = sd.get_point(snowflake_item['x'], snowflake_item['y'])
            sd.snowflake(center=point, length=snowflake_item['length'], factor_a=snowflake_item['factor_a'],
                     factor_b=snowflake_item['factor_b'], factor_c=snowflake_item['factor_c'],
                     color=sd.COLOR_WHITE)
            snowflake_item['y'] -= snowflake_item['speed']
            snowflake_item['x'] += sd.random_number(-15, 15)
            point = sd.get_point(snowflake_item['x'], snowflake_item['y'])
            #sd.snowflake(center=point, length=snowflake_item['length'], factor_a=snowflake_item['factor_a'],
                    #factor_b=snowflake_item['factor_b'], factor_c=snowflake_item['factor_c'])
            if snowflake_item['y'] < 10:
                #sd.snowflake(center=point, length=snowflake_item['length'], factor_a=snowflake_item['factor_a'],
                  #       factor_b=snowflake_item['factor_b'], factor_c=snowflake_item['factor_c'])
                snowflake_item['y'] = 700
        sd.finish_drawing()
        

