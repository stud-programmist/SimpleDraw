# -*- coding: utf-8 -*-

import simple_draw as sd
width = 1000
height = 600
sd.resolution = (width, height)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

'''while True:
    sd.clear_screen()
    # TODO здесь ваш код
    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()'''

# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл

def start_point():
    x = height + 100
    y = sd.randint(10, width - 10)
    return sd.get_point(x, y)


def snowflake_gen():
    return {'length': sd.random_number(10, 100), 'x': sd.randint(10, width - 10), 'y': height + sd.randint(100, 150)}


def snowf(N):
    
    snowflakes = []
    for _ in range(N):
        snowflakes.append(snowflake_gen())
    i = 0
    while True:
        sd.clear_screen()
        for snowflake in snowflakes:
            point = sd.get_point(snowflake['x'], snowflake['y'])
            sd.snowflake(point, snowflake['length'],sd.background_color)

            snowflake['x'] -= sd.randint(-10, 10)
            snowflake['y'] -= sd.randint(10, 25)

            point = sd.get_point(snowflake['x'], snowflake['y'])
            sd.snowflake(point, snowflake['length'], sd.COLOR_WHITE)
            if snowflake['y'] < sd.randint(0, 40):
                snowflakes.remove(snowflake)
        i += 1
        if i % 2 == 0:
            new_snowflake = snowflake_gen()
            snowflakes.append(snowflake_gen())

        sd.sleep(0.1)
        if sd.user_want_exit():
            break 
#snowf(40)


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла
# - в начале рисования всех снежинок вызвать sd.start_drawing()
# - на старом месте снежинки отрисовать её же, но цветом sd.background_color
# - сдвинуть снежинку
# - отрисовать её цветом sd.COLOR_WHITE на новом месте
# - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()

'''N = 30'''

def snowfall(N):

    def start_point():
        x = height + 100
        y = sd.randint(10, width - 10)
        return sd.get_point(x, y)

    def snowflake_gen():
        return {'length': sd.random_number(10, 100), 'x': sd.randint(10, width - 10), 'y': height + sd.randint(100, 150)}


    snowflakes = []

    for _ in range(N):
        snowflakes.append(snowflake_gen())
    
    i = 0

    sd.start_drawing()
    while True:
        for snowflake in snowflakes:
            point = sd.get_point(snowflake['x'], snowflake['y'])
            sd.snowflake(point, snowflake['length'],sd.background_color)

            snowflake['x'] -= sd.randint(-10, 10)
            snowflake['y'] -= sd.randint(10, 25)

            point = sd.get_point(snowflake['x'], snowflake['y'])
            sd.snowflake(point, snowflake['length'], sd.COLOR_WHITE)
            if snowflake['y'] < sd.randint(0, 40):
                snowflakes.remove(snowflake)
        i += 1
        if i % 2 == 0:
            new_snowflake = snowflake_gen()
            snowflakes.append(snowflake_gen())

        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break

snowfall(30)

'''x=sd.random_number(100, 600)
y = sd.random_number(100, 900)
sd.start_drawing()'
sd.snowflake(center=sd.get_point(x, y), length=50, color=sd.COLOR_WHITE, factor_a=0.6)
#sd.finish_drawing()'''

#-----------------------------------------------


sd.pause()
# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

