#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
def smile(x,y, color):
    start_point = simple_draw.get_point(x, y)
    simple_draw.circle(start_point, 50, color, width = 4)
    simple_draw.circle(simple_draw.get_point(x-14,y+15), 8, color, width = 3)
    simple_draw.circle(simple_draw.get_point(x+14,y+15), 8, color, width = 3)
    
    simple_draw.line(simple_draw.get_point(x-25,y-5), simple_draw.get_point(x-10, y-20), color, 2)
    simple_draw.line(simple_draw.get_point(x-9, y-20), simple_draw.get_point(x+9, y-20), color, 2)
    simple_draw.line(simple_draw.get_point(x+25, y-5), simple_draw.get_point(x+10, y-20), color, 2)


for i in range(10):
    point = simple_draw.random_point()
    x = point.x
    y = point.y
    color = simple_draw.random_color()
    smile(x,y,color)

simple_draw.pause()
