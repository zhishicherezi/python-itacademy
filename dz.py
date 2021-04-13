weight = int(input(f'Введите вес '))
height = int(input(f'Введите рост '))
gender = str(input('Введите пол (м\ж) '))
bmi = int(weight / height**2 * 10000)
print(f'Ваш индекс массы тела: {bmi}')
x = list("================================================")
x.insert(bmi, "|")
print(''.join((str(i) for i in x[20:50])))
if gender == ('м'):
    if bmi < 20:
        print('Поднабрать бы')
    elif bmi < 30:
        print('нормас')
    elif bmi > 30:
        print('харош)')
if gender == ('ж'):
    if bmi < 20:
        print('улет')
    elif bmi < 30:
        print('нормас')
    elif bmi > 30:
        print('крошка)')