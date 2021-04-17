login = input('vvedite login ')
summa = 5000
def decorator(admin):
    def check(n):
        if login != 'admin':
            print ('доступ запрещен')
            return
        admin(n)
    return check
@decorator
def dai_schet(login):
    print(summa)
dai_schet(login)
    