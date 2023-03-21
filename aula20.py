'''def titulo(txt):
    print('~'*30)
    print(txt)
    print('~'*30)


titulo('    Curso em video   ')
titulo('    Python')


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


soma(78, 98)


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2, 4, 4, 7)
contador(8, 55, 6, 9)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 7, 4, 8, 6, 9]
dobra(valores)
print(valores)'''


def soma (*val):
    s = 0
    for num in val:
        s += num
    print(f'Somando os valores {val} temos {s}')


soma(5, 6, 8)
soma(7, 3, 8, 80, 45, 6)