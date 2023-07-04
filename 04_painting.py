#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать (или при необходимости написать) функции отрисовки
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)
import simple_draw as sd
import picture as pic

screen_width = 1200
screen_height = 720
sd.resolution = (screen_width, screen_height)
#Радуга
pic.rb()
#Солнце
pic.sun(980,660)
#Земля
pic.gr()


# Стена
brick_width, brick_height = 40, 20
wall_width, wall_height = 400, 340
start_wall_x, start_wall_y = 300, 100
#wall_color = (255, 140, 0)
wall_color =sd.COLOR_BLACK 

pic.draw_wall(wall_width, wall_height, brick_width, brick_height, start_wall_x, start_wall_y, wall_color)

# Окно
win_height = 160
win_width = 122
win_color = (240, 230, 140)
win_left_bottom = sd.get_point(wall_width/2 - win_width/2 + start_wall_x, wall_height/2 - win_height/4 + start_wall_y)
win_right_top = sd.get_point(wall_width/2 + win_width/2 + start_wall_x, wall_height/2 + win_height*3/4 + start_wall_y)

pic.draw_window(win_left_bottom, win_right_top, win_color)
#Крыша
start_p1 = sd.get_point(240,360)
start_p2 = sd.get_point(760,360)
pic.draw_roof(start_p1,300, 30)
pic.draw_roof(start_p2,300, 150)
#Человек

pic.draw_smile(int(wall_width/2 + start_wall_x * 2)-300, int(wall_height/2 - start_wall_y) + 240, sd.COLOR_BLACK)
#pic.draw_smile(int(wall_width/2 + start_wall_x * 2)-40, int(wall_height/2 - start_wall_y) + 250, sd.COLOR_RED)


# Дерево
root_point = sd.get_point(1000, 100)
pic.draw_branches(root_point, 90, 80)

root_point = sd.get_point(100, 100)
pic.draw_branches(root_point, 90, 55)

#Снежинки
x, y = 0, 100
for _ in range(25):
    pic.draw_snow(x,y)
    x+=50


sd.pause()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
