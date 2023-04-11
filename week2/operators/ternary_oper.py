# sentence = input('Введите предложение:')
# if sentence[-1] == '?':
#     print('Yes')
# else:
#     print('No')
#------------------------------------------------------------------------------------------
# sentence = input('Введите предложение:')
# print('Yes' if sentence[-1] == '?' else 'No') #использование тернарного оператора
#ternary operators (Тернарный оператор) -- это конструкция которая по своему дейстию аналогичн
# # конструкции 'if, else', но при этом записывается в однустрочку
# number = int(input('Введите число:'))
# res = 'even number' if number % 2 == 0 else 'odd number' #even - четное, odd - нечетное
# print(res)
#-------------------------------------------------------------------------------------
# <выражение если True> if <условие> else <выражение которое сработает если False>
#У тернарного оператора используется когда нужно 1 условие и 2 результата поместить в одну строчку
#-------------------------------------------------------------------------------------
# ls = [55,65,75,89,100,15,6]
#print(ls)
# choice = input('Введите max или min: ')
# # res = max(ls) if choice.lower() == 'max' else min(ls)
# # print(res)
# if choice.lower().strip() == 'max':
#     print(max(ls))
# elif choice.lower().strip() == 'min':
#     print(min(ls))
# else:
#     print('Invalid choice!')
# res = max(ls) if choice.lower().strip() == 'max' else min(ls) if choice.lower().strip() == 'min' else 'invalid choice!'
# print(res)
#----------------------------------------------------------------------------------------------------------
# flag = True
# symbols = '0,1,2,3,4,5,6,7,8,9' + '-' + '.' #0123456789-.

# while flag:
#     num1 = input('Введите первое число:')
#     is_correct_number = True
#     for x in num1:
#         if x not in symbols:
#             print('Вы ввели неправильное число!')
#             is_correct_number = False
#             break

#     if not is_correct_number:
#         continue

#     num2 = (input('Введите второе число:'))
#     for x in num2:
#         if x not in symbols:
#             print('Вы ввели неправильное число!')
#             is_correct_number = False
#             break
#     if not is_correct_number:
#         continue

#     num1 = float(num1) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)
#     # print(num1, type(num1))
#     # print(num2, type(num2))
#     operator = input('Введите оператор(+, -, *, /):').strip()

#     if operator == '+':
#         print(f'Результат: {num1 + num2}')
#     elif operator == '-':
#         print(f'Результат: {num1 - num2}')
#     elif operator == '*':
#         print(f'Результат: {num1 * num2}')
#     elif operator == '/':
#         if num2 == 0:
#             print('На ноль делить нельзя!')
#         else:
#             print(f'Результат: {num1 / num2}')
#     else:
#         print('Вы ввели неверный оператор!')

#     choice = input('Вы хотите продолжить?(yes/no)')
#     if choice.lower().strip() != 'yes':
#         flag = False   #break
#         print('Пока пока!')
#--------------------------------------------------------------------------------------------