def xyxax(a, b):
    if a > b:
        print(a, 'Максимально')
    elif a == b:
        print(a, 'Равно', b)
    else:
        print(b, 'Максимально')

xyxax(3, 4)  #прямая передача значений

x = 7
y = 7

xyxax(x, y) #передача переменных в качестве аргументов
