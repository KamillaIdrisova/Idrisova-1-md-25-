color1 = input('Введите первый цвет')
color2 = input('Введите второй цвет')
if color1 == 'Красный' and color2 == 'Синий' or color1 == 'Синий' and color2 == 'Красный':
    print('Зеленый')
elif color1 == 'Красный' and color2 == 'Желтый' or color1 == 'Красный' and color2 == 'Желтый':
    print('Оранжевый')
elif color1 == 'Желтый' and color2 == 'Синий' or color1 == 'Синий' and color2 == 'Желтый':
    print('Зеленый')
else:
    print('Неправильно введен цвет')