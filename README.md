# SimpleDraw

SimpleDraw это библиотека языка программирования Python, позволяющая рисовать графические примитивы с помощью pygame.

Основные элементы SimpleDraw это геометрические фигуры, "снежинки" и фракталы.

Эту библиотеку я изучала в рамках базового курса программирования на Python.

В репозитории собраны, на мой взгляд, интересные задачи с использованием SimpleDraw

:woman_teacher: Условие задачи:

1. Нарисовать мыльных пузырей. (код программы в файле 00_bubbles)

:writing_hand: Немного о реализации:

 - Для начала необходимо вызвать функцию создания окна,где будет отображен рисунок.

      Это можно сделать с помощью функции 
      
           simple_draw.resolution = (1200, 600)

      В скобках указывает размер окна.

 - Для рисования круга необходимо использовать специальную функцию simple_draw.circle(center_position=point, radius=radius, width=2)
 
     center_position - центр круга, заданный точкой с координатами (x,y), где значения x,y берутся исходя из размеров окна  [ пример введения начальной точки, из которой выходит вектор 300 пикс. от левого экрана и 300 пикс. от низа экрана размером (1200, 600): point = sd.get_point(300,300)]
     
     radius - радиус круга. Для увеличения радиуса круга необходимо с каждым циклом его увеличить. В файле за это отвечает конструкция 
     
        for _ in range(3):
            
            radius += step
        
            sd.circle(center_position=point, radius=radius, width=2)
        
     где step - значение для увеличеия радиуса круга. В коде переменная step инициализирована.
     
     width - толщина линий фигуры. Можно задать в виде значения или в виде width=2
     
     Кроме перечисленных параметров может быть параметр color - задание цвета фигуры. (подробнее о цвете будет сказано далее).
     
     Также можно задать метод, "рисующий" любую геометрическую фигуру в рандомной точке рабочего окна (подробнее об этом будет сказано далее)
     
     
     
Результат работы функции:

 - bubble
   <div align="left">
        <img src="https://github.com/stud-programmist/SimpleDraw/blob/main/image/1.png" width= "300"/>
    </div>
    
 - bubble_row
   <div align="left">
        <img src="https://github.com/stud-programmist/SimpleDraw/blob/main/image/2.png" width= "300"/>
    </div>
    
 - bubble_row_three
   <div align="left">
        <img src="https://github.com/stud-programmist/SimpleDraw/blob/main/image/3.png" width= "300"/>
    </div>
    
 - bublle_color
   <div align="left">
        <img src="https://github.com/stud-programmist/SimpleDraw/blob/main/image/4.png" width= "300"/>
    </div>
    
 - bubble_rand
   <div align="left">
        <img src="https://github.com/stud-programmist/SimpleDraw/blob/main/image/5.png" width= "300"/>
    </div>


---
2. Нарисовать разноцветные рожицы. (код программы в файле 08_smile)

:writing_hand: Немного о реализации:

 - Ранее было дано описание создания окна и построения окружности; поэтому в этом как и в других разделах, я буду подчёркивать "новые" функции SimpleDraw, используемые в настоящей программе.
 
 - Как было сказано в предыдущем описании реализации, положение окружности можно задавать вручную, прописав координаты точки. Однако это не всегда удобно, когда фигур на изображении нужно задать очень много. Для этого в  SimpleDraw существует встроенная функциия random_point(), которая задаёт рандомное значение точки (берутся исходя из размеров окна), от которой необходимо начинать "рисование". Задать точку можно таким образом:
 
        point = simple_draw.random_point()
   
   При обращении к переменной point выведется кортеж (point.x, point.y). Если нам нужно получить только одно значение, то в выводе прописываем 
   
   
       print(point.x)  или   print(point.y)
   
   
- Чтобы задать цвет фигуре можно воспользоваться функцией random_color().

 
      color = simple_draw.random_color()


   SimpleDraw выдаёт цвет, который ему "известен". Пользователь может задавать цвет самостоятельно (подробнее об этом будет сказано далее)

- Также необходимо "нарисовать" улыбку для рожицы. Для этого используем функцию line. Например:
  simple_draw.line(simple_draw.get_point(x-25,y-5), simple_draw.get_point(x-10, y-20), color, 2)
  
  Задаются следующие параметры:
      Начальная точка линии
      Конечная точка линии
      Цвет линии (необязательный параметр)
      Толщина линии (можно задать в виде значения или в виде width=2)

Результат работы функции:

 - smile
    <div align="left">
        <img src="https://github.com/stud-programmist/SimpleDraw/blob/main/image/6.png" width= "300"/>
    </div>

---

3. Нарисовать радугу. (код программы в файле 06_rainbow)

:writing_hand: Немного о реализации:

Чтобы нарисовать радугу в виде линий, использовалась встроенная функция line. Синтаксиск функции:

      simple_draw.line(start_point=sd.get_point(start_x, start_y), end_point=sd.get_point(end_x, end_y), color=rainbow_colors[i], width=4)
      
      где start_x, start_y - значение начальных координат линии; end_x, end_y - значение конечных координат линии. В коде перменные инициализированы
      Цвета радуги заданы в виде кортежа:

      

Результат работы метода:

 - simple_draw.line
   <div align="left">
        <img src="https://github.com/stud-programmist/SimpleDraw/blob/main/image/7.png" width= "300"/>
    </div>
 - simple_draw.circle
   <div align="left">
        <img src="https://github.com/stud-programmist/SimpleDraw/blob/main/image/8.png" width= "300"/>
    </div>

---
4. Нарисовать дерево. 

:writing_hand: Немного о реализации:

---

5. Нарисовать падающие снежинки. 

:writing_hand: Немного о реализации:

---
6. "Весенний пейзаж". 

:writing_hand: Немного о реализации:
