def template(z, y, x):
    if z + y > x and z + x > y and y + x > z:
        print(f'Периметр: {z + y + x}')
        r = (z + y + x) / 2
        print('Площадь:', (r * (r - z) * (r - y) * (r - x)) ** 0.5)
        print('Равнобедренный:', "да" if z == y or z == x or y == x else "нет")
        print('Равносторонний:', "да" if z == y == x else "нет")
    else:
        print('None')


template(2, 4, 6)


