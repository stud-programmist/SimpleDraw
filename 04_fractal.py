# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код
#Часть 1
sd.resolution = (900, 700)



# сделать функцию рисования ветки из заданной точки,
# заданной длины, с заданным наклоном
'''def branch(point, angl, le):
     po = point
     ang = angl
     l = le
     
     
     for _ in range(6):
         angl-=30
         le-=30
         point_end_f = sd.get_vector(point, angl, le).end_point
         sd.line(start_point=point, end_point=point_end_f, color=sd.COLOR_YELLOW, width=3)
         point = point_end_f

     for _ in range(6):
         ang+=30
         l-=30
         po_end_f = sd.get_vector(po, ang, l).end_point
         sd.line(start_point=po, end_point=po_end_f, color=sd.COLOR_YELLOW, width=3)
         po = po_end_f


angle_0 = 90
length_0 = 200
point_0 = sd.get_point(450, 5)
point_end = sd.get_vector(point_0, angle_0, length_0/2).end_point
sd.line(start_point=point_0, end_point=point_end, color=sd.COLOR_YELLOW, width=4)
branch(point_end, angle_0, length_0)'''


#--------------------------------------------------------
#Часть 2
def draw_bunches(point_start, angle_start, length_start):
     if length_start < 10:
         return
     angle_list = (-30, 30)
     for angle_delta in angle_list:
         angle = angle_start + angle_delta
         point_end_f = sd.get_vector(point_start, angle, length_start).end_point
         sd.line(start_point=point_start, end_point=point_end_f, color=sd.COLOR_YELLOW, width=1)
         draw_bunches(point_end_f, angle, length_start * .75)


angle_root = 90
length_root = 100
point_root = sd.get_point(300, 0)
point_end = sd.get_vector(point_root, angle_root, length_root/2).end_point
sd.line(start_point=point_root, end_point=point_end, color=sd.COLOR_YELLOW, width=1)
draw_bunches(point_end, angle_root, length_root)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
