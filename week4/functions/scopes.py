#   Область видимости и пространство имен/scopes
# технология которая определяет котекст имени(переменные)
# в рамках которого мы можем ее использовать

# built-ins(Встроенная область видимости) -> print, len, max, min
#Global(глобальная область видимости) -> область одного файла
#Enclosed(не локальная(замкнуьая областьь видимости), nonlocal)
# local(локальная) -> область внутри одной функции

                   #GLOBAL
# x = 200

# def myFunc():
#     print(x)

# myFunc()  -- 200
#print(x) -- 200

#---------------------------------------------------------------------------------------------------
                    #local
# x = 200

# def myFunc():
#     print(x)
#     a = 300
#     print(a)

# myFunc() -- 200, 300
# print(a)   #NameError: name 'a' is not defined
#---------------------------------------------------------------------------------------------------

# a = 10 # global
# print # built-in

# def hello(): # global
#     a = 'Hello World!' # Local
#     print(a, 'local inside in func')

# hello()
# print(a, 'Global')
#---------------------------------------------------------------------
#LEGB - local, enclosed, global,built-in
# определяет поиск имен
#-----------------------------------------------------------------------
#Enclosed
# замкнутое пространство имен - локальное пространство имен, у которого есть внутреннее(вложенное) локальное пространство

# x = 'global'
# print(x, '1')   #global


# def enclosed(): # global 
#     x = 'enclosed'
#     def local(): #enclosed
#         x = 'local'
#         print(x, '3') #local
#     print(x, '2') #enclosed
#     local()
#     print(x, '4') #enclosed

# enclosed()
# print(x, '5')
#--------------------------------------------------------------------------------------------------
# a = 5

# def func():
#     print(a) # 5
#     a = a + 1  # нельзя поменять значние
#     print(a)

# func()
#-----------------------------------------------------------
# global -> позволяет изменять значение глобальной переменной 
# находясь внутри локальной области видимости

# nonlocal -> позволяет изменять значение не локальной (замкнутой)
# переменной находясь внутри локальной области видимости
#--------------------------------------------------------------------------------------------
                                  #Функция GLOBAL

# var = 0

# def increment(): #LEGB
#     global var
#     var += 1 # var = var + 1
    
# print(var)  #100
# increment()
# print(var) #101
#----------------------------------------------------------------
# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment
# c = counter()
# print(c()) # 1
# print(c()) # 2
# # print(counter())


# print(dir(__builtins__))
# print(len(dir(__builtins__)))
#--------------------------------------------------------------------------
# globals -- func которая возвращает все имена внутри глобальной области видимости
# locals -- функция которая возвращает все имена внутри глобальной области видимости и локальной
#---------------------------------------------------------------------------------------

def counter():
    num = 0
    def increment():
        nonlocal num
        num += 1
        return num
    return increment

def showStats(heroes, mobs):
    print()
    print(f'John Snow, ты убил: \n\tгероев: {heroes} \n\tмобов: {mobs}')
    print()


counter_heroes = counter()
counter_mobs = counter()
heroes = 0
mobs = 0
print('Приветствую вас, король севера John Snow, в вестеросе!')

while True:
    print('Тебе доступны следующие дейтвия:')
    print('1-убить Ланистера, 2-убить Белого ходока, 3-статистикa, 4-выйти из игры')
    choice = input('Введите выбранное действие:').strip()
    if choice == '1':
        heroes = counter_heroes()
        print('Вы обезглавили Ланистера!')
    elif choice == '2':
        mobs = counter_mobs()
        print('Вы убили белого ходока!')
    elif choice == '3':
        showStats(heroes, mobs)
    elif choice == '4':
        print('Пока Пока!')
        break
    