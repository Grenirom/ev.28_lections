# file1 = open('makers.txt', 'r')
# print(file1.read())


"""
1) - 'r' = для чтения
'r+' = для чтения и записи
'w' = только для записи, если указать несуществующий файл, то он создаст новый, возвращает кол-во символов строки
'w+' = для записи и чтения и стирает все соедржимое(если оно есть)
'a' = дозаписывает данные в файл
'a+' = позволяет и считать данные, и 
x = write, используется только в том случае, когда нужно создать новый файл
если файл существует, то выдает ошибку

"""

# file1 = open('makers.txt', 'r')
# print(file1.read(5))  #dknf. == возвращает только первые 5 символов в файле
# print(file1.read(5))  # zc.cm == следующие 5 символов
# ----------------------------------------------------------
# seek(int) = возвращает курсор в начало
# file1.seek(0)
# print(file1.read(5))  #dknf.
# ---------------------------------------------------------------
#readline() = выводит данные построчно
# print(file1.readline())  #dknf.zc.cms;mSC - первая строка
# print(file1.readline())  #hohohhoohho

# for line in file1:
#     print(line)
#-------------------------------------------
# readlines() = считывает строки файла в список
# list_ = file1.readlines() #['dknf.zc.cms;mSC\n', 'hohohhoohho\n', 'elelellelelelele\n', 'whshhshhshshshhsh\n']
# list1 = [line.replace('\n', '') for line in list_]
# print(list1) #['dknf.zc.cms;mSC', 'hohohhoohho', 'elelellelelelele', 'whshhshhshshshhsh']


# #-----------------------------------------------------------------------
# file2 = open('makers.txt', 'w')
# file2.write('it\'s such a beautiful day today' + '\n')
# file2.write('today is my birthday')
#writelines() - принимает список строк в качестве аргуемнта, склеивает все элементы
# list_mottos = ['sdnflzdck', 'esfucnald', 'dskfjc', 'sdkjbvn']
# list_motos = [motto + '\n' for motto in list_mottos]
# dict_ = {'name': 'carl', 'age': 2122, 'pap': 'jndgl'}
# file2.writelines(dict_)

#--------------------------------------------------------------------------
# file2 = open('bootcamp.txt', 'a') # Добавляет строки в конец, последовательно
# print(file2.write('makers' + '\n'))
# file3 = open('files.txt', 'a')
# list_mottos = ['sdnflzdck', 'esfucnald', 'dskfjc', 'sdkjbvn']
# list_mottos = [motto + '\n' for motto in list_mottos]
# file3.write('motot mottos' + '\n')
# for moto in list_mottos:
#     file3.write(moto)
#-------------------------------------------------

# file2 = open('moook.txt', 'x')
# print(file2.write('makers'))

#-------------------------------------------------------------



#with - оператор который автоматически закрывает файд после работы с ним

# with open('files.txt', 'r+') as my_file:
#     print(my_file.read())
#     my_file.write('additional string')

#------------------------------------------------------------


    # with open('task1.txt', 'r+') as my_file:
    #     my_file.writelines(['1', '\n2', '\n3', '\n4', '\n5', '\n6', '\n7', '\n8', '\n9', '\n10'])
    #     for line in my_file.readlines(8):
    #         print(line



with open('files.txt', 'r') as file:
    max_ = max(file.readlines())
    min_ = min(file.readlines())
    print(max_, min_)
