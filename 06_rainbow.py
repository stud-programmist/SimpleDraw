#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

#Кортеж,содержащий цвета радуги
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
sd.resolution = (400, 500) #создание окна
#Начальные условия
start_x = 50
start_y = 50
end_x = 350
end_y = 450
step_x = 5
step_y = 5
    
for i in range(len(rainbow_colors)):
    start_x+=step_x
    end_x+=step_x
    # Отрисовка линий. Параметры: начал. точка линии, конеч. точка линии, цвет линии, толщина
    sd.line(start_point=sd.get_point(start_x, start_y), end_point=sd.get_point(end_x, end_y), color=rainbow_colors[i], width=4)
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

point = sd.get_point(400, -100) 

r = 400
st = 20
for i in range(len(rainbow_colors)):
    #sd.circle(center_position=point, radius=r, color=rainbow_colors[i], width=20)
    r-=st

sd.pause()
