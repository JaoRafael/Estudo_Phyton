n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
multi = n1 * n2
div = n1 / n2
di = n1 // n2
ex = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(soma, multi, div), end=' >>> ')
print('Divisão inteira é{:.3f}e a potência {}'.format(div, ex))