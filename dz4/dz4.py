#2
n1 = int(input('Vvedi chislo 1 '))
n2 = int(input('Vvedi chislo 2 '))
n3 = int(input('Vvedi chislo 3 '))
c = n1 or n2 or n3 or 'Введены все нули!'
bred = 'Нет нулевых значений!!!' or n1 or n2 or n3
print(c)
print(bred)

#3
if n1 > n2 + n3:
    print('a - b - c')
#4
if n1 < n2 + n3:
    print('b + c - a')
if n1 > 50 and (n2 > n1 or n3 > n1):
    print ('Вася!')
if n1 > 5 or n2 == n3 == 7:
    print('Петя')
