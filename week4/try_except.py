# обработка исключений
# операторы try..except
# errors ->  связаны с кодом
#     #syntax error
#     # indentation error
#     #taberror

#исключения exceptions -> связаны с неправиьными данными которые передаются в код
    #ZeroDivisionError
    #ArithmeticError
    #NameError
    #IndexError
    #KeyError
    #BaseException - прородитель всех исключений
# try:
#     a = int(input('enter the number:'))
# except:
#     print('неправильные данные !')
# else:
#     print(a * 5)
#---------------------------------------------------------------------------------
# try:
#     <body>
# except:
#     <body> сработает если есть ошибка
# else:
#     <body> если нет ошибки
# finally:
#     <body> сработает в любом случае
#------------------------------------------------------------------------------------
# ls = ['john', 'snow', 'tirion']
# try:
#     a = int(input('Введите индекс:'))
#     print(ls[a])
# except ValueError: # в скобках ошибки которые нужно обработать
#     print('вы ввели неправильные данные!')
# except IndexError:
#     print('вы ввели неправильный индекс!')
#------------------------------------------------------------------
#отображение ошибки
# Exception as e (error)
# dict_ = {'1': 'one', '2': 'two', 'name': 'john'}


# try:        
#     key = input('Введите key:')
#     print(dict_[key])
# except Exception as e:
#     print(f'Oops,{e.__class__} Error!')
#-------------------------------------------------------------------
# try:
#     num1 = int(input('Enter num1:'))
#     num2 = int(input('Enter num2:'))
#     res = num1 / num2
# except ValueError:
#     print('Invalid input!')
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# else:
#     print(res)
# finally:
#     print('The End!')


# try:
# #     print(list(range(0,11)))
# except:
#     print('неверно')
# a = 1
# b = 0
# print(a / b)

# a = 'makers'

# print(int(a))

# if a == b:
#     print('hello')

# dict_ = {'a': 1, 'b': 2, 'c': 3}
# print(dict_[e])

# a = list(range(1, 31, 2))
# print(a)

