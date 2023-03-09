# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall import create_snow, draw_snow_background_color, move_snowflake, draw_snowflake_colour, delete_snowfalke


# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
N=int(input('Введите количество снежинок'))
create_snow(N)
while True:
    sd.start_drawing()
    draw_snow_background_color()
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    move_snowflake()
    #  сдвинуть_снежинки()
    draw_snowflake_colour()
    move_snowflake()
    sd.finish_drawing()
    delete_snowfalke()
    #  нарисовать_снежинки_цветом(color)

    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
