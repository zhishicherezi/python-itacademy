
import dpath.util
# 1. Вывести список польз(ключ - login)(L)

users = dict(Kapitan={'ФИО': 'Иван Куклусклан', 'рост': 189, 'вес': 85, 'BMI': 21},
                    Moryak={'ФИО': 'Маргарита Вурдак', 'рост': 179, 'вес': 55, 'BMI': 26},
                    Kivin={'ФИО': 'Саша Шапик', 'рост': 189, 'вес': 81, 'BMI': 17},
                    Bomber={'ФИО': 'Картье Микашевич', 'рост': 193, 'вес': 110, 'BMI': 31},
                    Nastenka={'ФИО': 'Гоша Куценко', 'рост': 177, 'вес': 80, 'BMI': 24})

def show_users():
    for key in users:
        print(key)
# Декоратор запроса ника

# 2. Посмотреть инфо о пользователе (рост, вес, шкала БМИ) (R)
def show_info():
    current_user = input('Введите никнейм пользователя ')
    print(users.get(current_user))


# 3. Изменить данные о пользователе (выбираем соот во ключу)
def upd_user():
    current_user = input('Кого меняем? ')
    print(users.get(current_user))
    user_data = input('Что изменить?  (Логин, Имя, Рост, Вес) ')
    value = input('новое значение = .. ')
    dpath.util.set(users, [current_user, user_data], value)

# 4. Удалить выбранного пользователя (D)
def del_user():
    current_user = input('Кого?')
    users.__delitem__(current_user)
    print('Done')

# 5. Add user
def add_user():
    new_user = input(str('enter login '))
    username = input(str('enter name '))
    userh = int(input('enter height '))
    userw = int(input('user weight '))
    userbmi = userw / (userh * userh)
    new_user_data = dict({'ФИО': username, 'рост': userh, 'вес': userw, 'BMI': userbmi})
    users[new_user] = new_user_data
    
def show_menu():
    MENU = """
    1. Вывести список польз(ключ - login) (L)
    2. Посмотреть инфо о пользователе (рост, вес, шкала БМИ) (R)
    3. Изменить данные о пользователе (выбираем соот во ключу) (U)
    4. Удалить выбранного пользователя (D)
    5. Добавить пользователя(C)
    6. Выход
    """
    print(MENU)
    return 

def main():
    while True:
        show_menu()
        choice = input('Ваш выбор? ') #1, 2, 3 ..
        if choice == ('1'):
            show_users()    # Вывести список польз(ключ - login)
        if choice == ('2'):
            show_info()     # Посмотреть инфо о пользователе (рост, вес, шкала БМИ) 
        if choice == ('3'):
            upd_user()
        if choice == ('4'):
            del_user()
        if choice == ('5'):
            add_user()
        else:
            choice == ('6')
    exit()
main()