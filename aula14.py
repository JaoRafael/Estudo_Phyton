par = impar = 0
n = 1
while n != 0:
    n = int(input('Difite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números impares!')