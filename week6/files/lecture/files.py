# Работа с файлами

# каретка - указатель - курсор

#open(<путь до файла>)

# file = open('/home/user/Рабочий стол/week6/lecture/files.py') # абсолютный путь
# file = open('files.py') # относительный путь (относительно той директории в которой вы работаете)

# Режимы работы с файлами 
# 1. Чтение -> r/r+ (read)
# 2. Запись -> w/w+ (write)
# 3. Добавления -> a/a+ (append)
# b, x, t



# file = open('text.txt', 'r')
# print(file.read())
# file.close()
#----------------------------
# file = open('text.txt')
# data = file.read()
# data = data.split('\n')
# print(data)
# file.close()
#----------------------------------
# Контекстный менеджер
# with open('text.txt') as file:  #file = open('text.txt')
#     data = file.readline()
#     print(data)
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())
#     print(file, 'inside')

# print(file, 'outside')
#------------------------------------------

# file.tell() -> Возвращает индекс, где находится каретка(курсор)
#file.seek(index) -> Перемещает курсор на индекс который вы передали

#---------------------------------

# with open('text.txt') as file:
    # print(file.readline().replace('\n', ''))
    # print(file.tell())
    # # file.seek(0)
    # print(file.readline().replace('\n', ''))
    # data = file.read()
    # index = data.index('\n')
    # file.seek(index+1)
    # print(file.readline().replace('\n', ''))
    # print(file.readlines()[1])
    # print(file.tell())
    # file.read()
    # file.seek(0)
    # print(file.tell())
    # print(file.readline().replace('\n', ''))
#-----------------------------------
# with open('text.txt', 'r') as file:
    # print(file.readline(7))
    # print(file.readlines(5)) # индекс того символа до которого хотим прочитать строку
    # print(file.read(5))

#-----------------------------------------------------------------


# with open('text.txt', 'a') as file1:
#     file1.write('Pervaya Strochka!\n')
#     file1.write('John Snow is bastard of Ned Stark!\n')
#     file1.write('This is lesson about files\n')
#     file1.write('no name added!\n')
#     file1.seek(0)
#     data = ['Bilal is genius\n', 'Tima is a good boy\n']
#     file1.writelines(data)
#------------------------------------------------------------------------

# with open('text.txt', 'a+') as file:
#     file.write('John Snow')
#     file.seek(0)
#     print(file.read())


from PIL import Image
import pytesseract
import re

def get_imei_code(image):
    string = pytesseract.image_to_string(image)
    # print(string, type(string))
    list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
    print(list_of_imei)

    with open('imei_codes.txt', 'w') as file:
        file.writelines(f'{x}\n' for x in list_of_imei)


image = 'imei.jpg'
get_imei_code(image)
