#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import simple_draw as sd
# создание окна, где будет отрисовано изображение. Параметры - размер окна
sd.resolution = (1200, 600)  

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
def bubble (point, step):
    radius = 50
    for _ in range(3):
        radius += step
        #функций рисования круга. Параметры: центр круга, радиус и ширина линий
        sd.circle(center_position=point, radius=radius, width=2) 

# задаём начальную точку, из которой выходит вектор 300 пикс. от левого экрана и 300 пикс. от низа экрана
point = sd.get_point(300,300) 
bubble(point, 10)

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
# TODO здесь ваш код
def bublle_color (point, step, color):
    radius = 50
    sd.circle(point, (radius+step), color, width = 3)
    
    
        
st = 5
for _ in range(50):
    point = sd.random_point()
    col = sd.random_color()
    bublle_color(point, st, col)
    st +=1
    

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
def bubble_row (point, step):
    sd.resolution = (1000, 600)
    radius = 50
    for _ in range(10):
        sd.circle(point, radius, width=2)
    
for x in range(100,1001,100):
    point = sd.get_point(x,300)
    bubble_row(point, 5)

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
def bubble_row_three (point, step):
    radius = 50
    for _ in range(10):
        sd.circle(center_position=point, radius=radius, width=2)

for y in range(100,301,100):
    for x in range(100,1001,100):
        point = sd.get_point(x,y)
        #bubble_row_three(point, 5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
def bubble_rand (point, clr):
    radius = 50
    sd.circle(point, radius, clr, 2)
        
for _ in range(100):
    point = sd.random_point()
    c = sd.random_color()
    bubble_rand(point, c)

sd.pause()
